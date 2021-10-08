from datetime import datetime as dt
def get_components(datetime:str)->list:
    '''
    get_components checks the length, format and values of date time. Returns the values
    as a list. If the pattern is not matched, return [0,0,0,0,0,0]
    '''
    try:
        date_object = dt.strptime(datetime, "%d/%m/%Y %H:%M:%S")
        return_object = [date_object.year, date_object.month, date_object.day, date_object.hour, date_object.minute, date_object.second]
        return return_object
    except ValueError as ve:
        print(ve)
        return [0,0,0,0,0,0]
