import requests
from send_email import send_email

topic = "tesla"
language = "en"
api_key ="your_api_key"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-10-29&"
       "sortBy=publishedAt&"
       f"apiKey={api_key}&"
       f"language={language}")



# Make Request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = ("Subject: Today's news" + "\n" + body + article["title"] + "\n"
                + article["description"] + "\n"
                + article["url"] + 2*"\n")

body = body.encode('utf-8')
send_email(body)