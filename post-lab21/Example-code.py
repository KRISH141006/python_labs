import requests

# Define the API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Make a GET request
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    # Parse JSON response
    posts = response.json()
    print("Fetched Posts:")
    for post in posts[:5]:  # Print the first 5 posts
        print(f"Title: {post['title']}")
else:
    print(f"Failed to retrieve posts. Status code: {response.status_code}")
# Making a POST Request
# Create a new post.
import requests

# Define the API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Define the data to send
new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}

# Make a POST request
response = requests.post(url, json=new_post)

# Check the status code
if response.status_code == 201:
    # Parse JSON response
    created_post = response.json()
    print("Created Post:")
    print(f"Title: {created_post['title']}")
    print(f"Body: {created_post['body']}")
else:
    print(f"Failed to create post. Status code: {response.status_code}")
# Error Handling
# Handle potential errors in API requests.
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1000'  # Non-existent post

response = requests.get(url)

if response.status_code == 200:
    post = response.json()
    print("Fetched Post:", post)
else:
    print(f"Error: {response.status_code} - {response.reason}")
