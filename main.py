import requests
import os
from send_email import send_email

topic = "tesla"
API_KEY = os.getenv("API_KEY_NEWSAPI")

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-02-13&" \
      "sortBy=publishedAt&" \
      f"apiKey={API_KEY}&"\
      "language=en"

request = requests.get(url)
content = request.json()

body = "Subject: Today's news" + "\n"

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] \
            + "\n" + article["description"] \
            + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
