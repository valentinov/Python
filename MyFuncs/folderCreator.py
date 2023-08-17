import os

def new_folder(folder_path):
    """
    Creates a new folder at the specified path if it doesn't already exist.

    :param folder_path: The path to the folder to be created.
    :type folder_path: str
    """
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"SUCCESS! Folder created: [{folder_path}]")
        else:
            print(f"WARNING! Folder already exists: [{folder_path}]")
    except Exception as e:
        print(f"ERROR! Failed to create [{folder_path}] folder. Exception: [{e}]")

# Example
new_folder("C:\\MyFolder\xyfolder")
