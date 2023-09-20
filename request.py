import requests

# Print requests version
print(requests.__version__)


# send GET request to Google homepage
url = "http://www.gooogle.com"
response = requests.get(url)
