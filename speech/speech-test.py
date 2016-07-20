import requests
import xml.etree.ElementTree as xmlt

url = 'https://asr.yandex.net/asr_xml'
params = {'uuid':'34353bf726ff4ea885eea4164d3ab413', 'key' : 'f1233cf8-c27a-4bad-9b5e-04f6ed2f265a', 'topic' : 'notes', 'lang':'ru-RU'}
headers = {"Content-Type": "audio/x-mpeg-3"}
files = {'file': open('speech.mp3', 'rb').read()}

req = requests.post(url, params = params, headers = headers, files = files)
income_xml = xmlt.fromstring(req.text)
command = income_xml[0].text
print(command)