import requests

response = requests.get('https://gitlab.com/api/v4/users/jeetdesai995/projects') 

# print(response.text)
# print(type(response.text))
# print(response.json())

project_list = response.json()

for project_item in project_list:
    print(f"Project name: '{project_item['name']}' and Project URL: '{project_item['http_url_to_repo']}'")