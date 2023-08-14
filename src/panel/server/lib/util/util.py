import random
import datetime
import string
# from this import d
import colorama
import json
import platform
import os
import re
import string
from os import system,name
from colorama import Fore

colorama.init(autoreset=True) # colorful terminal

# for the coloring the console for debugging
success = Fore.GREEN
warning = Fore.YELLOW
error   = Fore.RED
# for the coloring the console for debugging


GEN_API_KEY_CHOOSE = string.ascii_uppercase + string.digits + \
    string.ascii_lowercase + string.punctuation + string.ascii_letters

REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

COMMANDS = {
    "pip-linux"          : "python3 -m pip install --upgrade pip",
    "pip-windows"        : "python -m pip install --upgrade pip",
    "update-package"     : "pip-review --auto", #<=======================> this is an external package for updating the packages
    "Decrypt-package"    : "pip-Decrypt", #<=============================> this is an external package for Decrypting what needs to be updated
    "windows-cls"        : "cls",
    "linux-cls"          : "clear",
    "install-pkg-win"    : "pip install -r requirements.txt",
    "install-pkg-linux"  : "pip3 install -r requirements.txt"
}

OS_SUPPORTED = {
    "mac"     : "Darwin",
    "linux"   : "Linux",
    "windows" : "Windows"
}


#region getting basic time, date, month, by day, weekday
def get_time() -> str:  # * get full 12 hour time
    return f'{datetime.datetime.now().strftime("%I")} : {datetime.datetime.now().strftime("%M")} {datetime.datetime.now().strftime("%p")}'


def get_Date() -> str:  # * get full date
    return datetime.datetime.now().strftime("%x")


def getMonth() -> str: # * full name of month
    return datetime.datetime.now().strftime("%B")


def getMonthDay() -> str: # * get the day of the month
    return datetime.datetime.now().strftime("%d")


def getWeekDay() -> str: # * get fullname of the weekday
    return datetime.datetime.now().strftime("%A")

#endregion


#region basic utilities
def generateAPIKey(Size) -> str:  # * generating the random api key and saving it with each user
    return ''.join(random.choice(GEN_API_KEY_CHOOSE) for _ in range(Size))


def open_json(path: str, title: str, json_usage='r') -> dict:# * opening json file
    try:
        with open(f"{path}/{title}.json", json_usage) as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error opening JSON file: {e}")
        return {}  # Return an empty dictionary in case of an error


def write_json(path: str, title: str, data=None, write_type='w', indents=4) -> None:
    if data is None:
        data = {}

    try:
        with open(f"{path}/{title}.json", write_type) as file:
            json.dump(data, file, indent=indents)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error writing JSON to file: {e}")



def write_to_file(path: str, title: str, file_type: str, data: str, write_type: str = "w") -> bool:
    if not path or not title or not data:
        raise ValueError("Path, title, and data must be provided.")

    try:
        with open(f"{path}/{title}.{file_type}", write_type) as file:
            file.write(data)
        return True
    except IOError as e:
        print(f"{error}Error writing to file: {e}")
        return False



def save_html_to_file(html_content:str, file_path:str) -> None: # writes html_content to a file to file_path
    # purpose is for auto generating documentation. once the algorithm works
    if os.path.exists(file_path):
        print(f"Error: File already exists at {file_path}. Choose a different file path.")
        return

    with open(file_path, "w") as file:
        file.write(html_content)
    print(f"HTML file saved successfully at {file_path}")


def rnd(max:int) -> int:  # * random number generator default min = 1
    return random.randint(1, max)


def rnd(min:int, max:int) -> int:  # * random number generator between min and max
    return random.randint(min, max)


def evenRnd(min:int, max:int, step=2) -> int: # generating random even numbers
    return random.randint(min, max, step)


def oddRnd(min:int, max:int, step=3) -> int: # generating random odd numbers
    return random.randint(min, max, step)


def isDict(data) -> bool: # returns true or false if data is of type dict or not
    if type(data) is dict:
        return True
    else:
        return False

def isString(data) -> bool: # returns true or false if data is of type string or not
    if type(data) is str:
        return True
    else:
        return False

    
