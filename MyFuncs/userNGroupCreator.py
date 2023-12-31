#!/usr/bin/python3
import os

def create_users(userlist):
    """
    Checks if users exist using the 'id' command and adds them if they don't exist.

    :param userlist: List of user names to check and possibly create.
    :type userlist: list
    """
    try:
        for user in userlist:
            print(user)
            exitcode = os.system(f"id {user}")
            if exitcode != 0:
                try:
                    print(f"User [{user}] does not exist. Creating it")
                    os.system(f"sudo useradd {user}")
                except Exception as e:
                    print(f"Error creating user [{user}]: {e}")
            else:
                print(f"User [{user}] already exists, skipping it.")
    except Exception as e:
        print(f"An error occurred: [{e}]")

def create_group(groupname):
    """
    Checks if a group exists in /etc/group. If not, adds the group.

    :param groupname: The name of the group to check and possibly create.
    :type groupname: str
    """
    try:
        exitcode = os.system(f"grep {groupname} /etc/group")
        if exitcode != 0:
            try:
                print(f"Group [{groupname}] does not exist. Creating it.")
                os.system(f"sudo groupadd {groupname}")
            except Exception as e:
                print(f"Error creating group [{groupname}]: {e}")
        else:
            print("Group [{groupname}] already exists, skipping it.")
    except Exception as e:
        print(f"An error occurred: [{e}]")

def add_users_group(userlist, groupname):
    """
    Adds multiple users to a group and checks if users are already in the group.

    :param userlist: List of user names to be added to the group.
    :type userlist: list
    :param groupname: Group name to which the users will be added.
    :type groupname: str
    """
    try:
        for user in userlist:
            exitcode = os.system(f"id {user} | grep -q '{groupname}'")
            if exitcode != 0:
                try:
                    print(f"Adding user [{user}] to the group [{groupname}].")
                    os.system(f"usermod -G {groupname} {user}")
                except Exception as e:
                    print(f"Error adding [{user}] user to [{groupname}] group: {e}")
            else:
                print(f"User [{user}] is already in the group [{groupname}].")
    except Exception as e:
        print(f"An error occurred: [{e}]")

# Example usage
users_to_check = ["user1", "user2", "user3"]
group_name = "ops"

create_users(users_to_check)
create_group(group_name)
add_users_group(users_to_check, group_name)
