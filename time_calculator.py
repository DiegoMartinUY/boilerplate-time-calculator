from datetime import datetime, timedelta

def add_time(start, duration, day = None):
    week_days = list(['monday','tuesday','wednesday','thursday','friday','saturday','sunday'])
    start = datetime.strptime(start, '%I:%M %p')
    duration = duration.split(':')
    add = timedelta(minutes=int(duration[1]), hours=int(duration[0]))
    new_time = start + add
    days = datetime.strftime(new_time, '%d')
    cant_days = int(days) - 1
    print_days = ''
    if( cant_days == 1 ):
        print_days = ' (next day)'
    if( cant_days > 1 ):
        print_days = ' (' + str(cant_days) + ' days later)'

    time = datetime.strftime(new_time, '%I:%M %p').split(':')
    hour = int(time[0])
    time = str(hour) + ':' + str(time[1])
    if(day != None):
        index = week_days.index(day.lower())
        if(index >= 0):
            print_days = ', ' + week_days[(new_time.weekday() + index) % 7].capitalize() + print_days
    ret = time + print_days



    return ret.rstrip()
