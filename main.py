import requests

from send_email import send_email

topic = "tesla"
 
api_key ="38b62e3fc7b147fa948b46277ce027e738b62e3fc7b147fa948b46277ce027e7"
url="https://newsapi.org/v2/everything?"\
    f"q={topic}&" \
    "sortBy=publishedAt&"\
    "apiKey=38b62e3fc7b147fa948b46277ce027e7&" \
    "language=en"

#Make Request
request = requests.get(url)

#Get a dict
content = request.json()

body = "Subject: Today's news\n"
for article in content["articles"][:15]:
    body += (article["title"] or "") + "\n" + (article["description"] or "") + "\n" + (article["url"] or "") + "\n"

body = body.encode("utf-8")
send_email(message=body)