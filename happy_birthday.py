from collections import defaultdict
from datetime import datetime, timedelta


def main(users: dict):
    users = transform_date(users)
    birthday_list = defaultdict(list)
    for name, birthday in users.items():
        delta = birthday - datetime.now()
        if int(delta.days) == -1:
            birthday_list[birthday.strftime("%A")].append(name)
        elif int(delta.days) in range(0, 6):
            birthday = birthday_on_weekend(birthday)
            birthday_list[birthday.strftime("%A")].append(name)
    output_birthday_list(birthday_list)


def transform_date(users: dict) -> dict:
    """Function of counting the date of the people's birth until the day of the people's day at the current rotation"""

    current_year = (datetime.now()).year
    for name, birthday in users.items():
        users.update({name: birthday.replace(year=current_year)})
    return users


def birthday_on_weekend(birthday: datetime) -> datetime:
    """The function handles birthdays that fall on a holiday"""

    if birthday.strftime("%A") == "Saturday":
        birthday += timedelta(days=2)
    elif birthday.strftime("%A") == "Sunday":
        birthday += timedelta(days=1)
    return birthday


def output_birthday_list(birthday_list: dict):
    """The function displays a list of colleagues who should be congratulated for the week"""

    for day, name in birthday_list.items():
        name = ", ".join(name)
        print(f"{day}: {name}")


def read_birthday_list(source: str) -> dict:
    """The function reads the file with the source data and returns the received data
    to the dictionary "Name: Date of Birth (format YYYY-MM-D)" """

    with open(source, "r") as file:
        users = {}
        for line in file.readlines():
            name, birthday = (line.split())[0], (line.split())[1]
            users.update({name: datetime.strptime(birthday, "%Y-%m-%d")})
        return users


if __name__ == "__main__":
    users = read_birthday_list("list_birthday.txt")
    main(users)
