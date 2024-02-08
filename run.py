# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Raises value error if strings cannot be converted to integers, 
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


def calculate_surplus_data(sales_row):
    """
    Calculates the surplus data for the sales data provided.
    Surplus data = stock - sold 
    If negative, more were needed. If positive, less were needed.
    """
    print('Calculating surplus data...\n ')
    stock = SHEET.worksheet("stock").get_all_values() 
    stock_row = stock[-1]
    surplus_data = []
    
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    print(f'surplus data: {surplus_data}')
    return surplus_data


def update_worksheet(data, worksheet): 
    """ 
    Compare sales and surplus data and update the worksheet in the google sheet.
    Negative surplus = extra needing to be made. 
    Positive surplus = waste.
    """
    print(f'Updating {worksheet} worksheet!\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated!\n')

def get_last_five_entries_sales():
    """
    Gets last 5 entries of sales data, returns mean average plus 10% for sales incentive.
    """
    sales = SHEET.worksheet("sales")
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    return columns 
def main():
    """
    Call all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data] #convert all sales data to integers to be accepte by google sheets
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, 'surplus')

print('Welcome to Love Sandwiches!\n')
# main()
sales_columns = get_last_five_entries_sales()
 