def main():
    (year, month, day) = get_date()
    print_date(year, month, day)

def get_date():
    month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        date_str = input("Date: ")

        # first try to parse as MM/DD/YYYY
        try:
            (month, day, year) = date_str.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            pass
        else:
            if 1<=day <= 31 and 1<=month<=12 and year>=1:
                return (year, month, day)

        # now try DD Month, YYYY
        try:
           (str1, year) = date_str.split(",")
           (month, day) = str1.split(" ")
           month = month_names.index(month) + 1
           day = int(day)
           year = int(year)
        except ValueError:
            pass
        else:
            if 1<=day <= 31 and 1<=month<=12 and year>=1:
                return (year, month, day)

def print_date(year, month, day):
    print(f"{year:04}-{month:02}-{day:02}")

main()
