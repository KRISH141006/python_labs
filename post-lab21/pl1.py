import requests

class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        url = f"{self.base_url}/posts"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"GET Error: {response.status_code}")
            return None

    def create_post(self, title, body, user_id):
        url = f"{self.base_url}/posts"
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(url, json=data)

        if response.status_code == 201:
            return response.json()
        else:
            print(f"POST Error: {response.status_code}")
            return None


client = JSONPlaceholderClient()


print("Fetching Posts:")
posts = client.get_posts()
if posts:
    for p in posts[:5]:   
        print(f"- {p['title']}")


print("\nCreating New Post:")
new_post = client.create_post(
    title="My API Post",
    body="This post was created using my API client.",
    user_id=1
)

if new_post:
    print("Created Post:")
    print(new_post)
