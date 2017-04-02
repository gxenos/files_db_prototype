import os
import math
import hashlib


# Function to return size from bytes
def convert_size(size_bytes):
    if size_bytes == 0:
        return '0B'
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    size_name_pointer = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, size_name_pointer)
    round_size = round(size_bytes/p, 2)
    return '%s %s' % (round_size, size_name[size_name_pointer])


def md5checksum(filepath):
    with open(filepath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


for root, dirnames, files in os.walk("C:/Users/George/Documents/test_folder"):
    for file in files:

        info = os.stat(os.path.join(root, file))
        print("Name: ", file)
        print("Size: ", convert_size(info.st_size))
        print("Path Relative to Scan Point:", os.path.relpath(root))
        print("MD5 Hash: ", md5checksum(os.path.join(root, file)))
        print("Path Relative to Scan Point:", os.path.relpath(root))
        print("Basename: ", file.split(".")[0])
        print("Extension: ", file.split(".")[1])
        print("Directory Name: ", os.path.split(root)[1])
        permissions = info.st_mode
        print("Read:", bool(permissions & 0o00400), "Write:", bool(permissions & 0o00200),"Execute:", bool(permissions & 0o00100))
        print("-------------------------")


