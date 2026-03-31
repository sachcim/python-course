import csv
import json
from pathlib import Path

DIR = Path(__file__).parent
DATA_DIR = DIR / "data"

def separator():
    print("="*100)

def read_json_file(filename: str):
    try:
        with open(DATA_DIR / filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON.")

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
    converted_arr = []
    for i in range(len(arr)):
        try:
            converted_arr.append(int(arr[i]))
        except ValueError:
            print(f'Element {i} is not an integer.')
    return converted_arr

# def csv_loader(filename: str):
#     result = []
#     try:
#         with open(DATA_DIR / filename, "r") as f:
#             dict = csv.DictReader(f)
#             for row, index  in enumerate(dict, start = 1):
#                  if row["score"] is not None:
#                      result.append(row)
#                 else:
#                     print(f"Invalid input. on row {index}")
#     except FileNotFoundError:
#         print("File not found.")
#         return []
def csv_loader(filename: str):
    result = []
    try:
        with open(DATA_DIR / filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader, start=1):
                score_raw = (row.get("score") or "").strip()
                try:
                    score = int(score_raw)
                except ValueError:
                    print(f"Invalid score in row {index}, skipping.")
                    continue

                result.append({
                    "name": row.get("name"),
                    "score": score
                })
    except FileNotFoundError:
        print("File not found.")
        return []

    return result

if __name__ == "__main__":
        # print(divide_hundred())
        # separator()
        # test_file = read_json_file("valid.json")
        # if test_file is not None:
        #     print(test_file)
        # separator()
        #
        # test_file = read_json_file("invalid.json")
        # if test_file is not None:
        #     print(test_file)
        # separator()
        #
        # test_file = read_json_file("no file.json")
        # if test_file is not None:
        #     print(test_file)
        separator()
        # print(read_int("Please enter a NUMBER: "))
        values = ["10", "abc", "25", "", "7"]
        result = convert_arr_to_ints(values)
        print(f"Original: {values}")
        print(f"Converted: {result}")
        print(f"{csv_loader('scores.csv')}")
