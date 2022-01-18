import requests
import json

msg="how are you ? you got a new assignment"

url="http://127.0.0.1:7500/serializer/postapi/Baibars/"
re=requests.get(url)

dta=json.load(re)
print(dta)
