import os
import requests

for page in range(1, 12):
    query = "hand grenade"
    per_page = 30

    save_folder = "images"
    os.makedirs(save_folder, exist_ok=True)

    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": 6,
        "gsrlimit": per_page,
        "gsroffset": (page - 1) * per_page,
        "prop": "imageinfo",
        "iiprop": "url",
        "format": "json"
    }

    headers = {
        "User-Agent": "WeaponDatasetDownloader/1.0 (your_email@email.com)"
    }

    response = requests.get(
        "https://commons.wikimedia.org/w/api.php",
        params=params,
        headers=headers
    )

    response.raise_for_status()

    data = response.json()
    pages = data.get("query", {}).get("pages", {})

    print(f"Found {len(pages)} files on page {page}.")

    for photo in pages.values():

        image_url = photo["imageinfo"][0]["url"]

        if not image_url.lower().endswith((".jpg", ".jpeg")):
            continue

        filename = photo["title"].replace("File:", "")

        filename = filename.replace("/", "_").replace("\\", "_").replace(":", "_")

        try:
            image = requests.get(image_url, headers=headers)
            image.raise_for_status()

            with open(os.path.join(save_folder, filename), "wb") as f:
                f.write(image.content)

            print(f"Downloaded: {filename}")

        except Exception as e:
            print(f"Failed to download {filename}: {e}")

print("Done!")