def isInt(data) -> bool: # returns true or false if data is of type int or not
    if type(data) is int:
        return True
    else:
        return False

    
def isFloat(data) -> bool: # returns true or false if data is of type float or not
    if type(data) is float:
        return True
    else:
        return False

    
def toInt(data) -> int: # type casting data to int
    return int(data)


def toFloat(data) -> float: # type casting data to Float
    return float(data)


def toString(data) -> str: # type casting data to String
    return str(data)


def toJson(data:dict) -> json: # dump data into a json object
    return json.dumps(data)


def toUpper(data:str) -> str: # returns data as upper case
    return data.upper()


def toLower(data:str) -> str: # returns data as lower case
    return data.lower()


def isLower(data:str) -> bool: # returns true or false if data is lower case or not
    return data.islower()


def isUpper(data:str) -> bool: # returns true or false if data is lower case or not
    return data.isupper()


def cls() -> None:  # * clear the console
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#endregion


#region advanced utilities
def getPcDevOs() -> str: # getting the os that the python script is runTerminalCommand on 
    return platform.system()


def delFile(title:str) -> None: # deleting specific file with title
    if os.path.exists(title):
      os.remove(title)
    else:
        return f"The file {title} does not exist"


def runTerminalCommand(command) -> None: # runTerminalCommand terminal commands
    os.system(command)


def update_packages() -> None: # auto updater to be used in development
    try:
        if getPcDevOs() == OS_SUPPORTED['linux'] or getPcDevOs() == OS_SUPPORTED['mac']:
            # runTerminalCommand(COMMANDS["pip-linux"])
            # runTerminalCommand(COMMANDS["Decrypt-package"]) # Decrypting first what needs to be updated
            runTerminalCommand(COMMANDS["update-package"]) # update any packages that need updating
            runTerminalCommand(COMMANDS["install-pkg-linux"]) # install packages from requirements.txt

        elif getPcDevOs() == OS_SUPPORTED['windows']:
            # runTerminalCommand(COMMANDS["pip-windows"])
            # runTerminalCommand(COMMANDS["Decrypt-package"]) # Decrypting first what needs to be updated
            runTerminalCommand(COMMANDS["update-package"]) # update any packages that need updating
            runTerminalCommand(COMMANDS["install-pkg-win"]) # install packages from requirements.txt

        else:
            print(f"{error} * Unables to get os")
        
    except Exception as e:
        print(f"{error} * Error: {str(e)}")


def aboveBellow(compare, myList=None) -> None: # get's how many numbers in the list are above and bellow the compare
    # not needed or used
    if myList is None:
        myList = []
    
    above   = 0
    bellow  = 0
      
    for i in myList:
      if i < compare:
        bellow += 1

      elif i > compare:
        above += 1

      else:
        return ("this else statement should not reach here.\nIn theory\nif it does. sorry")

    # wanted to get fancy. un coment this for it to be written in a file
    # self.write(      
    #   {
    #     "above": above,
    #     "bellow": bellow
    #   }
    # )

    return json.dumps(
      {
        "above": above,
        "bellow": bellow
      }
    )


def rotateRight(data:str, rotateTimes:int) -> str: # rotate string char to the right rotateTimes times
    return data[-rotateTimes:] + data[:-rotateTimes]


def addStrings(string_A, string_B, defaultAdd='+') -> str: # adding 2 strings with defaultAdd separating the 2 strings and returning it
    return str(f"{string_A}{defaultAdd}{string_B}")


def split(str_A:str, defaultSplit='+') -> list[str]: # spliting a string and returning the list
    return str_A.split(defaultSplit)

#endregion


#region basic sorting and searching
def sort(arr=None) -> list: # returns sorted list or aka array
    if arr is None:
        arr = []

    return sorted(arr)


def search(Search, arr=None) -> bool: # returning true or false if Search is found in arr
    if arr is None:
        arr = []
        
    return Search in arr


def search(Search, In) -> bool: # returning true or false if Search is found in In
    return Search in In

#endregion


def valEmail(email) -> bool: # validating if the email is valid or not
    # validating email and more
    if not re.fullmatch(REGEX, email):
        return False
    else:
        return True