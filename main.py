from InquirerPy import prompt
from rich.console import Console
from rich.text import Text

README_FILE = "README.md"
LICENSE_CHOICES = [
    "MIT License",
    "Apache License 2.0",
    "GNU General Public License (GPL v3)",
    "GNU Lesser General Public License (LGPL v3)",
    "Mozilla Public License 2.0 (MPL 2.0)",
    "Creative Commons Licenses (CC0, CC BY, etc.)",
    "Unlicense",
]

# Questions for user input
QUESTIONS = [
    {"type": "input", "name": "title", "message": "Project Title:"},
    {"type": "input", "name": "description", "message": "Project Description:"},
    {"type": "input", "name": "installation", "message": "Installation Instructions:"},
    {"type": "input", "name": "usage", "message": "Usage Instructions:"},
    {
        "type": "list",
        "name": "license",
        "message": "Choose a license:",
        "choices": LICENSE_CHOICES,
    },
    {"type": "input", "name": "contact", "message": "Contact / Author Information:"},
]


def get_user_responses():
    """Get user responses to questions"""
    return prompt(QUESTIONS)


def format_readme_content(answers):
    """Format README content based on user responses"""
    return f"""
# {answers['title']}

## Description
{answers['description']}

## Installation
{answers['installation']}

## Usage
{answers['usage']}

## License
This project is licensed under the {answers['license']} license.

## Contact
{answers['contact']}
"""


def write_to_readme(readme_content):
    """Write README content to file"""
    with open(README_FILE, "w", encoding="utf-8") as readme_file:
        readme_file.write(readme_content)


def main():
    console = Console()
    answers = get_user_responses()
    readme_content = format_readme_content(answers)
    write_to_readme(readme_content)
    console.print(f"[bold green]README.md has been successfully created![/bold green]")


if __name__ == "__main__":
    main()
