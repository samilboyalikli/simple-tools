import json
from datetime import datetime
import os

# TODO: 2. look-up the dataset to decrease O(n) complexity.
# TODO - add statistical results
# TODO - add basic UI
# TODO - add component for find spesific album

DATA_FILE = "dataset.json"


def initialize_dataset():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding='utf-8') as file:
            json.dump([], file)
            print(f"INFO: {DATA_FILE} created successfully.")


with open(DATA_FILE, "r", encoding="utf-8") as file:
    dataset = json.load(file)


def album_saver(album):
    dataset.append(album)
    with open(DATA_FILE, "w", encoding='utf-8') as file:
        json.dump(dataset, file, indent=4, ensure_ascii=False)
        print("INFO: New album added to the list.")
        print(album)


def date_checker(day):
    now = datetime.now()
    format = now.strftime("%d/%m")
    if day == format:
        return 1
    else:
        return 0


def month_checker(day):
    month = day[-2:]
    now = datetime.now()
    this_month = now.strftime("%m")
    if month == this_month:
        return True
    else:
        return False    


def user_option():
    option = input("""
For listen album print 0 and enter.
For add an album print 1 and enter.
                   """)
    if option == "0":
        return 0
    elif option == "1":
        return 1
    else:
        print("INFO: Undefined process. Please just enter 0 or 1.")


def listener_option():
    option = input("""
Enter 0 to listen to the album of the day.
Enter 1 to see the albums of the month.
                """)
    if option == "0":
        return True
    elif option == "1":
        return False
    else:
        print("INFO: Undefined process. Please just enter 0 or 1.")


def chronologic_sorter(albums):
    albums = sorted(albums, key=lambda x: int(x["released-on"][:2])) 
    for album in albums:
        print(album)


def main():
    user_choise = user_option()
    if user_choise:
        new_data = {}
        new_data["musician"] = input("Musician Name: ")
        new_data["album"] = input("Album Name: ")
        new_data["genre"] = input("Album Genre: ")
        new_data["released-on"] = input("When Released: ")
        album_saver(new_data)
    else:
        # TODO: 2. look-up the dataset to decrease O(n) complexity.
        albums = []
        listener_choise = listener_option()
        if listener_choise:
            for data in dataset:
                if date_checker(data["released-on"]):
                    print(data)
                else:
                    pass
        else:
            for data in dataset:
                if month_checker(data["released-on"]):
                        albums.append(data)
                else:
                    pass
        chronologic_sorter(albums)


if __name__ == "__main__":
    main()
