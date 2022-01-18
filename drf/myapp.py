import requests
import json
#
# URL="http://127.0.0.1:7000/create/"
#
#
# data={"age":"15",
#  "city":"pml",
#  "nationality":"pakistan",
#  "id_card":"33333999"}
# json_data=json.dumps(data)
#r=requests.post(url=URL, data=json_data)

msg="how are you ? you got a new assignment"

# url="http://127.0.0.1:7100/serializer/getapi/Baibars/"
# URL="http://127.0.0.1:7100/crud/updateapi/"
# re=requests.get(url)
# json_data=(re.json())
# strr=json.dumps(json_data) #to convert json response to string
# strr2=json.loads(strr) #to str to list
# dict1={
# "id":4,"name":"nomi_2","age":"22","phone":"03136627303"
# }

URL="http://127.0.0.1:8000/func_crud/func_get/"
# for get
# dict1={
# "id":1
# }
# for post
# dict1={
# "name":"baibarstech1",
# "age":"19",
# "phone":"03410704239"
# }
dict1={
"id":10,
"name":"baibarstech11",
"age":"19",
"phone":"03410704239"
}



# json_dat=json.dumps(dict1)
# headers={'content-type':'application/json'}
# r=requests.put(url=URL,headers=headers ,data=json_dat)
# print(r.json())
# print("______loads______")
# print(strr2)
# print("______type______")
# print(type(strr2))


def put_method():
	json_dat=json.dumps(dict1)
	headers={'content-type':'application/json'}
	r=requests.put(url=URL,headers=headers ,data=json_dat)
	print(r.json())

# put_method()

def delete_method(id):
	{"id":id}
	json_dat=json.dumps(dict1)
	headers={'content-type':'application/json'}
	r=requests.delete(url=URL,headers=headers ,data=json_dat)
	print(r.json())

delete_method(10)