from InquirerPy import prompt
from rich.console import Console
from rich.text import Text

# Initialise Rich console
console = Console()

# Questions for user input
questions = [
    {"type": "input", "name": "title", "message": "Project Title:"},
    {"type": "input", "name": "description", "message": "Project Description:"},
    {"type": "input", "name": "installation", "message": "Installation Instructions:"},
    {"type": "input", "name": "usage", "message": "Usage Instructions:"},
    {
        "type": "list",
        "name": "license",
        "message": "Choose a license:",
        "choices": [
            "MIT License",
            "Apache License 2.0",
            "GNU General Public License (GPL v3)",
            "GNU Lesser General Public License (LGPL v3)",
            "Mozilla Public License 2.0 (MPL 2.0)",
            "Creative Commons Licenses (CC0, CC BY, etc.)",
            "Unlicense",
        ],
    },
    {"type": "input", "name": "contact", "message": "Contact / Author Information:"},
]
