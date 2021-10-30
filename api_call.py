import requests

# put your keys in the header
headers = {
    "app_id": "YOUR_APP_ID",
    "app_key": "YOUR_APP_KEY"
}

payload = '{"image":"YOUR_IMAGE_URL"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers);

# print r.content