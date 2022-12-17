#Command List
# view_cwd - will show all files in the directory where the file is running
#custom_dir - will show files from custom directory
#download_files - files will download files from directory

import os
import socket

s = socket.socket()
port = 8080
host = input("Please enter the server adress: ")
s.connect((host, port))
print("Connected to the server successfully")

# connection has been completed

# command receiving and execution

while True:
    command = s.recv(1024)
    command = command.decode()
    print("Command received")
    if command == "view_cwd":
        files = os.listdir()
        files = str(files)
        s.send(files.encode())
        print("Command has been executed successfully")

    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("Command has been executed successfully")

    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        with open(file_path, "rb") as file:
            data = file.read()
        s.send(data)
        print("File has been sent successfully")

    elif command == "remove_file":
        file_and_dir = s.recv(6000)  # Change when a file is bigger than 6000MB
        file_and_dir = file_and_dir.decode()
        os.remove(file_and_dir)
        print("Command has been executed successfully")

    elif command == "send_files":
        filename = s.recv(6000)
        filename = filename.decode()
        with open(filename, "wb") as new_file:
            data = s.recv(6000)
            new_file.write(data)
        print("File received successfully")

    else:
        print("Command not recognized")
