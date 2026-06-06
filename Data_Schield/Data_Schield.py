
#----------------------------------------------------------------------------------------
# Project Name : Marvellous Data Shield
# Description  : Automatic Incremental Backup and Archiving System
# Features     :
#               1. Periodic backup scheduling
#               2. Incremental backup using MD5 hashing
#               3. Automatic ZIP archive creation
#               4. Preservation of file metadata
# Author       : Rekha ShankarLal Kumawat
# Date         : 07/02/2026
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Required Modules
#----------------------------------------------------------------------------------------

import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

#----------------------------------------------------------------------------------------
#
# Function Name : make_zip()
# Description   : Creates a compressed ZIP archive of the backup folder.
# Input         : folder - Name of the folder to be archived.
# Output        : Returns the generated ZIP file name.
# Author        : Rekha ShankarLal Kumawat
# Date          : 07/02/2026
#
#----------------------------------------------------------------------------------------

def make_zip(folder):

    # Generate timestamp for unique ZIP file name
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    # Create ZIP file name using folder name and timestamp
    zip_name = folder + "_" + timestamp + ".zip"

    # Open ZIP file in write mode with compression enabled
    zobj = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    # Traverse all files and subfolders inside backup folder
    for root, dirs, files in os.walk(folder):
        for file in files:

            # Get complete path of current file
            full_path = os.path.join(root, file)

            # Calculate relative path to maintain folder structure
            relative = os.path.relpath(full_path, folder)

            # Add file to ZIP archive
            zobj.write(full_path, relative)

    # Close ZIP archive
    zobj.close()

    # Return generated ZIP file name
    return zip_name

#----------------------------------------------------------------------------------------
#
# Function Name : calculate_hash()
# Description   : Calculates MD5 hash value of a file for comparison.
# Input         : path - Full path of the file.
# Output        : Returns MD5 hash string.
# Author        : Rekha ShankarLal Kumawat
# Date          : 07/02/2026
#
#----------------------------------------------------------------------------------------

def calculate_hash(path):

    # Create MD5 hash object
    hobj = hashlib.md5()

    # Open file in binary mode
    fobj = open(path, "rb")

    # Read file in chunks
    while True:
        data = fobj.read(1024)

        # Stop if end of file is reached
        if not data:
            break
        else:
            # Update hash object with current chunk
            hobj.update(data)

    # Close file
    fobj.close()

    # Return generated hash value
    return hobj.hexdigest()

#----------------------------------------------------------------------------------------
#
# Function Name : BackupFiles()
# Description   : Performs incremental backup by copying only new or
#                 modified files from source to destination directory.
# Input         : Source      - Source directory path.
#                 Destination - Backup directory path.
# Output        : Returns list of copied files.
# Author        : Rekha ShankarLal Kumawat
# Date          : 07/02/2026
#
#----------------------------------------------------------------------------------------

def BackupFiles(Source, Destination):

    # Store names of copied files
    copied_files = []

    print("Creating the Backup folder for backup process")

    # Create backup directory if it does not exist
    os.makedirs(Destination, exist_ok=True)

    # Traverse source directory recursively
    for root, dirs, files in os.walk(Source):
        for file in files:

            # Complete path of source file
            src_path = os.path.join(root, file)

            # Relative path from source folder
            relative = os.path.relpath(src_path, Source)

            # Destination path inside backup folder
            dest_path = os.path.join(Destination, relative)

            # Create required subdirectories
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy file if it is new or modified
            if ((not os.path.exists(dest_path)) or
                (calculate_hash(src_path) != calculate_hash(dest_path))):

                # Copy file along with metadata
                shutil.copy2(src_path, dest_path)

                # Store copied file name
                copied_files.append(relative)

    # Return copied file list
    return copied_files

#----------------------------------------------------------------------------------------
#
# Function Name : MarvellousDataShieldStart()
# Description   : Initiates backup process, performs incremental backup,
#                 and creates ZIP archive of backup folder.
# Input         : Source - Source directory name (Default: Data)
# Output        : Displays backup status and archive information.
# Author        : Rekha ShankarLal Kumawat
# Date          : 07/02/2026
#
#----------------------------------------------------------------------------------------

def MarvellousDataShieldStart(Source="Data"):

    Border = "-" * 50

    # Name of backup directory
    BackupName = "MarvellousBackup"

    print(Border)
    print("Backup Process Started Successfully at :", time.ctime())
    print(Border)

    # Perform incremental backup
    files = BackupFiles(Source, BackupName)

    # Create ZIP archive of backup folder
    zip_file = make_zip(BackupName)

    print(Border)
    print("Backup Completed Successfully")
    print("Files Copied :", len(files))
    print("ZIP File Created :", zip_file)
    print(Border)

#----------------------------------------------------------------------------------------
#
# Function Name : main()
# Description   : Entry point of the application. Handles command line
#                 arguments, displays help/usage information, and starts
#                 scheduled backup execution.
# Input         : Command line arguments.
# Output        : Executes backup scheduling and displays status messages.
# Author        : Rekha ShankarLal Kumawat
# Date          : 07/02/2026
#
#----------------------------------------------------------------------------------------

def main():

    Border = "-" * 50

    print(Border)
    print("--------- Marvellous Data Shield System ----------")
    print(Border)

    # Check number of command line arguments
    if(len(sys.argv) == 2):

        # Display help information
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This script is used to :")
            print("1 : Take automatic backup at specified intervals")
            print("2 : Backup only new and modified files")
            print("3 : Create ZIP archive of backup periodically")

        # Display usage information
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage :")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : Backup interval in minutes")
            print("SourceDirectory : Directory to be backed up")

        else:

            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # Example:
    # python Demo.py 5 Data

    elif(len(sys.argv) == 3):

        print("Inside project logic")
        print("Time Interval :", sys.argv[1])
        print("Directory Name :", sys.argv[2])

        # Schedule backup task after specified interval
        schedule.every(int(sys.argv[1])).minutes.do(
            MarvellousDataShieldStart,
            sys.argv[2]
        )

        print(Border)
        print("Data Shield System Started Successfully")
        print("Time Interval (Minutes) :", sys.argv[1])
        print("Press Ctrl + C to stop execution")
        print(Border)

        # Keep scheduler running continuously
        while True:

            # Execute pending scheduled jobs
            schedule.run_pending()

            # Delay to reduce CPU usage
            time.sleep(1)

    else:

        print("Invalid number of command line arguments")
        print("Unable to proceed")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)

#----------------------------------------------------------------------------------------
# Application Starter
#----------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
