# PC Diagnostic Tool

A simple **Python-based PC Diagnostic Tool** that runs in the terminal and displays useful information about a computer's system, CPU, RAM, disk, network, battery, processes, storage, performance, and overall system health.

This project was created as a beginner-friendly Python project to practice functions, loops, conditional statements, user input, file handling, system information, exception handling, process management, directory handling, and the use of Python libraries.

## Features

### System Information

* Operating system
* System version
* Computer name
* Machine type
* System architecture
* Processor information

### CPU Information

* Physical CPU cores
* Logical CPU cores
* CPU usage
* CPU frequency
* Minimum CPU frequency
* Maximum CPU frequency
* CPU usage per individual core

### RAM Information

* Total RAM
* Used RAM
* Available RAM
* RAM usage percentage

### Virtual Memory and Swap

* Virtual memory information
* Virtual memory usage
* Available virtual memory
* Swap memory
* Swap memory usage
* Swap memory free space

### Disk Information

* Available drives
* Total storage
* Used storage
* Free storage
* Disk usage percentage
* Disk activity
* Total read operations
* Total write operations
* Read and write counts

### Storage Summary

* Total storage
* Used storage
* Free storage
* Overall storage information

### Disk Space Warning

* Checks disk usage
* Displays storage usage
* Warns when disk space is getting low
* Identifies drives with high storage usage

### Network Information

* Computer name
* Local IP address
* Basic network information

### Network Interfaces

* Network adapter names
* IP addresses
* Network masks
* Broadcast addresses
* Available network interfaces

### Network Connections

* Active network connections
* Connection status
* Local address information
* Network connection count

### Hostname and DNS Information

* Computer hostname
* Canonical hostname
* IP addresses associated with the computer
* Basic DNS information

### Internet Connection Test

* Tests basic internet connectivity
* Checks connection to a test server
* Displays connection status
* Measures basic response time

### Ping Test

* Allows the user to enter a website or IP address
* Sends four ping requests
* Displays ping results
* Supports Windows and other operating systems
* Helps check basic network connectivity

### MAC Address

* Detects the computer's MAC address
* Displays the MAC address in a readable format

### Battery Information

* Battery percentage
* Charging status
* Estimated remaining time
* Battery power status

### Detailed Battery Health

* Battery percentage
* Charging status
* Estimated remaining time
* Battery condition
* High, normal, low, or critical battery status

### System Uptime

* Boot time
* Current time
* System uptime

### Boot Information

* Last boot time
* Current time
* Calculated uptime

### System Temperature

* Checks available temperature sensors
* Displays temperature readings where supported
* Supports systems that provide temperature sensor information

### System Health Check

* CPU usage status
* RAM usage status
* Basic health warnings
* Overall system health status

### Quick Diagnostic Scan

* Performs a quick system check
* Checks CPU usage
* Checks RAM usage
* Checks disk usage
* Checks battery level when available
* Displays potential issues
* Reports whether major problems were detected

### Diagnostic Checklist

* Checks CPU usage
* Checks RAM usage
* Checks disk usage
* Checks battery status
* Displays warnings
* Counts detected issues
* Provides a simple diagnostic checklist

### System Health Score

* CPU health score
* RAM health score
* Disk health score
* Overall health score
* Health status

### Performance Summary

* CPU performance status
* RAM performance status
* Disk usage status
* Basic performance warnings

### System Summary

* Computer information
* Operating system
* Processor
* CPU cores
* CPU usage
* RAM
* Disk storage
* Disk usage
* Python version

### Running Processes

* Currently running processes
* Process ID
* Process name
* Process status
* Total process count
* Displays a list of running processes

### Top CPU Processes

* Processes using the most CPU
* CPU usage percentage
* Process ID
* Process name
* Sorts processes based on CPU usage

### Top RAM Processes

* Processes using the most RAM
* Memory usage percentage
* Process ID
* Process name
* Sorts processes based on memory usage

### Process Search

* Searches for a running process
* Allows the user to enter a process name
* Displays matching process IDs
* Displays process status
* Helps locate specific running programs

### Process Termination

* Allows the user to enter a process ID
* Displays the selected process
* Asks for confirmation before termination
* Attempts to terminate the selected process
* Handles invalid process IDs
* Handles permission errors

