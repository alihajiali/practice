from datetime import datetime


def chenge_date(year, month, day) :
    # زمان حال
    now = datetime.now()
    # تغییر زمان حال به زمان ورودی کاربر
    new_time = datetime.replace(now, year=year, month=month, day=day, hour=0, minute=0, second=0, microsecond=0)
    # زمان تغییر یافته به فرمت دیت تایم
    print(new_time)
    # جواب سوال
    return new_time.strftime('%A - %B - %Y')

print(chenge_date(2018, 6, 1))