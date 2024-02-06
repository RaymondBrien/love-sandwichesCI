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
     while True:
        print("Please enter the sales data from the last market")
        print('Data should be six numbers, serpated by commas')
        print('Example: 1,2,3,4,5,6\n') #new line for extra space in terminal
        
        data_string = input("enter sales data: ")

        sales_data = data_string.split(",")
        
        if validate_data(sales_data):
            print("Data is valid")
            break
     return sales_data
     
     
def validate_data(values):
    """
    Inside the try, converts all string values to integers.
    Rasies value error if strings cannot be converted to integers, 
    or if the number of values is not 6.
    """
    print(values)
    try:
        [int(value) for value in values] #converts all string values to integers
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 numbers are required, but {len(values)} were given'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again')
        return False #continues while loop until data is valid
      
    return True


def update_sales_data(data):
    """
    Updates the sales data worksheet in the google sheet, add new row with list data provided.
    """
    print('Updating sales data...\n ')
    sales_worksheet = SHEET.worksheet("sales") #adds the sales data worksheet in the google sheet, add new row with list data
    sales_worksheet.append_row(data)
    print('Sales data updated!\n')

data = get_sales_data()
sales_data = [int(num) for num in data] #convert all sales data to integers to be accepte by google sheets
update_sales_data(sales_data)
 