### System Resource Monitor

* Continuously monitors CPU usage
* Continuously monitors RAM usage
* Displays updated resource information
* Runs until the user stops the monitor
* Uses `CTRL+C` to stop monitoring

### Python Information

* Python version
* Python installation path
* Python build
* Python compiler

### Python Package Check

* Checks installed Python packages
* Checks `psutil`
* Checks `pip`
* Checks `setuptools`
* Displays whether packages are installed

### GPU Information

* Graphics card information
* GPU name
* GPU memory information
* Driver information where available

### Motherboard Information

* Motherboard manufacturer
* Motherboard product information
* Serial number where available

### User Information

* Current Windows username
* Home directory
* Computer name

### Environment Variables

* Displays system environment variables
* Shows variable names and values
* Displays the number of available variables
* Limits displayed results to prevent excessive terminal output

### Folder Size Checker

* Allows the user to enter a folder path
* Calculates folder size
* Displays size in MB
* Displays size in GB
* Handles inaccessible files

### Folder File Counter

* Counts files inside a folder
* Counts folders inside a folder
* Supports subfolders
* Displays the total number of files
* Displays the total number of folders

### File Extension Analyzer

* Scans files inside a folder
* Groups files by extension
* Counts different file types
* Sorts extensions by file count
* Identifies files without an extension

### Large File Finder

* Allows the user to enter a folder path
* Searches for large files
* Allows the user to set a minimum file size
* Sorts large files by size
* Displays the largest files found
* Handles inaccessible files

### Duplicate File Finder

* Searches for possible duplicate files
* Groups files based on file size
* Displays possible duplicate groups
* Shows file paths
* Helps identify files that may take unnecessary storage space

> The current duplicate-file feature groups files by size. It does not perform a complete file-content hash comparison.

### Temporary File Checker

* Finds the system temporary folder
* Counts temporary files
* Calculates temporary file size
* Displays temporary storage usage

### Windows Services

* Displays Windows services
* Lists available service names
* Supports Windows systems
* Displays up to 30 services

### Startup Programs

* Checks Windows startup folders
* Displays startup files
* Checks user startup folder
* Checks system startup folder

### System Architecture Details

* Operating system
* OS release
* OS version
* Machine type
* Processor
* Architecture
* Platform information
* Python version

### Save Diagnostic Report

* Creates a diagnostic report
* Saves the report as a `.txt` file
* Includes system information
* Includes CPU usage
* Includes RAM usage
* Includes disk usage
* Includes username
* Includes Python version
* Includes report date and time

### Help

* Explains how to use the program
* Provides basic instructions
* Explains the menu system
* Provides information about diagnostic limitations

### About

* Displays information about the project
* Shows the project purpose
* Displays the project version
* Shows the technologies used

### Clear Screen

* Clears the terminal screen
* Supports Windows
* Supports other operating systems

## Menu

```text
========================================
          PC DIAGNOSTIC TOOL
========================================
1.  System Information
2.  CPU Information
3.  RAM Information
4.  Disk Information
5.  Network Information
6.  Battery Information
7.  System Uptime
8.  System Health Check
9.  Full Diagnostic Report
10. Running Processes
11. Top CPU Processes
12. Top RAM Processes
13. Network Connections
14. Python Information
15. Performance Summary
16. System Health Score
17. Folder Size Checker
18. Save Diagnostic Report
19. GPU Information
20. Motherboard Information
21. User Information
22. Environment Variables
23. Internet Connection Test
24. Ping Test
25. MAC Address
26. Storage Summary
27. Large File Finder
28. Temporary File Checker
29. Boot Information
30. System Temperature
31. Disk Space Warning
32. Quick Diagnostic Scan
33. System Summary
34. Help
35. About
36. CPU Load Per Core
37. Virtual Memory / Swap
38. Disk Activity
39. Network Interface Details
40. Hostname and DNS Information
41. Windows Services
42. Startup Programs
43. System Architecture Details
44. Python Package Check
45. Folder File Counter
46. File Extension Analyzer
47. Duplicate File Finder
48. Detailed Battery Health
49. Diagnostic Checklist
50. System Resource Monitor
51. Process Search
52. Process Termination
53. Clear Screen
0.  Exit
========================================
```

