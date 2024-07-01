from datetime import datetime



def parse_datetime(datetime_str):
    try:
        # Try to parse with time
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        # If that fails, try to parse just the date
        return datetime.strptime(datetime_str, '%Y-%m-%d').date()

def get_default_start_end():
    now = datetime.now()
    start = now.replace(hour=10, minute=0, second=0, microsecond=0)
    end = now.replace(hour=23, minute=59, second=59, microsecond=0)
    return start, end

