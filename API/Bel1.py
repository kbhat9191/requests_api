import requests

baseurl = "https://belstarservice.nimblelos.com:8901"

endpointurl = "/api/v2/loan-demographics/BankDetail/1"

headers = {
    "accept": "application/json"
}


def bankdetails():
    response = requests.get(baseurl + endpointurl, headers=headers)
    if response.status_code == 200:
        print("Success OK")
    else:
        print("Error/no data found")

    resp = response.json()
    print(resp["accountHolderNameAsPerBank"])
    assert resp["branchName"] == 'SHAHADA', "Branch is invalid"

    for r in resp:
        print(r)


'''
{
  "id": 1,
  "accountType": "SB",
  "accountHolderNameAsPerBank": "Marathe Kunal Sanjay",
  "ifscCode": "UBIN0559717",
  "bankName": "UNION BANK OF INDIA",
  "branchName": "SHAHADA",
  "accountNumber": "597102010022524",
  "confirmedAccountNumber": "597102010022524",
  "bankLinkedMobileNo": "",
  "upiId": "",
  "dmsId": 0,
  "isBankVerified": true,
  "accountToBeUsedFor": "BOTH",
  "accountVerificationStatus": "Not Verified",
  "createdBy": "133",
  "createdDate": "2024-07-21T13:31:03.868Z",
  "modifiedBy": "133",
  "modifiedDate": "2024-07-21T08:01:01.942Z",
  "averageMonthlyBalance": "0.0000",
  "typeOfConstitution": "SNGL",
  "noOfDigitalSales": "",
  "totalNoOfSales": "",
  "accountOpeningDate": "2024-07-21",
  "isSaved": true
}
'''


bankdetails()