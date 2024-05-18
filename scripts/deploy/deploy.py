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


async def download_file(url, filepath):
  """Downloads a file asynchronously from the given URL to the specified filepath."""
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      if response.status == 200:
        data = await response.read()
        async with open(filepath, 'wb') as f:
          await f.write(data)
      else:
        print(f"Error downloading {url} (Status: {response.status})")

async def download_repo(repo_url, directory):
  """Downloads a Git repository asynchronously to the specified directory."""
  # Use a temporary directory for cloning
  temp_dir = os.path.join(directory, ".tmp_clone")
  os.makedirs(temp_dir, exist_ok=True)

  # Clone the repository using a series of asynchronous downloads
  async with aiohttp.ClientSession() as session:
    async def download_object(url, local_path):
      async with session.get(url) as response:
        if response.status == 200:
          data = await response.read()
          async with open(local_path, 'wb') as f:
            await f.write(data)
        else:
          print(f"Error downloading object from {url} (Status: {response.status})")

    # Get the content of the "objects" folder
    objects_url = f"{repo_url}/objects"
    async with session.get(objects_url) as response:
      if response.status == 200:
        objects_html = await response.text()
        for obj_ref in objects_html.splitlines():
          obj_url = f"{objects_url}/{obj_ref}"
          obj_path = os.path.join(temp_dir, "objects", obj_ref)
          await download_object(obj_url, obj_path)
      else:
        print(f"Error getting objects list (Status: {response.status})")

    # Download additional files (like HEAD and refs)
    tasks = []
    for filename in ["HEAD", "refs"]:
      url = f"{repo_url}/{filename}"
      local_path = os.path.join(temp_dir, filename)
      tasks.append(download_object(url, local_path))
    await asyncio.gather(*tasks)

  # Download individual files (if needed)
  for root, _, files in os.walk(temp_dir):
    for filename in files:
      if filename in files_to_replace:  # Replace with your list of files to replace
        file_path = os.path.join(root, filename)
        url = f"{repo_url}/raw/master/{filename}"  # Adjust URL structure as needed
        await download_file(url, os.path.join(directory, filename))

  # Move downloaded files and remove temporary directory
  shutil.move(os.path.join(temp_dir, "*"), directory)
  shutil.rmtree(temp_dir)

async def replace_files(directory, replace):
    """Replaces specific files in the directory with provided content."""
    for filename, content in replace.items():  # Replace with your file replacements
        filepath = os.path.join(directory, filename)
        async with open(filepath, 'w') as f:
            await f.write(content)

async def main():
    # Replace with your desired values
    repo_url = "https://github.com/Fern135/Boba-landing-page.git"
    directory = "your_download_directory"
    files_to_replace = ["file1.txt", "file2.py"]  # List of files to download from repo
    replacements = {"file3.txt": "This is the new content for file3.txt"}  # Dictionary of replacements

    await download_repo(repo_url, directory)
    await replace_files(directory, replacements)

    print("Download and replacement completed!")



if __name__ == "__main__":
    asyncio.run(main())