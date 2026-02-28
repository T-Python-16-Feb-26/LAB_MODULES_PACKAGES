from datetime import date
def current_date():
    """Prints the current date in YYYY-MM-DD format.""" 
today = date.today()
print("current_date:", today.strftime("%Y-%m-%d"))

