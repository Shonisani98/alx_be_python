from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
