from dateutil.parser import parse
def change_date_format(*date):
    Dates = []
    for d in date:
        str = parse(d).strftime('%Y%m%d')
        Dates.append(str)
    print(F"Date in year month day (YYYYMMDD) is : {Dates} ")

change_date_format("15/12/2016") # Enter your date here