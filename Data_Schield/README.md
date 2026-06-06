# Marvellous Data Shield
An automated Python-based backup system that performs incremental backups, detects file changes using MD5 hashing, and automatically creates ZIP archives for secure storage.
---

## Overview
Marvellous Data Shield is designed to automate the process of backing up important files and folders. Instead of copying all files every time, the system intelligently identifies only new or modified files and backs them up, making the process faster and more storage-efficient.

The application also generates compressed ZIP archives of the backup folder and supports scheduled execution at user-defined intervals.
---

## Features
```
-> Automated backup scheduling
-> Incremental backup mechanism
-> MD5 hash-based file comparison
-> Copies only new or modified files
-> Preserves original file metadata
-> Automatic ZIP archive creation
-> Command-line interface support
-> Lightweight and easy to use

```
## Usage
Display Help
python DataShield.py --h

Display Usage Information
python DataShield.py --u

Start Automated Backup
python DataShield.py 5 Data

## Sample Output
```
--------------------------------------------------
--------- Marvellous Data Shield System ----------
--------------------------------------------------

Data Shield System Started Successfully
Time Interval (Minutes) : 5

Press Ctrl + C to stop execution

--------------------------------------------------
Backup Process Started Successfully at :
Sat Feb 07 10:30:00 2026
--------------------------------------------------

Backup Completed Successfully
Files Copied : 15
ZIP File Created :
MarvellousBackup_2026-02-07_10-30-00.zip
--------------------------------------------------
```
## Project Structure
```
Data-Shield/
│
|---src/
|    |
|    |── Data_Shield.py
├── README.md
```

## Concepts Implemented

-> File Handling
-> Directory Traversal
-> Incremental Backup
-> MD5 Hashing
-> Task Scheduling
-> Data Compression
-> Command-Line Argument Processing
-> Automation Scripting

## Future Enhancements
-> Email notification after backup completion
-> GUI-based dashboard
-> Multi-directory backup support
