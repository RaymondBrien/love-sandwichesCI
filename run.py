# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) 
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
     """
     Get sales figures input from the user
     """
     
     print("Please enter the sales data from the last market")
     print('Data should be six numbers, serpated by commas')
     print('Example: 1,2,3,4,5,6\n') #new line for extra space in terminal
     
     data_string = input("enter sales data: ")

     sales_data = data_string.split(",")
     validate_data(sales_data)
     
     
def validate_data(values):
    """
    Inside the try, converts all string values to integers.
    Rasies value error if strings cannot be converted to integers, 
    or if the number of values is not 6.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 numbers are required, but {len(values)} were given'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again')

get_sales_data()

 