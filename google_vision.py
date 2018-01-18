from decouple import config
import sys
import json
import requests
import base64


GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='

image_name = sys.argv[1]

try:
    imgfile = open(image_name, 'rb')
    imgbytes = imgfile.read()
    encoded_string = base64.b64encode(imgbytes).decode()
    imgfile.close()
except:
    print('There was an error opening the image')

api_url = GOOGLE_CLOUD_VISION_API_URL + config('GOOGLE_KEY')
req_body = json.dumps({
    'requests': [{
        'image': {
            'content': encoded_string
        },
        'features': [{
            'type': "TEXT_DETECTION",
            'maxResults': 30,
        }]
    }]
})

res = requests.post(api_url, data=req_body)
print(res.json())
