import requests

from send_email import send_email

api_key ="38b62e3fc7b147fa948b46277ce027e738b62e3fc7b147fa948b46277ce027e7"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=38b62e3fc7b147fa948b46277ce027e7"

#Make Request
request = requests.get(url)

#Get a dict
content = request.json()

body = ""
for article in content["articles"]:
    body = body + (article["title"] or "") + "\n" + (article["description"] or "") + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)