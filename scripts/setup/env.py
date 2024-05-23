import random
import string
import os

CHARACTERS = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation

def generate_random_alphanumeric_string(length: int):
    # print("Generating random string")
    result = ''.join(random.choice(CHARACTERS) for _ in range(length))
    # print("Random string generated")
    return result

def write_env_file():
    # print("Entering write_env_file function")
    env_data = f"""secret_key={generate_random_alphanumeric_string(255)}
db_user_name=
db_password=
db_ip=localhost
db_name=Boba
debugging=true
"""

    # Use the absolute path to ensure the file is written in the correct location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, ".env")

    # print(f"Attempting to write to {file_path}")

    try:
        with open(file_path, "w") as env_file:
            env_file.write(env_data)
            print("Data written to file successfully")

    except Exception as e:
        print(f"Error: {str(e)}")
        return  # Exit the function if an error occurs

    # print(f".env file written successfully at {file_path}")

if __name__ == "__main__":
    write_env_file()
