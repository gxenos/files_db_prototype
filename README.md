# files_db_prototype
Quick Implementation of Files DB GFOSS Project
Prints metadata about all the files of the specified directory. Set Path_To_Directory_To_Scan to the directory you wish to scan (Use only '/', even on Windows).


Prints the following information for each file:
* Name
* Size
* Path Relative to Scan Point
* MD5sum
* Basename
* Extension
* Permissions

Things to add the following days:
1. ArgParse to take the folder to scan as an argument
2. SQLiteIntegration
