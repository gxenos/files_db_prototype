import os
import math
import hashlib
import argparse
import sqlite3


# Function to return size from bytes, transformed into KB,MB,etc
def convert_size(size_bytes):
    if size_bytes == 0:
        return '0B'
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    size_name_pointer = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, size_name_pointer)
    round_size = round(size_bytes/p, 2)
    return '%s %s' % (round_size, size_name[size_name_pointer])


# Returns the md5checksum of a file, reading 8KB each time, for memory saving
def md5checksum(filepath):
    with open(filepath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_scan", help="The path you wish to scan.")
    args = parser.parse_args()

    conn = sqlite3.connect('files.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS file(
      FILE_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      NAME TEXT NOT NULL,
      SIZE TEXT NOT NULL,
      PATH TEXT NOT NULL,
      MD5 CHAR(32),
      BASENAME TEXT NOT NULL,
      EXTENSION TEXT,
      DIRECTORY TEXT,
      READ BOOLEAN,
      WRITE BOOLEAN,
      EXECUTE BOOLEAN
    );''')

    for root, dirnames, files in os.walk(args.path_to_scan):
        for file in files:

            info = os.stat(os.path.join(root, file))
            permissions = info.st_mode


            name = file;
            size = convert_size(info.st_size)
            path = os.path.relpath(root)
            md5 = md5checksum(os.path.join(root, file))
            if "." in file:
                basename = file.split(".")[0]
                extension = ".".join(file.split(".")[1:])
            else:
                basename = file
                extension = ""
            directory = os.path.split(root)[1]
            read = 1 if bool(permissions & 0o00400) == True else 0
            write = 1 if bool(permissions & 0o00200) == True else 0
            execute = 1 if bool(permissions & 0o00100) == True else 0

            cursor.execute(
                '''INSERT INTO file(NAME,SIZE, PATH,MD5,BASENAME,EXTENSION,DIRECTORY,READ,WRITE,EXECUTE) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',(name, size, path, md5,basename, extension, directory, read, write, execute)
            )

            cursor.execute('''SELECT * FROM file''')

            for row in cursor:
                print("File ID: ", row[0])
                print("Name:: ", row[1])
                print("Size: ", row[2])
                print("Path Relative to Scan Point: ", row[3])
                print("MD5 Hash: ", row[4])
                print("Basename ", row[5])
                print("Extension: ", row[6])
                print("Directory Name: ", row[7])
                print("Read:  ", True if row[8] == 1 else False)
                print("Write:  ", True if row[9] == 1 else False)
                print("Execute:  ", True if row[10] == 1 else False)
                print("----------------------")

            conn.commit()

if __name__ == "__main__":
    main()


