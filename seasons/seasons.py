from datetime import date
from inflect import engine
import sys
import re


def main():
    try:
        dob = to_date(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    mins = get_life_minutes(dob, date.today())
    print(mins + " minutes")

def to_date(dobs:str):
    if not re.search(r"^\d{4}-\d{2}-\d{2}$", dobs):
        raise ValueError("incorrect date format")
    dob = date.fromisoformat(dobs)
    return dob

def get_life_minutes(dob:date, today:date):
    delta = today - dob
    mins = round(delta.total_seconds() / 60)
    #print(mins)
    return engine().number_to_words(mins, andword="").capitalize()



if __name__ == "__main__":
    main()
