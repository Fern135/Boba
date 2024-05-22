import random
import string

CHARACTERS = string.ascii_uppercase + string.digits + \
    string.ascii_lowercase + string.punctuation + string.ascii_letters

def generate_random_alphanumeric_string(length: int):
    return ''.join(random.choice(CHARACTERS) for _ in range(length))

def write_env_file():
    # todo: debug why this keeps running in the terminal. 
    # env_data = {
    #     "secret_key": generate_random_alphanumeric_string(random.randint(1, 250)) + "\n",
    #     "db_user_name": "",
    #     "db_password": "",
    #     "db_ip": "",
    #     "db_name": "",
    #     "debugging": "True"
    # }

    env_data = f"""
        secret_key={generate_random_alphanumeric_string(255)}\n\n
        db_user_name=\n
        db_password=\n
        db_ip=localhost\n
        db_name=Boba\n
        debugging=true\n
    """

    file_path = "../../.env"
    with open(file_path, "w") as env_file:
        # for key, value in env_data.items():
        env_file.write(env_data)

    env_file.close()
    print(f".env file written successfully at {file_path}")

if __name__ == "__main__":
    write_env_file()