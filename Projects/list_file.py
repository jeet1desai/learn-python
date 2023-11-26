import os

folders = input("Please provide list of folders name with space in between: ")
folder_list = folders.split()

for folder in folder_list:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Please provide a valid folder name, looks like {folder} folder is not exist.")
        break
    except PermissionError:
        print(f"You don't have access to {folder} folder.")
        break

    print(f"{folder}:")

    for file in files:
        print(f"|_____ {file}")
        # print(f"\t {file}")
