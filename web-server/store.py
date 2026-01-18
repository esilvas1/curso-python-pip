import requests

def get_categories():
    url = "https://api.escuelajs.co/api/v1/categories"
    r = requests.get(url) #response object
    print(r.status_code)  # Print the status code of the response   
    print(r.text)  # Print the response text (the content of the response)
    print(type(r.text))  # Print the type of the response text
    categories = r.json()  # Parse the response text as JSON
    for category in categories:
        print(category['name'])  # Print the name of each category