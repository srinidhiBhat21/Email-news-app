import requests

api_key ="38b62e3fc7b147fa948b46277ce027e738b62e3fc7b147fa948b46277ce027e7"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-06-24&sortBy=publishedAt&apiKey=38b62e3fc7b147fa948b46277ce027e7"

#Make Request
request = requests.get(url)

#Get a dict
content = request.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])
