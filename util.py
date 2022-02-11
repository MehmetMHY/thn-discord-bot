import datetime

def current_time():
    ctime = datetime.datetime.now()
    return {
        "second": ctime.second,
        "minute": ctime.minute,
        "hour": ctime.hour,
        "day": ctime.day,
        "month": ctime.month,
        "year": ctime.year
    }
