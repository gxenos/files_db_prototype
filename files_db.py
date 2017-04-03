import os
import math
import hashlib
import argparse


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

    for root, dirnames, files in os.walk(args.path_to_scan):
        for file in files:

            info = os.stat(os.path.join(root, file))
            print("Name: ", file)  # Prints the name of the file, with its extension
            print("Size: ", convert_size(info.st_size))  # Prints the size of the file using convert_size()
            print("Path Relative to Scan Point:", os.path.relpath(root))  # Prints the path of the file relative to the scan point
            print("MD5 Hash: ", md5checksum(os.path.join(root, file)))  # Prints the md5checksum of the file using md5checksum()
            # Prints the basename and the extension of a file
            if "." in file:
                print("Basename: ", file.split(".")[0])
                print("Extension: ", ".".join(file.split(".")[1:]))  # If more than one '.' exist
            else:
                print("Basename: ", file)
                print("Extension: ", "No extension")  # If there are no '.' there is no extension

            print("Directory Name: ", os.path.split(root)[1])
            permissions = info.st_mode
            print("Read:", bool(permissions & 0o00400), "Write:", bool(permissions & 0o00200),"Execute:", bool(permissions & 0o00100))
            print("-------------------------")


if __name__ == "__main__":
    main()