## Technologies Used

* Python
* `psutil`
* `platform`
* `socket`
* `datetime`
* `os`
* `sys`
* `subprocess`
* `getpass`
* `uuid`
* `tempfile`

## Requirements

Before running the program, make sure you have:

* Python 3.x
* PyCharm, VS Code, or another Python editor
* `psutil`
* Windows for some Windows-specific hardware and system information features

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PC-Diagnostic-Tool.git
```

### 2. Open the Project

Open the project folder in **PyCharm** or your preferred Python editor.

### 3. Install psutil

Open the terminal and run:

```bash
pip install psutil
```

You can also install it using:

```bash
python -m pip install psutil
```

### 4. Run the Program

Run:

```bash
python main.py
```

Or run `main.py` directly from PyCharm.

## Project Structure

```text
PC-Diagnostic-Tool/
│
├── main.py
├── README.md
└── requirements.txt
```

## Example

When the program starts, it displays a menu where the user can choose which diagnostic function they want to use.

Example:

```text
========================================
          PC DIAGNOSTIC TOOL
========================================
1.  System Information
2.  CPU Information
3.  RAM Information
4.  Disk Information
...
49. Diagnostic Checklist
50. System Resource Monitor
51. Process Search
52. Process Termination
53. Clear Screen
0.  Exit
========================================

Enter your choice:
```

### CPU Information

```text
Enter your choice: 2

---------- CPU INFORMATION ----------
CPU Cores        : 4
Logical CPUs     : 8
CPU Usage        : 15.2 %
CPU Frequency    : 2394.0 MHz
Minimum Frequency: 800.0 MHz
Maximum Frequency: 4200.0 MHz
```

### CPU Load Per Core

```text
Enter your choice: 36

---------- CPU LOAD PER CORE ----------
CPU Core 1 : 12.5 %
CPU Core 2 : 18.2 %
CPU Core 3 : 9.7 %
CPU Core 4 : 14.1 %
```

### Virtual Memory

```text
Enter your choice: 37

---------- VIRTUAL MEMORY ----------
Virtual Memory Total : 16.0 GB
Virtual Memory Used  : 9.5 GB
Virtual Memory Free  : 6.5 GB
Virtual Memory Usage : 59.4 %

Swap Memory Total    : 4.0 GB
Swap Memory Used     : 0.5 GB
Swap Memory Free     : 3.5 GB
Swap Memory Usage    : 12.5 %
```

### Disk Activity

```text
Enter your choice: 38

---------- DISK ACTIVITY ----------
Total Read  : 245.32 GB
Total Write : 182.47 GB
Read Count  : 124583
Write Count : 98452
```

### Network Interface Details

```text
Enter your choice: 39

---------- NETWORK INTERFACES ----------

Interface: Ethernet
  Family : ...
  Address: 192.168.1.10
  Netmask: 255.255.255.0
```

### Hostname and DNS

```text
Enter your choice: 40

---------- HOSTNAME AND DNS ----------
Hostname : DESKTOP-PC
Canonical Name : DESKTOP-PC
IP Addresses :
 - 192.168.1.10
```

### Running Processes

```text
Enter your choice: 10

---------- RUNNING PROCESSES ----------
Total Processes : 145

PID       NAME                         STATUS
-----------------------------------------------
1          System                       running
432        explorer.exe                 running
1024       python.exe                   running
...
```

### Top CPU Processes

```text
Enter your choice: 11

---------- TOP CPU PROCESSES ----------

PID       CPU %      NAME
-----------------------------------------------
1024      15.4       python.exe
432       8.7        explorer.exe
2210      5.2        chrome.exe
```

### Process Search

```text
Enter your choice: 51

---------- PROCESS SEARCH ----------
Enter process name to search: chrome

PID: 2210 | Name: chrome.exe | Status: running
PID: 2350 | Name: chrome.exe | Status: running
```

### Process Termination

```text
Enter your choice: 52

---------- PROCESS TERMINATION ----------
Enter process PID: 2210

Process Name: example.exe
Are you sure you want to terminate this process? (yes/no): no

