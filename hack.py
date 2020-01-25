import json

import requests

def access_time():
    duration=[]
    for i in range(len(sites)):
        response1 = requests.get(mainUrl+sites[i])
        parsed_json1 = json.loads(response1.text)
        duration.append(parsed_json.get(i).get('duration'))
    for i in range(len(duration)):
        print(duration)

mainUrl="http://localhost:5600/api/0/buckets/"
response=requests.get(mainUrl)
str1="/events"
sites=[]
print(response.json())
parsed_json=json.loads(response.text)

for i in parsed_json:
    sites.append(parsed_json.get(i).get('id'))
   # print(parsed_json.get(i).get('id'))

print(sites)

for i in range(len(sites)):
    sites[i]+=str1
print(sites)

access_time()
#directly accessing the running ActivityWatch times

