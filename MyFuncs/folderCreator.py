#!/usr/bin/python3
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
        
def permission_owner(folder_path, owner, permission):
    """
    Changes ownership and permissions of a folder.

    :param folder_path: The path to the folder to modify.
    :type folder_path: str
    :param owner: The new owner of the folder.
    :type owner: str
    :param permission: The new permission to set on the folder.
    :type permission: str
    """
    try:
        if os.path.exists(folder_path):
            os.system(f"chown :{owner} {folder_path}")
            os.system(f"chmod {permission} {folder_path}")
            print(f"SUCCESS! Permission and owner updated for folder: [{folder_path}]")
        else:
            print(f"ERROR! Folder [{folder_path}] does not exist.")
    except Exception as e:
        print(f"ERROR! An unexpected error occurred: [{e}]")
        
# Example
folder_path = "/home/ubuntu/opt/apple/red"
new_owner = "user1"
new_permission = "770"
new_folder(folder_path)
permission_owner(folder_path, new_owner, new_permission)
