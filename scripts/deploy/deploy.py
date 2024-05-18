# todo: run deploy script here. 

import os

def delete_file(filepath):
  try:
    os.remove(filepath)
    return True
  except FileNotFoundError:
    return False


API_SET_UP_DIR = "../../Boba/api/st.txt"
deleted = delete_file(API_SET_UP_DIR)

if deleted:
    print("File deleted successfully!")
else:
    print("File not found.")