Process termination cancelled.
```

### System Health Check

```text
---------- SYSTEM HEALTH CHECK ----------

CPU Usage : 23.5 %
RAM Usage : 61.2 %

CPU Status : Normal
RAM Status : Normal

Health Check Complete.
```

### Quick Diagnostic Scan

```text
========================================
         QUICK DIAGNOSTIC SCAN
========================================

CPU Usage : 23.5 %
RAM Usage : 61.2 %
Disk Usage: 48.7 %

Checking system status...

[OK] CPU usage is normal.
[OK] RAM usage is normal.
[OK] Disk space is sufficient.
[OK] Battery level is acceptable.

----------------------------------------
No major problems detected.
Quick scan complete.
```

### Diagnostic Checklist

```text
---------- DIAGNOSTIC CHECKLIST ----------

Checking CPU...
[OK] CPU usage is acceptable.

Checking RAM...
[OK] RAM usage is acceptable.

Checking Disk...
[OK] Disk space is acceptable.

Checking Battery...
[OK] Battery level is acceptable.

========================================
Diagnostic Checklist: No major issues found.
========================================
```

### System Resource Monitor

```text
---------- SYSTEM RESOURCE MONITOR ----------
Press CTRL+C to stop the monitor.

CPU: 18.5% | RAM: 55.2%
CPU: 21.3% | RAM: 55.4%
CPU: 17.8% | RAM: 55.1%
```

Press `CTRL+C` to stop the monitor.

### System Summary

```text
========================================
          SYSTEM SUMMARY
========================================

Computer Name : DESKTOP-PC
Operating System: Windows
OS Version     : Windows Version
Processor      : Intel Processor
CPU Cores      : 4
Logical CPUs   : 8
CPU Usage      : 15.2 %
Total RAM      : 16.0 GB
RAM Usage      : 61.2 %
System Disk    : 476.84 GB
Disk Usage     : 48.7 %
Python Version : 3.x.x
```

### Large File Finder

```text
---------- LARGE FILE FINDER ----------

Enter folder path: C:\Users\User\Downloads
Minimum file size in MB: 500

Searching...

Large Files:
-----------------------------------------------
1250.45 MB - C:\Users\User\Downloads\file1.zip
850.20 MB - C:\Users\User\Downloads\video.mp4
620.75 MB - C:\Users\User\Downloads\backup.zip
```

### File Extension Analyzer

```text
---------- FILE EXTENSION ANALYZER ----------

File Types:
.txt : 25 file(s)
.py : 18 file(s)
.jpg : 12 file(s)
.mp4 : 5 file(s)
.zip : 3 file(s)
```

### Folder File Counter

```text
---------- FOLDER FILE COUNTER ----------

Folder : C:\Users\User\Downloads
Files  : 125
Folders: 18
```

### Duplicate File Finder

```text
---------- DUPLICATE FILE FINDER ----------

Possible duplicate group:
File Size: 125.50 MB
- C:\Users\User\Downloads\file1.zip
- C:\Users\User\Documents\file1.zip

Possible duplicate groups: 1
Files were grouped by size only.
```

### Internet Connection Test

```text
---------- INTERNET CONNECTION TEST ----------

Connection Status : Connected
Test Server       : google.com
Response Time     : 25.31 ms
```

### Ping Test

```text
---------- PING TEST ----------

Enter website or IP address: google.com

Pinging google.com...
Reply from ...
Reply from ...
Reply from ...
Reply from ...
```

### Save Diagnostic Report

The program can create a text file called:

```text
diagnostic_report.txt
```

The report contains basic system and performance information that can be saved for later reference.

Example:

```text
========================================
       PC DIAGNOSTIC REPORT
========================================

System Information
------------------
Operating System : Windows
System Version   : Windows Version
Computer Name    : DESKTOP-PC
Architecture     : 64bit
Processor        : Intel Processor

Performance
-----------
CPU Usage  : 15.2%
RAM Usage  : 61.2%
Disk Usage : 48.7%

Python Version : 3.x.x
Username       : User

