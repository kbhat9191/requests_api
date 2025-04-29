import requests

baseurl = "https://reqres.in"
endpointurl = "/api/login"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "x-api-key": "reqres-free-v1"
}

login1 = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

login2 = {
    "email": "eve.holt"
}


def successlogin():
    response = requests.post(baseurl + endpointurl, headers=headers, json=login1)
    resp = response.json()
    if response.status_code == 200:
        print("user logged in successfully")
    else:
        print("Either email/password is missing or wrong")

    print(resp["token"])
    #print(response.json())
    #print(response.status_code)


def faillogin():
    response = requests.post(baseurl + endpointurl, headers=headers, json=login2)
    if response.status_code == 400:
        print("Error: password missing")
    else:
        print("Logged in")

    #print(response.status_code)
    #print(response.json())


successlogin()
faillogin()
