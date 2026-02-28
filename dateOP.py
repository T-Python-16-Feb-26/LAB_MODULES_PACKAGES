from datetime import date

def whats_the_date():
    """Prints out the today's date in a formatted manner"""
    formatted_date = date.today().strftime("%A, %d-%m-%Y")
    print(f"Today is {formatted_date}")