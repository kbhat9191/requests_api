import requests

baseurl = "https://reqres.in"

endpointurl = {
    "api1": "/api/users",
    "api2": "/api/users/2"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "x-api-key": "reqres-free-v1"
}

data = {
    "name": "karthik",
    "job": "leader"
}


def createuser():
    response = requests.post(baseurl + endpointurl["api1"], headers=headers, json=data)
    if response.status_code == 201:
        print("user is created")
    else:
        print("user already exits/ user creation error")

    print(response.status_code)
    print(response.headers)


def updateuserput():
    response = requests.put(baseurl + endpointurl["api2"], headers=headers, json=data)
    if response.status_code == 201:
        print("user is updated")
    else:
        print("user updation error")

    print(response.status_code)
    print(response.headers)


def updateuserpatch():
    response = requests.put(baseurl + endpointurl["api2"], headers=headers, json=data)
    if response.status_code == 200:
        print("user is updated")
    else:
        print("user updation error")

    print(response.status_code)
    print(response.headers)


createuser()
updateuserput()
updateuserpatch()