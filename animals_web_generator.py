import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
REQUEST_URL = 'https://api.api-ninjas.com/v1/animals?name='


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_data_from_api(search_term = "fox"):
    """ Loads a JSON from API ninjas
    https://api-ninjas.com/
    """
    url = REQUEST_URL + search_term
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers)
    return response.json()


def get_request():
    search_term = input("Please enter a search term: ")
    url = REQUEST_URL + search_term
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers)
    print(response)
    print(response.json())
    for row in response.json():
        print(row)


def load_html(file_path):
  """ Loads an HTML file """
  with open(file_path, "r") as handle:
      return handle.read()


def get_skin_types(data):
    """ returns a set of the available skin types """
    skin_types = set()
    for item in data:
        skin_types.add(item.get("characteristics", {}).get("skin_type"))
    return skin_types


def write_html(html, file_path):
  """ Writes an HTML file """
  with open(file_path, "w") as handle:
      handle.write(html)


def print_animal_data(data):
    """ prints the animal data to the screen"""
    for item in data:
        complete_list = [
            item.get("name"),
            item.get("characteristics", {}).get("diet"),
            item.get("locations"),
            item.get("characteristics", {}).get("type"),
        ]
        if not None in complete_list: # only print if all fields are set
            print(f"Name: {complete_list[0]}")
            print(f"Diet: {complete_list[1]}")
            print(f"Location: ", end="")
            for location in complete_list[2][:-1]:
                print(f"{location}, ", end="")
            print(complete_list[2][-1])
            print(f"Type: {complete_list[3]}") # last one without ','
            print()


def animal_data_to_str(data):
    """ writes the animal data to a string and returns it """
    output = ""
    for item in data:
        complete_list = [
            item.get("name"),
            item.get("characteristics", {}).get("diet"),
            item.get("locations"),
            item.get("characteristics", {}).get("type"),
        ]
        if not None in complete_list: # only print if all fields are set
            output += (f"Name: {complete_list[0]}\n")
            output += (f"Diet: {complete_list[1]}\n")
            output += (f"Location: ")
            for location in complete_list[2][:-1]:
                output += (f"{location}, ")
            output += (complete_list[2][-1])
            output += (f"\nType: {complete_list[3]}\n\n") # last one without ','
    return output


def serialize_animal(animal):
    """ serializes the animal data to a string and returns it """
    ret = ""
    ret += "<li class='cards__item'>\n"
    ret += (f"<div class='card__title'>{animal.get('name')}</div>\n")
    ret += "<p class='card__text'>\n"
    ret += "<ul class='cards'>\n"
    diet = animal.get("characteristics", {}).get("diet")
    if diet:
        ret += (f"<li><strong>Diet:</strong> {diet}</li>\n")
    animal_class = animal.get("taxonomy").get("class")
    if animal_class:
        ret += (f"<li><strong>Class:</strong> {animal_class}</li>\n")
    family = animal.get("taxonomy").get("family")
    if family:
        ret += (f"<li><strong>Family:</strong> {family}</li>\n")
    locations = animal.get("locations")
    if len(locations) > 0:
        ret += "<li><strong>Location:</strong> "
        for location in locations[:-1]:
            ret += (f"{location}, ")
        ret += locations[-1]
        ret += "</li>\n"
    type = animal.get("characteristics", {}).get("type")
    if type:
        ret += (f"<li><strong>Type:</strong> {type}</li>\n")
    skin_type = animal.get("characteristics", {}).get("skin_type")
    if skin_type:
        ret += (f"<li><strong>Skin:</strong> {skin_type}</li>\n")
    ret += "</ul>\n"
    ret += "</p>\n"
    ret += "</li>\n"
    return ret


def animal_data_to_html(data):
    """ writes all the animals from data to a string and returns it """
    output = ""
    for item in data:
        output += serialize_animal(item)
    return output


def main():
#    loaded_data = load_data("animals_data.json")
    loaded_data = load_data_from_api()
    for animal in loaded_data:
        print(animal)
    print(len(loaded_data))

    print("My Animal Repository")
    print("--------------------\n")

    # show selection of available skin types to choose from
    skins = list(get_skin_types(loaded_data))
    print("0: All Types")
    i = 1
    for skin in skins:
        print(f"{i}: {skin}")
        i += 1

    choice = 0
    while True:
        try:
            choice = int(input("Choose a Skin Type Number: "))
            if 0 <= choice <= len(skins):
                break
        except ValueError:
            pass
        print("Invalid choice. Try again.")


    if choice == 0:
        filtered_data = loaded_data # animals of all types - no filter
    else:
        skin_type = skins[choice - 1]
        filtered_data = [item for item in loaded_data if
                         item['characteristics']['skin_type'] == skin_type]

    animals_html = animal_data_to_html(filtered_data)
    html_template = load_html("animals_template.html")
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    file_name = "animals.html"
    write_html(html_output, file_name)
    print(f"Animals written successfully to file '{file_name}'")


if __name__ == "__main__":
    main()
