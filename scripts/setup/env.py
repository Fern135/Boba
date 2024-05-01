import random
import string

CHARACTERS = string.ascii_uppercase + string.digits + \
    string.ascii_lowercase + string.punctuation + string.ascii_letters

if __name__ == "__main__":
    env_data = {
        "secret_key": ''.join(random.choice(CHARACTERS) for _ in range(random.randint(1, 250))) + "\n",
        "db_user_name": "",
        "db_password": "",
        "db_ip": "",
        "db_name": ""+ "\n",
        "debugging": "True"
    }

    file_path = "../../.env"
    with open(file_path, "w") as env_file:
        for key, value in env_data.items():
            env_file.write(f"{key}={value}\n")

    print(f".env file written successfully at {file_path}")

    