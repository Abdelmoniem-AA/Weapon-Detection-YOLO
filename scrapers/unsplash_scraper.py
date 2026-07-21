import os
import requests

access_key = "API_KEY"

for page in range(1, 12):
    query = "gun"
    per_page = 30

    save_folder = "images"
    os.makedirs(save_folder, exist_ok=True)

    headers = {
        "Authorization": f"Client-ID {access_key}"
    }

    params = {
        "query": query,
        "page": page,
        "per_page": per_page
    }

    response = requests.get(
        "https://api.unsplash.com/search/photos",
        headers=headers,
        params=params
    )

    response.raise_for_status()

    data = response.json()
    photos = data.get("results", [])

    print(f"Found {len(photos)} images on page {page}.")

    for photo in photos:
        photo_id = photo["id"]
        image_url = photo["urls"]["full"]

        image = requests.get(image_url)

        with open(os.path.join(save_folder, f"{photo_id}.jpg"), "wb") as f:
            f.write(image.content)