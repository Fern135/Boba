import random
import string

CHARACTERS = string.ascii_uppercase + string.digits + \
    string.ascii_lowercase + string.punctuation + string.ascii_letters

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
    return ''.join(random.choice(CHARACTERS) for _ in range(length))

def write_env_file():
    env_data = {
        "secret_key": generate_random_alphanumeric_string(random.randint(1, 250)) + "\n",
        "db_user_name": "",
        "db_password": "",
        "db_ip": "",
        "db_name": "",
        "debugging": "True"
    }

    file_path = "../../.env"
    with open(file_path, "w") as env_file:
        for key, value in env_data.items():
            env_file.write(f"{key}={value}\n")

    print(f".env file written successfully at {file_path}")

if __name__ == "__main__":
    write_env_file()