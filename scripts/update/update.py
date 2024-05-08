import json 
import platform
import asyncio
import os

CONF_DIR = "../../bin/conf/conf.json"
conf_data = json.loads(CONF_DIR)
language_used = ["go", "php", "python", "node", "npm"]

def getOs():
    if platform.system() == "Linux":
        return "Linux"
    elif platform.system() == "Darwin":
        return "Mac"
    elif platform.system() == "Windows":
        return "Windows"
    else:
        print("Unknown operating system")



def main():
    pass


if __name__ == "__main__":
    main()