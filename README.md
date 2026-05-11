# API to Website Demo (Python)

A simple Python project for learning and practice purposes.  
This application fetches data from an external API and generates a local website from the retrieved data.

## Features

- Fetches data from a public or private API
- Processes and formats the data
- Generates a local HTML website
- Simple and beginner-friendly project structure
- Easy to extend with templates, databases, or frontend frameworks

---

## Project Structure

```text
project/
│
├── animals_web_generator.py
├── data_fetcher.py
├── requirements.txt
├── animals_template.html
├── animals.html
├── env.txt
└── README.md
```

## Installation

To install this project, simply clone the repository

## Install dependencies

All required Python packages are listed in requirements.txt.
Install them with:

```text
pip install -r requirements.txt
```

## Run the application

Start the project with:
```text
python/python3 animals_web_generator.py
```

## Output

After execution, the generated website will be available locally.
Open the file in your browser to view the generated website:
```text
animals.html
```

## Example Workflow

1. Request data from an API
2. Parse JSON response
3. Generate HTML content
4. Save website locally
5. Open website in browser

## Environment Variables

The API requires authentication, so create an .env file:

```text
API_KEY = YOUR_API_KEY
```

## License

This project is intended for educational purposes.
You may use, modify, and extend it freely.