Report Created : 2026-09-28 10:30:15
========================================
```

## Learning Objectives

This project helps practice the following Python concepts:

* Functions
* Function parameters
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* Lists
* Dictionaries
* User input using `input()`
* Modules and libraries
* Exception handling
* Basic calculations
* File handling
* Reading computer resource usage
* Sorting system data
* Processing lists of processes
* Working with operating system information
* Working with directories and files
* Searching through files
* Processing file extensions
* Working with process IDs
* Working with `subprocess`
* Working with environment variables
* Working with dates and times
* Creating menu-driven programs
* Monitoring system resources
* Generating text reports

## Purpose

The purpose of this project is to create a simple command-line tool that allows users to check useful computer information without using a graphical interface.

It is also a practice project for learning how Python can interact with information from the computer's operating system.

The project has been expanded to provide more **performance monitoring, file analysis, process management, storage analysis, network diagnostics, and system diagnostic features**.

Users can now check:

```text
System Information
        ↓
CPU Information
        ↓
RAM Information
        ↓
Storage Information
        ↓
Network Information
        ↓
Battery Information
        ↓
Running Processes
        ↓
File and Folder Information
        ↓
Performance Monitoring
        ↓
Network Diagnostics
        ↓
Hardware Information
        ↓
Health Checks
        ↓
Diagnostic Report
```

## Diagnostic Features

The tool can be used to perform several basic diagnostic checks:

### Hardware

* CPU
* RAM
* Disk
* GPU
* Motherboard
* Battery
* Temperature sensors

### Operating System

* Windows information
* System architecture
* Boot information
* Running processes
* Windows services
* Startup programs
* Environment variables

### Storage

* Disk usage
* Storage summary
* Folder size
* File count
* File extensions
* Large files
* Temporary files
* Possible duplicate files

### Network

* IP address
* Network interfaces
* Network connections
* DNS information
* Internet connection
* Ping testing
* MAC address

### Performance

* CPU usage
* CPU usage per core
* RAM usage
* Virtual memory
* Swap memory
* Disk activity
* Process CPU usage
* Process RAM usage
* Resource monitoring
* System health score

## Important Notes

Some features depend on the computer and operating system.

For example:

* Battery information may not be available on desktop computers.
* Temperature information depends on available hardware sensors.
* GPU and motherboard information may depend on Windows system tools.
* Some process and network information may require administrator permissions.
* Different computers may display different hardware information.
* The internet connection test requires an active network connection.
* The ping test depends on the destination server allowing ping requests.
* Windows services and startup information are intended mainly for Windows systems.
* Some commands may not be available on newer Windows installations.
* Hardware information can vary depending on the manufacturer's drivers.
* Process termination may fail when administrator permissions are required.
* Duplicate files are currently identified by matching file sizes rather than comparing complete file contents.
* Environment variables may contain system-specific information and should be handled carefully when sharing reports.

## Safety and Usage Notes

This program is mainly designed to **read and display diagnostic information**.

Some features can interact with running processes, particularly the **Process Termination** feature.

Before terminating a process, make sure you understand what the process is used for. System processes should not be terminated unless you know what you are doing.

The program also does not automatically delete files, clean temporary files, modify system settings, or change hardware configurations.

## Future Improvements

Possible features that can be added in future versions:

* Internet speed test
* More detailed CPU temperature monitoring
* More detailed GPU information
* More detailed storage information
* Export reports as `.csv` files
* System performance history
* Automatic health recommendations
* Process filtering
* Process monitoring with automatic refresh
* Network speed monitoring
* Detailed network adapter information
* More startup application information
* Automatic diagnostic report generation
* Graphs and charts for CPU and RAM usage
* Automatic temporary file cleanup
* Hardware inventory
* More advanced disk health information
* File hash comparison for more accurate duplicate detection
* Real-time disk monitoring
* Real-time network monitoring

## Disclaimer

This project is intended for **educational and personal use**. The diagnostic information displayed depends on the computer and operating system where the program is running.

Some features may provide different information depending on the operating system, available hardware, permissions, installed system components, drivers, and available system tools.

The program is designed primarily for monitoring and displaying information and should not be considered a professional hardware diagnostic or repair tool.

## Author

**Jose Navoa**

Aspiring Information Technology Student

Created as a Python learning project.
