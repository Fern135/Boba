# todo: run deploy script here. 
import asyncio
import aiohttp
import os
import shutil
from urllib.request import urlretrieve

def delete_file(filepath):
  try:
    os.remove(filepath)
    return True
  except FileNotFoundError:
    return False


def delete_api_tmp():
    API_SET_UP_DIR = "../../Boba/api/st.txt"
    deleted = delete_file(API_SET_UP_DIR)

    if deleted:
        print("File deleted successfully!")
    else:
        print("File not found.")


async def main():
    """
        todo: 
            1 download repo
            2 replace anchor where the download is with the new .exe or for mac or linux
            2.5 be sure it's using git and it's pushing to the correct one. 
            3 git add . -> git commit -m "update Boba.exe" -> git push origin
            4. print("New version successfully deployed")
    """
    await delete_api_tmp()
    repo_url = "https://github.com/Fern135/Boba-landing-page.git"
    directory = "your_download_directory"
    files_to_replace = ["file1.txt", "file2.py"]  # List of files to download from repo
    replacements = {"file3.txt": "This is the new content for file3.txt"}  # Dictionary of replacements




if __name__ == "__main__":
    asyncio.run(main())