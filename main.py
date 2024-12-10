from datetime import datetime as timesite


def get_day_name(number_formate_date):
    date_object = timesite.strptime(number_formate_date, '%d%m%Y')
    day_name = date_object.strftime("%A")
    return day_name

def excel_operation(day):
    pass

def main():
    user_input_date = input('Enter a Date (DDMMYYYY): ')
    day = get_day_name(user_input_date)
    print(day)

main()