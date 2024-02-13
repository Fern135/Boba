import json
import subprocess
import sys
import string
import random
import os
import platform
import re
import sys
import time
import asyncio


CHARACTERS = string.ascii_uppercase + string.digits + \
    string.ascii_lowercase + string.punctuation + string.ascii_letters

OS_SUPPORTED = {
    "mac"     : "Darwin",
    "linux"   : "Linux",
    "windows" : "Windows"
}

#region useful utilities
def read_json_file(file_path:str, key:str):
    """
        Read a JSON file and retrieve the value associated with the given key.

        Parameters:
            file_path (str): The path to the JSON file.
            key (str): The key whose value is to be retrieved.

        Returns:
            any: The value associated with the given key in the JSON file.
                Returns None if the key is not found or there is an error reading the file.

        Raises:
            FileNotFoundError: If the specified file_path does not exist.
            json.JSONDecodeError: If the JSON file is not valid and cannot be decoded.

        Example:
            # JSON file contents: {"name": "John", "age": 30}
            value = read_json_file('data.json', 'name')
            print(value)  # Output: "John"
            
            value = read_json_file('data.json', 'occupation')
            print(value)  # Output: None (key not found in the JSON file)
    """
    try:
        with open(get_absolute_path(file_path), 'r') as file:
            data = json.load(file)

            if data is not None:
                return data.get(key, None)
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {file_path}")
        return None

