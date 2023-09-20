import requests
import base64

# Print requests version
print(requests.__version__)

# send GET request to Google homepage
url = "http://www.gooogle.com"
requests.get(url)

# Send a GET request to the GitHub API
# Reference: https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-repository-content
github_api_url = f"https://api.github.com/repos/phamhuutriet/cmput404-lab1/contents/request.py?ref=master"
response = requests.get(github_api_url)
file_content = response.json()["content"]
decoded_content = base64.b64decode(file_content).decode("utf-8")
print(
    f"""File content:
      {decoded_content}
      """
)
