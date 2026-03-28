import csv
import json
from pathlib import Path

DIR = Path(__file__).parent
DATA_DIR = DIR / "data"

def separator():
    print("====================================================================================================================================================================================")

def read_json_file(filename: str):
    try:
        with open(DATA_DIR / filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON.")
        return None

def divide_hundred():
    try:
        num = int(input("Enter a number to divide: "))
    except ValueError:
        print("Invalid input.")
    else:
        try:
            return 100 / int(num)
        except ZeroDivisionError:
            print("Cannot divide by zero.")

def read_int(prompt: str):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def convert_arr_to_ints(arr: list):
    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except ValueError:
            print(f'Element {i} is not an integer.')

# def csv_loader(filename: str):
#     try:
#         with open(DATA_DIR / filename, "r") as f:
#             return csv.reader(f)
#     except FileNotFoundError:
#         print("File not found.")
# CSV_LOADER SHOULD BE FINISHED LATER ON, NOT READY TO USE!
if __name__ == "__main__":
        print(divide_hundred())
        separator()
        print(read_json_file("valid.json"))
        separator()
        print(read_json_file("invalid.json"))
        separator()
        print(read_json_file("no file.json"))
        separator()
        print(read_int("Please enter a NUMBER: "))
        values = ["10", "abc", "25", "", "7"]
        convert_arr_to_ints(values)
        print(values)