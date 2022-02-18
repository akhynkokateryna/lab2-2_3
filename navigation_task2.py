"navigation.py"

import twitter2


def navigate(dataset):
    "Creates a navigation in a JSON file based on user's input"
    current_data = dataset
    while True:
        if isinstance(current_data, str):
            print("Here is your data", current_data)
            break

        try:
            if isinstance(current_data, list):
                print("Here is the lenght of the list. Enter the number \
of the element you want to get.")
                print(len(current_data))
                num = input('Enter number: ')
                current_data = current_data[int(num)-1]
                continue

            if isinstance(current_data, dict):
                print("Here are the keys of the dictionary. Choose the one of them.")
                print(current_data.keys())
                key = input("Enter key: ")
                current_data = current_data[key]
                continue
        except KeyError:
            print("Wrong input")

if __name__ == "__main__":
    acct1 = input("Enter Twitter account: ")
    dataset1 = twitter2.get_data(acct1)
    navigate(dataset1)
