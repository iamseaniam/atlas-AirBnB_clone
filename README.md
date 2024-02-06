# Atlas AirBnB Clone

Atlas AirBnB Clone is a simplified version of the AirBnB platform, designed to mimic some of its core functionalities. This project is primarily intended for educational purposes, providing a hands-on experience with Python development and object-oriented design principles.

## Features

- Command-line interface for managing AirBnB-like entities such as cities, places, amenities, reviews, states, and users.
- Persistent storage of data using JSON files.
- Implementation of a base model class that provides common attributes and methods for all entities.
- Support for creating, reading, updating, and deleting instances of different entity types.

## Installation

To install and run the Atlas AirBnB Clone, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Ensure that you have Python  3 installed on your system.
4. Run the `console.py` script to start the command-line interface.

## Usage

Once the command-line interface is running, you can execute various commands to manage the entities. Here are some examples:

- To create a new instance of a class: `$ create BaseModel`
- To display an instance: `$ show BaseModel  1234-1234-1234`
- To delete an instance: `$ destroy BaseModel  1234-1234-1234`
- To list all instances: `$ all BaseModel` or `$ all`
- To update an instance's attribute: `$ update BaseModel  1234-1234-1234 email "airbnb@example.com"`

## Commands

The command-line interface supports the following commands:

- `create`: Creates a new instance of a specified class and saves it to the JSON file.
- `show`: Displays the string representation of an instance based on the class name and ID.
- `destroy`: Deletes an instance based on the class name and ID.
- `all`: Lists all instances of a specified class or all instances if no class is specified.
- `update`: Updates an instance's attribute based on the class name, ID, attribute name, and new value.

## Contributing

Contributions to the Atlas AirBnB Clone are welcome. Please feel free to fork the repository, make changes, and submit pull requests.
