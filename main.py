"""
Module to navigate through json file
"""
from pathlib import Path
import sys
import json


def get_location_to_json():
    """
    Ask user the location where json file is stored
    """
    while True:
        path = input("\nEnter a path to file: ")
        if Path(path).exists():
            return path
        print('Invalid path')


def read_file(path: str) -> dict:
    """
    Return dictionary with the iformation from file
    """
    with open(path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def parse(data: dict):
    """
    Go through json file structure and shows content
    """
    while True:
        if type(data) == list:
            if len(data) == 0:
                print("O files here. Nothing to display")
            else:
                print('\nThis object is list.', len(data), 'elements in this directory\nChoose\
 where to go by entering number in range from 1 to', len(data), 'or type EXIT to quit: ')
                element = int(input())
                if element == "EXIT":
                    sys.exit()
                elif element not in range(1, len(data) + 1):
                    print("\nInvalid location")
                    sys.exit()
                data = data[element-1]
        elif type(data) == dict:
            keys = list(data.keys())
            print('\n', len(keys), 'elements in this directory: \n')
            for i in keys:
                print(i)
            location = input('\nChoose where to go or type EXIT to quit: ')
            if location == "EXIT":
                sys.exit()
            elif location not in keys:
                print("\nInvalid location")
                sys.exit()
            data = data[location]
        else:
            print('\nNothing to display, except:')
            print(data)
            break


if __name__ == '__main__':
    parse(read_file(get_location_to_json()))
