from datetime import datetime as timesite
from  openpyxl import load_workbook
import web_operation


excel_file_path = 'Excel.xlsx'

# to get day name from user given date
def get_day_name(number_formate_date):   
    date_object = timesite.strptime(number_formate_date, '%d%m%Y')
    day_name = date_object.strftime("%A")
    return day_name

# operate all excel opeation from this function
def excel_operation(day):
    data_collected_column = 'C'                         # excel column name
    first_col = 3                                       # excel column data featching start porsition
    workbook = load_workbook(excel_file_path)           # loading excel file
    selected_sheet = workbook[day]                      # selecting worksheet depend on day name
    last_column = len(selected_sheet[data_collected_column])            # masurement column length for getting all data
    rng = selected_sheet[f"{data_collected_column}{first_col}:{data_collected_column}{last_column}"]        # featching data
    for cells in rng:                                                                                   # for print data
        for cell in cells:
            web_operation.web_to_scripting_operation(cell.value)

# main operation function
def main():
    user_input_date = input('Enter a Date (DDMMYYYY): ')
    day = get_day_name(user_input_date)                     #sending user giving data for geting week day
    print(f"\nYour Selected Day is: '{day}' \nand this day selected values are: \n")
    excel_operation(day)

main()