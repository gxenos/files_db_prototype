# files_db_prototype
Quick Implementation of Files DB GFOSS Project

Prints metadata about all the files of the specified directory. 
#### Usage
-h Prints Help

path_to_scan The path you wish to scan

_Example files_db.py C:\Users\User\folder_to_scan


Stores the following information for each file in an SQLite DB single file and then prints them:
* Name
* Size
* Path Relative to Scan Point
* MD5sum
* Basename
* Extension
* Permissions

Things to add the following days:
1. ~~ArgParse to take the folder to scan as an argument~~
2. ~~SQLiteIntegration~~
3. Argument for choosing db file name.
