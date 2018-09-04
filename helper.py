from datetime import datetime

def format_datetime(value):
    dt_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    return dt_obj.strftime("%Y-%m-%d %H:%M:%S")