def get_components(datetime:str)->list:                     #get_components checks the length, format and values of date time. Returns the values
                                                            #as a list. If the pattern is not matched, return [0,0,0,0,0,0]
    try:
        separated_date_and_time = datetime.split(" ")
        if(len(separated_date_and_time)!=2):
            raise ValueError("Date for time not entered")
        if(len(separated_date_and_time[0])!=10 or len(separated_date_and_time[1])!=8):
            raise ValueError("Incorrect Format")
        date_split = separated_date_and_time[0].split("/")
        if(len(date_split[0]) !=2 or len(date_split[1]) !=2 or len(date_split[2]) !=4 ):
            raise ValueError("Incorrect Date Format")
        time_split = separated_date_and_time[1].split(":")
        if(len(time_split[0]) !=2 or len(time_split[1]) !=2 or len(time_split[2]) !=2 ):
            raise ValueError("Incorrect Time Format")
        date_time_list = []
        for da in reversed(date_split):
            if(da.isnumeric() != True):
                raise ValueError("Non numeric date is not allowed")
            date_time_list.append(int(da))
        for ti in time_split:
            if(ti.isnumeric() != True):
                raise ValueError("Non numeric time is not allowed")
            date_time_list.append(int(ti))
        if(date_time_list[0] == 0 or date_time_list[1] == 0 or date_time_list[2] == 0):
            raise ValueError("Invalid Date entered")

        if(date_time_list[1]>12 or date_time_list[2]>31 or date_time_list[3]>23 or date_time_list[4]>60 or date_time_list[5]>60  ):
            raise ValueError("Incorrect value out of limit")
        return date_time_list
    except ValueError as ve:
        print(ve)
        return [0,0,0,0,0,0]