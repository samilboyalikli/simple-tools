import json
from datetime import datetime
import os

# TODO - add statistical results
# TODO - add basic UI
# TODO - add component for find spesific album

DATA_FILE = "dataset.json"
albums_by_day = {}
albums_by_month = {}
today = datetime.now()


def initialize_dataset():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding='utf-8') as file:
            json.dump([], file)
            print(f"[INFO] {DATA_FILE} created successfully.")


with open(DATA_FILE, "r", encoding="utf-8") as file:
    dataset = json.load(file)


def index():
    for album in dataset:
        day = album["released-on"]
        month = album["released-on"][-2:]

        albums_by_day.setdefault(day, []).append(album)
        albums_by_month.setdefault(month, []).append(album)


def chronologic_sorter(albums):
    albums = sorted(albums, key=lambda x: int(x["released-on"][:2])) 
    return albums


def album_saver(album):
    with open(DATA_FILE, "w", encoding='utf-8') as file:
        json.dump(dataset, file, indent=4, ensure_ascii=False)
        print("[INFO] New album added to the list.")
        print(album)


def date_checker():
    date = today.strftime("%d/%m")
    return albums_by_day.get(date, None)


def month_checker():
    month = today.strftime("%m")
    return albums_by_month.get(month, [])


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
        print("[INFO] Undefined process. Please just enter 0 or 1.")


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
        print("[INFO] Undefined process. Please just enter 0 or 1.")


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
        listener_choise = listener_option()
        if listener_choise:
            results = date_checker()
            if results:
                for result in results:
                    print(result)
            else: 
                "[INFO] There is no album for today. Time to explore :)"
        else:
            result_set = month_checker()
            sorted_result_set = chronologic_sorter(result_set)
            for result in sorted_result_set:
                print(result)


if __name__ == "__main__":
    index()
    main()
