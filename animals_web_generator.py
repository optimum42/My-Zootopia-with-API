import data_fetcher


def load_html(file_path):
  """ Loads an HTML file """
  with open(file_path, "r") as handle:
      return handle.read()


def write_html(html, file_path):
  """ Writes an HTML file """
  with open(file_path, "w") as handle:
      handle.write(html)


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
    assert len(data) > 0
    for item in data:
        output += serialize_animal(item)
    return output


def get_animal_name():
    """ asks for an animal name and verifies the input """
    while True:
        animal_name = input("Enter a name of an animal: ")
        animal_name = animal_name.strip()
        if animal_name.isalpha():
            return animal_name


def main():
#    loaded_data = load_data("animals_data.json")
    animal_name = get_animal_name()
    animals = data_fetcher.fetch_data(animal_name)

    if len(animals) == 0:
        animals_html = f"<h2 style='text-align: center;'>The animal '{animal_name}' doesn't exist.</h2>\n"
    else:
        animals_html = animal_data_to_html(animals)
    html_template = load_html("animals_template.html")
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    file_name = "animals.html"
    write_html(html_output, file_name)
    print(f"Animals written successfully to file '{file_name}'")


if __name__ == "__main__":
    main()
