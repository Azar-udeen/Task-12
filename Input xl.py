import openpyxl

# Create a workbook and select the active worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Define the headers
headers = ["Test ID", "Username", "Password", "Date", "Time of Test", "Name of Tester", "Test Result"]

# Write the headers to the first row
ws.append(headers)

# Add sample data (replace with your actual data)
sample_data = [
    [1, "Admin", "admin123", "", "", "Tester1", ""],
    [2, "User2", "password2", "", "", "Tester1", ""],
    [3, "User3", "password3", "", "", "Tester1", ""],
    [4, "User4", "password4", "", "", "Tester1", ""],
    [5, "User5", "password5", "", "", "Tester1", ""],
]

for row in sample_data:
    ws.append(row)

# Save the workbook
wb.save("login_test_data.xlsx")