import os

def check_and_create_users(userlist):
    """
    Checks if users exist using the 'id' command and adds them if they don't exist.

    :param userlist: List of user names to check and possibly create.
    :type userlist: list
    """
    try:
        for user in userlist:
            print(user)
            exitcode = os.system("id {}".format(user))
            if exitcode != 0:
                try:
                    print("User [{}] does not exist. Adding it".format(user))
                    os.system("sudo useradd {}".format(user))
                except Exception as e:
                    print(f"Error adding user [{user}]: {e}")
            else:
                print("User [{}] already exists, skipping it.".format(user))
    except Exception as e:
        print(f"An error occurred: {e}")

def create_group(groupname):
    """
    Checks if a group exists in /etc/group. If not, adds the group.

    :param groupname: The name of the group to check and possibly create.
    :type groupname: str
    """
    try:
        exitcode = os.system(f"grep {groupname} /etc/group")
        if exitcode != 0:
            print(f"Group [{groupname}] does not exist. Adding it.")
            os.system(f"sudo groupadd {groupname}")
        else:
            print("Group already exists, skipping it.")
    except Exception as e:
        print(f"An error occurred: {e}")



# Example usage

users_to_check = ["user1", "user2", "user3"]
check_and_create_users(users_to_check)

group_name = "ops"
check_and_create_group(group_name)
