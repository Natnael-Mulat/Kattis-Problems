import requests #load the library another library BeautifulSoup

# response = requests.get(url='http://www.davidson.edu')
# print(response) # 200 is a good response and 404 is page not found
# print(response.text) # prints everything on the website

##API
response = requests.get("http://api.open-notify.org/iss-now.json")
response = response.json()
print(response["iss_position"]["longitude"])
print(response["iss_position"]["latitude"])