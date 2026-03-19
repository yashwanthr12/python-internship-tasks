import os

# Folder path
folder_path = input("Enter folder path: ")

files = os.listdir(folder_path)

count = 1

for file in files:
    old_path = os.path.join(folder_path, file)

    # Get file extension
    extension = os.path.splitext(file)[1]

    new_name = f"file_{count}{extension}"
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)

    count += 1

print("Files renamed successfully.")

#C:\Users\Admin\Desktop\files