def modify_json_value(file_path: str, key: str, new_value: any) -> None:
    """
        Modify a specific value in a JSON file and write the changes back to the file.

        Parameters:
            file_path (str): The path to the JSON file.
            key (str): The key of the value to be modified.
            new_value (any): The new value to replace the existing value associated with the key.

        Returns:
            None

        Raises:
            FileNotFoundError: If the specified file_path does not exist.
            json.JSONDecodeError: If the JSON file is not valid and cannot be decoded.

        Example:
            JSON file contents: {"name": "John", "age": 30}
            modify_json_value('data.json', 'name', 'Jane')
            After execution, the JSON file will be updated to: {"name": "Jane", "age": 30}
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Modify the specific value with the new_value
        data[key] = new_value

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {file_path}")
        return


def get_absolute_path(path:str):
    """
        This function gets the absolute path to a file or directory.

        Args:
            path: The path to the file or directory.

        Returns:
            The absolute path to the file or directory.
    """

    """Gets the absolute path to a file or directory."""

    # return the absolute path to the file or directory.
    return os.path.realpath(path)

def generate_random_alphanumeric_string(length: int) -> str:
    """
        Generate a random alphanumeric string of a specified length.

        Parameters:
            length (int): The length of the random alphanumeric string to be generated.

        Returns:
            str: A random alphanumeric string of the specified length.

        Example:
            random_string = generate_random_alphanumeric_string(10)
            print(random_string)  # Output: "AbCdEfGhIj"
    """
    random_string = ''.join(random.choice(CHARACTERS) for _ in range(length))
    return random_string

def is_valid_email(email: str) -> bool:
    """
    Check if the given email address is a valid email format.

    Parameters:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.

    Example:
        result = is_valid_email("john.doe@example.com")
        print(result)  # Output: True
    """
    # Regular expression pattern to match a valid email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use the re.match function to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    
    return False

def run_terminal_command(command:str) -> None:
    """
        Execute a terminal command on Windows or Unix-like systems.

        Parameters:
            command (str): The terminal command to be executed.

        Returns:
            None: This function does not return any value.
            
        Notes:
            - The function uses the `subprocess.run()` method to run the command in a
            new subprocess and wait for it to complete.
            - On Windows, the command is executed in the Command Prompt (cmd) using the '/C' flag.
            - On Unix-like systems (Linux, macOS, etc.), the command is executed in a shell ('sh').

        Example:
            run_terminal_command('echo Hello, World!')
            run_terminal_command('dir')  # For Windows
            run_terminal_command('ls -l')  # For Unix-like systems
    """
    try:
        system = platform.system().lower()
        if system == 'darwin' or system == 'linux':
            # On macOS or Linux
            subprocess.run(command, shell=True)

        elif system == 'windows':
            # On Windows
            subprocess.run(command, shell=True, text=True)

        else:
            print(f"Unsupported OS: {system}")
    except Exception as e:
        print(f"An error occurred: {e}")

# in case async is needed for this 
def run_terminal_command(command:str) -> None:
    """
        Execute a terminal command on Windows or Unix-like systems.

        Parameters:
            command (str): The terminal command to be executed.

        Returns:
            None: This function does not return any value.
            
        Notes:
            - The function uses the `subprocess.run()` method to run the command in a
            new subprocess and wait for it to complete.
            - On Windows, the command is executed in the Command Prompt (cmd) using the '/C' flag.
            - On Unix-like systems (Linux, macOS, etc.), the command is executed in a shell ('sh').

        Example:
            run_terminal_command('echo Hello, World!')
            run_terminal_command('dir')  # For Windows
            run_terminal_command('ls -l')  # For Unix-like systems
    """
    try:
        system = platform.system().lower()
        if system == 'darwin' or system == 'linux':
            # On macOS or Linux
            subprocess.run(command, shell=True)

        elif system == 'windows':
            # On Windows
            subprocess.run(command, shell=True, text=True)

        else:
            print(f"Unsupported OS: {system}")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_and_write_to_file(folder_path: str, file_name: str, data: str) -> None:
    """
        Create a file and write data to a specific folder path.

        Parameters:
            folder_path (str): The path of the folder where the file will be created.
            file_name (str): The name of the file to be created.
            data (str): The data to be written to the file.

        Returns:
            None

        Raises:
            OSError: If there's an error while creating or writing to the file.

        Example:
            create_and_write_to_file("C:/MyDocuments", "example.txt", "Hello, world!")
    """
    try:
        # Check if the folder path exists, create it if it doesn't
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Combine the folder path and file name to create the full file path
        file_path = os.path.join(folder_path, file_name)

        # Open the file in write mode and write the data to it
        with open(file_path, "w") as file:
            file.write(data)

    except OSError as e:
        # Handle any errors that occur during file creation or writing
        raise OSError(f"Error creating or writing to the file: {e}")


def make_dir(dir:str) -> None:
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        print(f"Directory '{dir}' already exists and was not created.")


# for some reason this was giving a problem
# def make_dir(dir:str) -> None: 
#     if not os.path.exists(dir):
#         os.makedirs(dir)

#     else:
#         print(f"Directory '{dir}' already exists and was not created.")


#endregion

#region basic utilities
def rnd(max: int) -> int:
    """
    Generate a random integer between 1 and the given maximum (inclusive).

    Parameters:
        max (int): The upper limit for the random number (inclusive).

    Returns:
        int: A random integer between 1 and max (inclusive).

    Example:
        random_number = rnd(10)
        print(random_number)  # Output: Random integer between 1 and 10 (inclusive)
    """

    return random.randint(1, max)


def rnd(min: int, max: int) -> int:
    """
    Generate a random integer between the given minimum and maximum (inclusive).

    Parameters:
        min (int): The lower limit for the random number (inclusive).
        max (int): The upper limit for the random number (inclusive).

    Returns:
        int: A random integer between min and max (inclusive).

    Example:
        random_number = rnd(5, 15)
        print(random_number)  # Output: Random integer between 5 and 15 (inclusive)
    """ 
    return random.randint(min, max)


def evenRnd(min: int, max: int, step=2) -> int:
    """
    Generate a random even integer between the given minimum and maximum (inclusive).

    Parameters:
        min (int): The lower limit for the random number (inclusive).
        max (int): The upper limit for the random number (inclusive).
        step (int, optional): The step size for generating even numbers. Default is 2.

    Returns:
        int: A random even integer between min and max (inclusive).

    Example:
        random_even_number = evenRnd(2, 10)
        print(random_even_number)  # Output: Random even integer between 2 and 10 (inclusive)
    """ 
    return random.randrange(min, max + 1, step)


def oddRnd(min: int, max: int, step=2) -> int:
    """
    Generate a random odd integer between the given minimum and maximum (inclusive).

    Parameters:
        min (int): The lower limit for the random number (inclusive).
        max (int): The upper limit for the random number (inclusive).
        step (int, optional): The step size for generating odd numbers. Default is 2.

    Returns:
        int: A random odd integer between min and max (inclusive).

    Example:
        random_odd_number = oddRnd(1, 9)
        print(random_odd_number)  # Output: Random odd integer between 1 and 9 (inclusive)
    """ 
    return random.randrange(min + 1 if min % 2 == 0 else min, max + 1, step)


def isDict(data) -> bool:
    """
    Check if the given data is of type dict.

    Parameters:
        data: The data to be checked.

    Returns:
        bool: True if the data is of type dict, False otherwise.

    Example:
        result = isDict({'name': 'John', 'age': 30})
        print(result)  # Output: True
    """
    return type(data) is dict


def isString(data) -> bool:
    """
    Check if the given data is of type string.

    Parameters:
        data: The data to be checked.

    Returns:
        bool: True if the data is of type string, False otherwise.

    Example:
        result = isString("Hello, World!")
        print(result)  # Output: True
    """
    return type(data) is str


def isInt(data) -> bool:
    """
    Check if the given data is of type int.

    Parameters:
        data: The data to be checked.

    Returns:
        bool: True if the data is of type int, False otherwise.

    Example:
        result = isInt(42)
        print(result)  # Output: True
    """
    return type(data) is int


def isFloat(data) -> bool:
    """
    Check if the given data is of type float.

    Parameters:
        data: The data to be checked.

    Returns:
        bool: True if the data is of type float, False otherwise.

    Example:
        result = isFloat(3.14)
        print(result)  # Output: True
    """
    return type(data) is float


def toInt(data) -> int:
    """
    Convert the given data to an integer.

    Parameters:
        data: The data to be converted.

    Returns:
        int: The integer representation of the data.

    Example:
        result = toInt("42")
        print(result)  # Output: 42
    """
    return int(data)


def toFloat(data) -> float:
    """
    Convert the given data to a float.

    Parameters:
        data: The data to be converted.

    Returns:
        float: The float representation of the data.

    Example:
        result = toFloat("3.14")
        print(result)  # Output: 3.14
    """
    return float(data)


def toString(data) -> str:
    """
    Convert the given data to a string.

    Parameters:
        data: The data to be converted.

    Returns:
        str: The string representation of the data.

    Example:
        result = toString(42)
        print(result)  # Output: "42"
    """
    return str(data)


def toUpper(data: str) -> str:
    """
    Convert the given string to upper case.

    Parameters:
        data (str): The string to be converted.

    Returns:
        str: The string converted to upper case.

    Example:
        result = toUpper("hello")
        print(result)  # Output: "HELLO"
    """
    return data.upper()


def toLower(data: str) -> str:
    """
    Convert the given string to lower case.

    Parameters:
        data (str): The string to be converted.

    Returns:
        str: The string converted to lower case.

    Example:
        result = toLower("Hello")
        print(result)  # Output: "hello"
    """
    return data.lower()


def isLower(data: str) -> bool:
    """
    Check if the given string is in lower case.

    Parameters:
        data (str): The string to be checked.

    Returns:
        bool: True if the string is in lower case, False otherwise.

    Example:
        result = isLower("hello")
        print(result)  # Output: True
    """
    return data.islower()


def isUpper(data: str) -> bool:
    """
    Check if the given string is in upper case.

    Parameters:
        data (str): The string to be checked.

    Returns:
        bool: True if the string is in upper case, False otherwise.

    Example:
        result = isUpper("HELLO")
        print(result)  # Output: True
    """
    return data.isupper()


def cls() -> None:
    """
        Clear the console screen.

        Returns:
            None

        Note:
            This function works for both Windows and Unix-like systems (Linux, macOS).

        Example:
            cls()  # Clears the console screen
    """
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for macOS and Linux (here, os.name is 'posix')
    # else:
    _ = os.system('clear')

#endregion


def getPcDevOs() -> str:
    """
    Get the name of the operating system that the Python script is running on.

    Returns:
        str: The name of the operating system (e.g., "Windows", "Linux", "Darwin").

    Example:
        os_name = getPcDevOs()
        print(f"This script is running on {os_name}.")
    """
    return platform.system()


def delFile(title: str) -> None:
    """
    Delete a specific file with the given title.

    Parameters:
        title (str): The name of the file to be deleted.

    Returns:
        None

    Example:
        delFile("example.txt")
    """
    if os.path.exists(title):
        os.remove(title)
    else:
        print(f"The file {title} does not exist.")


def sort(arr=None) -> list:
    """
    Sort the elements in the given list (array) in ascending order.

    Parameters:
        arr (list, optional): The list to be sorted. Default is an empty list.

    Returns:
        list: A new list with elements sorted in ascending order.

    Example:
        sorted_list = sort([3, 1, 4, 2])
        print(sorted_list)  # Output: [1, 2, 3, 4]
    """
    if arr is None:
        arr = []
    return sorted(arr)


def search(Search, arr=None) -> bool:
    """
    Check if the given value (Search) is present in the list (arr).

    Parameters:
        Search: The value to be searched in the list.
        arr (list, optional): The list to be searched. Default is an empty list.

    Returns:
        bool: True if the value is found in the list, False otherwise.

    Example:
        result = search(3, [1, 2, 3, 4])
        print(result)  # Output: True
    """
    if arr is None:
        arr = []
    return Search in arr


def search(Search, In) -> bool:
    """
    Check if the given value (Search) is present in the iterable (In).

    Parameters:
        Search: The value to be searched in the iterable.
        In (iterable): The iterable to be searched.

    Returns:
        bool: True if the value is found in the iterable, False otherwise.

    Example:
        result = search("apple", ["orange", "banana", "apple"])
        print(result)  # Output: True
    """
    return Search in In

async def simple_loader(iterations, delay=0.1):
    for _ in range(iterations):
        sys.stdout.write('\rLoading |')
        sys.stdout.flush()
        time.sleep(delay)

        sys.stdout.write('\rLoading /')
        sys.stdout.flush()
        time.sleep(delay)

        sys.stdout.write('\rLoading -')
        sys.stdout.flush()
        time.sleep(delay)

        sys.stdout.write('\rLoading \\')
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write('\r')
    sys.stdout.flush()

#region installation
def is_homebrew_installed():
    try:
        subprocess.check_output(["brew", "--version"])
        return True
    except subprocess.CalledProcessError:
        return False


async def install_homebrew():
    try:
        system = platform.system().lower()
        if system == 'darwin':
            # macOS
            subprocess.run('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"', shell=True)

        elif system == 'linux':
            # Linux
            subprocess.run('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"', shell=True)

        else:
            print(f"Unsupported OS: {system}")

            return

        print("Homebrew is installed.")

    except Exception as e:
        print(f"An error occurred: {e}")


def is_mongodb_installed(install_path):
    mongodb_binaries = ['mongod', 'mongo']  # List of MongoDB executable files
    for binary in mongodb_binaries:
        binary_path = os.path.join(install_path, 'bin', binary)
        if not os.path.exists(binary_path):
            return False
    return True


async def install_latest_mongodb(install_path):
    # Check if MongoDB is installed using Homebrew
    installed = False
    try:
        result = subprocess.run(['brew', 'ls', '--versions', 'mongodb'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "mongodb" in result.stdout:
            installed = True
    except Exception as e:
        print(f"An error occurred while checking for MongoDB: {e}")

    if not installed:
        try:
            # Install the latest version of MongoDB using Homebrew to the specified install_path
            install_command = f'brew install mongodb --prefix={install_path}'
            subprocess.run(install_command, shell=True)
            print(f"MongoDB is installed in {install_path}.")
        except Exception as e:
            print(f"An error occurred while installing MongoDB: {e}")
    else:
        print("MongoDB is already installed.")


def is_mysql_installed(install_path):
    #* the installation of mysql is done in the main run.py
    mysql_binaries = ['mysql', 'mysqld', 'mysqladmin']  # List of MySQL executable files
    for binary in mysql_binaries:
        binary_path = os.path.join(install_path, 'bin', binary)
        if not os.path.exists(binary_path):
            return False
    return True


def is_choco_installed_win():
    # Check if Chocolatey executable exists in the PATH
    for directory in os.environ['PATH'].split(os.pathsep):
        chocolatey_executable = os.path.join(directory, 'chocolatey.exe')
        if os.path.exists(chocolatey_executable):
            return True
    return False


async def install_choco_win():
    # Check if Chocolatey is already installed
    if platform.system().lower() == "windows":
        try:
            result = subprocess.run(['choco', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if "Chocolatey" in result.stdout:
                print("Chocolatey is already installed.")
                return
        except FileNotFoundError:
            pass  # Chocolatey is not found, proceed with the installation

    # Download and install Chocolatey
    try:
        powershell_script = '''
        Set-ExecutionPolicy Bypass -Scope Process -Force;
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
        iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'));
        '''
        subprocess.run(['powershell', '-Command', powershell_script], shell=True)
        print("Chocolatey is installed.")
    except Exception as e:
        print(f"An error occurred while installing Chocolatey: {e}")


def is_mysql_installed_win(install_path):
    mysql_binaries = ['mysql', 'mysqldump']  # List of MySQL executable files
    for binary in mysql_binaries:
        binary_path = os.path.join(install_path, 'bin', binary)
        if not os.path.exists(binary_path):
            return False
    return True


async def install_mysql_win():
    try:
        # Check if MySQL is already installed
        result = subprocess.run(['choco', 'list', '--local-only', 'mysql'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "mysql" in result.stdout:
            print("MySQL is already installed.")
            return

        # Install MySQL using Chocolatey
        subprocess.run(['choco', 'install', 'mysql', '--yes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("MySQL is installed using Chocolatey.")
    except Exception as e:
        print(f"An error occurred while installing MySQL for windows: {e}")



def is_mongo_installed_win(install_path):
    mongodb_binaries = ['mongod', 'mongo']  # List of MongoDB executable files
    for binary in mongodb_binaries:
        binary_path = os.path.join(install_path, 'bin', binary)
        if not os.path.exists(binary_path):
            return False
    return True


async def install_mongo_win(install_path):
    try:
        # Check if MongoDB is already installed
        result = subprocess.run(['choco', 'list', '--local-only', 'mongodb'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "mongodb" in result.stdout:
            print("MongoDB is already installed.")
            return

        # Install MongoDB using Chocolatey with the specified install path
        install_command = f'choco install mongodb --yes --params "installdir={install_path}"'
        subprocess.run(install_command, shell=True)
        print(f"MongoDB is installed in {install_path}.")
    except Exception as e:
        print(f"An error occurred while installing MongoDB: {e}")

#endregion
