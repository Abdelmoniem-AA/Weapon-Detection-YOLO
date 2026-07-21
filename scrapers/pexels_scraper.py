import os
import requests

api_key = "API_KEY"

for i in range(7, 8):
    query = "person holding knife"
    per_page = 50

    save_folder = "images"

    os.makedirs(save_folder, exist_ok=True)

    headers = {"Authorization": api_key}

    params = {"query": query, "per_page": per_page, "page": i}

    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)

    data = response.json()

    photos = data.get("photos", [])

    print(f"Found {len(photos)} images.")

    for i, photo in enumerate(photos):

        photo_id = photo["id"]

        image_url = photo["src"]["large2x"]

        image = requests.get(image_url)

        with open(f"{save_folder}/{photo_id}.jpg", "wb") as f:
            f.write(image.content)