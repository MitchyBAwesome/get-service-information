# AWS Service Explorer

AWS Service Explorer is a Python program that allows users to explore AWS services and their corresponding API actions.

## Features

- List all available AWS services
- Choose a specific service
- Retrieve and display API actions for the chosen service

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/aws-service-explorer.git
   cd aws-service-explorer
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the program using Python:

```
python src/aws_service_explorer.py
```

Follow the prompts to choose a service and view its API actions.

## Running Tests

To run the unit tests, use the following command:

```
python -m unittest discover tests
```

## The prompt I used to create this project

```
The program should list the service names. The JSON list containing the service names and the corresponding URLs for the JSON object that include the full list of API actions can be found here: https://servicereference.us-east-1.amazonaws.com/. Each item in the list contains a “service” and “url” property. The “service” property is the name of the service and the “url” property contains the URL to the JSON object that includes the API action details.
One the list of services has been determined, the project enable me to choose a specific service via an input prompt. The input prompt should appear on the command line and should prompt for “Choose a service name:”.  
Based on the service name I choose program should iterate over  the JSON list here https://servicereference.us-east-1.amazonaws.com/ and find the corresponding URL for the service I chose. The program should then retrieve the list of API actions for that service. The API actions are contain in a JSON object which contains an “Actions” list. The actions list contains a number of items where the name is “Name” and the value represents the specific API action. Return the list of API actions as an output to the command line. 

The project should be structure as follows:
- A subdirectory for your package’s source code
- A subdirectory for your package’s tests
- A README.md file with information about your package
- A LICENSE file with the license information
- A requirements.txt file that includes all of the requirement packages

The project should confirm to the following rules:
- Use meaningful variable names
- Write functions that do one thing and do it well
- Include comments to explain what your code does
- Follow PEP 8 guidelines for formatting and style
- Write unit tests to ensure your code works as expected

```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.