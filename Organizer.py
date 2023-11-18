import os
import shutil

path = input("Enter Path: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    destination_folder = os.path.join(path, extension)

    if os.path.exists(destination_folder):
        destination_path = os.path.join(destination_folder, file)
        if not os.path.exists(destination_path):
            shutil.move(os.path.join(path, file), destination_path)
        else:
            print(f"File '{file}' already exists in the destination folder.")
    else:
        os.makedirs(destination_folder)
        shutil.move(os.path.join(path, file), os.path.join(destination_folder, file))
