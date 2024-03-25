import requests

# API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts"

# Custom headers
headers = {
    "User-Agent": "MyApp/1.0"
}

# Sending a GET request with custom headers
response = requests.get(api_url, headers=headers)

# Display response and headers
print("Response Status Code: ", response.status_code)
print("Response Headers: ")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# Response content (in this case, it's just an example)
print("Response Content: ", response.text)

# Data to be sent in the request body (in JSON format)
data = {
    "title": "Sample title",
    "body": "Sample text"
}

# POST request with data in the request body
post_response = requests.post(api_url, json=data)

# Handling the responses
print("POST Response Status Code: ", post_response.status_code)
print("POST Response Content: ", post_response.content)