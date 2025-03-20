from datetime import datetime, timedelta

def parse_time_entry(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    return start_time, end_time

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

def get_time_range(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.now() - timedelta(days=1)  # Default to 1 day ago
    if end_date is None:
        end_date = datetime.now()  # Default to now
    return start_date, end_date

def get_week_range():
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=1)
    return start_date, end_date

def get_month_range():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    return start_date, end_date

def format_time_for_display(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")