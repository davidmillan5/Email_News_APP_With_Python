import requests

api_key ="fcd2109498404de6b2a89bf9aabb772a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-10-29&sortBy=publishedAt&apiKey=fcd2109498404de6b2a89bf9aabb772a"

# Make Request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])