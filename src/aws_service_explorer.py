import requests
import json

def get_service_list():
    """
    Retrieves the list of AWS services and their corresponding API action URLs.
    
    Returns:
        list: A list of dictionaries containing service names and URLs.
    """
    url = "https://servicereference.us-east-1.amazonaws.com/"
    response = requests.get(url)
    return json.loads(response.text)

def choose_service(services):
    """
    Prompts the user to choose a service from the list of available services.
    
    Args:
        services (list): A list of dictionaries containing service names and URLs.
    
    Returns:
        dict: The chosen service dictionary containing 'service' and 'url' keys.
    """
    print("Available services:")
    for service in services:
        print(f"- {service['service']}")
    
    while True:
        choice = input("Choose a service name: ")
        for service in services:
            if service['service'].lower() == choice.lower():
                return service
        print("Invalid service name. Please try again.")

def get_api_actions(url):
    """
    Retrieves the list of API actions for a given service URL.
    
    Args:
        url (str): The URL to the JSON object containing API action details.
    
    Returns:
        list: A list of API action names.
    """
    response = requests.get(url)
    data = json.loads(response.text)
    return [action['Name'] for action in data['Actions']]

def main():
    services = get_service_list()
    chosen_service = choose_service(services)
    api_actions = get_api_actions(chosen_service['url'])
    
    print(f"\nAPI actions for {chosen_service['service']}:")
    for action in api_actions:
        print(action)

if __name__ == "__main__":
    main()