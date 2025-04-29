import openpyxl

def read_login_data(file_path, sheet_name="LoginData"):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    login_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header row
        username, password = row
        login_data.append((username, password))

    return login_data


# Example usage
file_path = "testdata.xlsx"
credentials = read_login_data(file_path)

for user, pwd in credentials:
    print(f"Username: {user} | Password: {pwd}")
