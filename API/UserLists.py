import requests

baseurl = "https://reqres.in"

endpointurl = {
    "Key1": "/api/users?page=2",
    "Key2": "/api/users/2",
    "Key3": "/api/users/23",
    "Key4": "/api/unknown",
    "Key5": "/api/unknown/2"
}

header = {
    "x-api-key": "reqres-free-v1"
}

s = requests.Session()

# get all list of users
def listofusers():
    response = s.get(baseurl + endpointurl["Key1"], headers=header)
    print(response.text)
    resp = response.json()

    print(response.status_code)
    print(response.json())
    print(response.headers)
    print(response.url)
    print(response.content)
    print(response.encoding)
    print(response.history)
    print(response.text)
    second_user = resp["data"][0]
    print("Second user data:", second_user)

    # Check if email matches
    if second_user["email"] == "michael.lawson@reqres.in":
        print("✅ Email address is in response")
    else:
        print("❌ Email address is NOT in response")


def singleuser():
    response = requests.get(baseurl + endpointurl["Key2"])
    if response.status_code == 200:
        print("Response OK")
    else:
        print("Response not OK")

    print(response.status_code)
    print(response.json())


def usernotfound():
    response = requests.get(baseurl + endpointurl["Key3"])
    if response.status_code == 401:
        print("User not found")
    else:
        print("User found")

    print(response.status_code)
    print(response.json())


def resourcelist():
    response = requests.get(baseurl + endpointurl["Key4"])
    if response.status_code == 200:
        print("User found -> Response OK")
    else:
        print("User not found")

    print(response.status_code)
    print(response.json())


def singleresource():
    response = requests.get(baseurl + endpointurl["Key5"], headers=header)
    print(response.headers)
    if response.status_code == 200:
        print("resource found -> Response OK")
    else:
        print("resource not found -> Error")
    print(response.status_code)
    print(response.json())
    resp = response.json()
    if resp["data"]["name"] == 'fuchsia rose':
        print("Name in Response is valid")
    else:
        print("Name in Response is not valid")


listofusers()
# singleuser()
# usernotfound()
# resourcelist()
#singleresource()
