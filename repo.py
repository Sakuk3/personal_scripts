import requests
import json

username = "Sakuk3"
repo_url = "https://api.github.com/users/{username}/repos".format(username=username)

data = requests.get(url=repo_url).json()
table = """
| Name          | Description           |
| ------------- |:-------------:|
"""
table_row = "| {link} | {description} |\n"
for key in data:
    table += table_row.format(
        link="[{name}]({url})".format(
            name=key["name"],
            url=key["html_url"]
        ),
        description=key["description"]
    )

print(table)