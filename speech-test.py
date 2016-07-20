import requests

url = 'https://asr.yandex.net/asr_xml'
params = {'uuid':'34353bf7-26ff-4ea8-85ee-a4164d3ab413', 'api_key' : 'f1233cf8-c27a-4bad-9b5e-04f6ed2f265a', 'topic' : 'notes', 'lang':'ru-RU'}
headers = {"Content-type": "audio/x-wav"}
files = {'file': open('speech.wav', 'rb')}

req = requests.post(url, params = params, headers = headers, files = files)
print(req.status_code)