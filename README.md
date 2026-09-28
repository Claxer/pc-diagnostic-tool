# PC Diagnostic Tool

A simple **Python-based PC Diagnostic Tool** that runs in the terminal and displays useful information about a computer's system, CPU, RAM, disk, network, battery, processes, storage, performance, and overall system health.

This project was created as a beginner-friendly Python project to practice functions, loops, conditional statements, user input, file handling, system information, exception handling, and the use of Python libraries.

## Features

* System Information

  * Operating system
  * System version
  * Computer name
  * Machine type
  * System architecture
  * Processor information

* CPU Information

  * Physical CPU cores
  * Logical CPU cores
  * CPU usage
  * CPU frequency
  * Minimum CPU frequency
  * Maximum CPU frequency

* RAM Information

  * Total RAM
  * Used RAM
  * Available RAM
  * RAM usage percentage

* Disk Information

  * Available drives
  * Total storage
  * Used storage
  * Free storage
  * Disk usage percentage

* Network Information

  * Computer name
  * Local IP address

* Battery Information

  * Battery percentage
  * Charging status
  * Estimated remaining time
  * Battery power status

* System Uptime

  * Boot time
  * Current time
  * System uptime

* System Health Check

  * CPU usage status
  * RAM usage status
  * Basic health warnings
  * Overall system health status

* Running Processes

  * Currently running processes
  * Process ID
  * Process name
  * Process status
  * Total process count

* Top CPU Processes

  * Processes using the most CPU
  * CPU usage percentage
  * Process ID
  * Process identification

* Top RAM Processes

  * Processes using the most RAM
  * Memory usage percentage
  * Process ID
  * Process identification

* Network Connections

  * Active network connections
  * Connection status
  * Local address information
  * Network connection count

* Python Information

  * Python version
  * Python installation path
  * Python build
  * Python compiler

* Performance Summary

  * CPU performance status
  * RAM performance status
  * Disk usage status
  * Basic performance warnings

* System Health Score

  * CPU health score
  * RAM health score
  * Disk health score
  * Overall health score
  * Health status

* Folder Size Checker

  * Select a folder
  * Calculate folder size
  * Display size in MB
  * Display size in GB
  * Handle inaccessible files

* Save Diagnostic Report

  * Creates a diagnostic report
  * Saves the report as a `.txt` file
  * Includes system information
  * Includes CPU usage
  * Includes RAM usage
  * Includes disk usage
  * Includes report date and time

* GPU Information

  * Graphics card information
  * GPU name
  * GPU memory information
  * Driver information where available

* Motherboard Information

  * Motherboard manufacturer
  * Motherboard product information
  * Serial number where available

* User Information

  * Current Windows username
  * Home directory
  * Computer name

* Environment Variables

  * Displays system environment variables
  * Shows variable names and values
  * Displays the number of available variables

* Internet Connection Test

  * Tests basic internet connectivity
  * Checks connection to a test server
  * Displays connection status
  * Measures basic response time

* Ping Test

  * Allows the user to enter a website or IP address
  * Sends four ping requests
  * Displays the ping results
  * Helps check network connectivity

* MAC Address

  * Detects the computer's MAC address
  * Displays the MAC address in a readable format

* Storage Summary

  * Calculates total storage
  * Calculates used storage
  * Calculates free storage
  * Displays overall storage information

* Large File Finder

  * Allows the user to select a folder
  * Searches for large files
  * Allows the user to set a minimum file size
  * Sorts large files by size
  * Displays the largest files found

* Temporary File Checker

  * Finds the system temporary folder
  * Counts temporary files
  * Calculates temporary file size
  * Displays temporary storage usage

* Boot Information

  * Displays the last boot time
  * Displays the current time
  * Calculates system uptime

* System Temperature

  * Checks available temperature sensors
  * Displays temperature readings where supported
  * Supports systems that provide temperature sensor information

* Disk Space Warning

  * Checks disk usage
  * Displays available storage
  * Warns when disk space is getting low
  * Identifies drives with high storage usage

* Quick Diagnostic Scan

  * Performs a quick system check
  * Checks CPU usage
  * Checks RAM usage
  * Checks disk usage
  * Checks battery level when available
  * Displays potential issues

* System Summary

  * Displays important system information
  * CPU information
  * RAM information
  * Disk information
  * Operating system information
  * Python information
  * Computer information

* Help

  * Explains how to use the program
  * Provides basic instructions
  * Explains the menu system
  * Provides information about diagnostic limitations

* About

  * Displays information about the project
  * Shows the project purpose
  * Displays the project version
  * Shows the technologies used

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
* `shutil`

## Requirements

Before running the program, make sure you have:

* Python 3.x
* PyCharm, VS Code, or another Python editor
* `psutil`
* Windows for some Windows-specific hardware information features

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
32. Quick Diagnostic Scan
33. System Summary
34. Help
35. About
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
* Using `subprocess`
* Working with environment variables
* Working with dates and times
* Creating menu-driven programs

## Purpose

The purpose of this project is to create a simple command-line tool that allows users to check useful computer information without using a graphical interface.

It is also a practice project for learning how Python can interact with information from the computer's operating system.

The project has been expanded to provide more **performance monitoring and diagnostic features**, allowing users to check running processes, resource usage, storage, network connectivity, hardware information, temporary files, large files, and overall system condition.

## Diagnostic Features

The tool can be used to perform several basic diagnostic checks:

```text
System
   ↓
CPU
   ↓
RAM
   ↓
Storage
   ↓
Network
   ↓
Battery
   ↓
Processes
   ↓
Performance
   ↓
Health Check
   ↓
Quick Diagnostic Scan
   ↓
Diagnostic Report
```

The program is designed to provide information and warnings rather than make permanent changes to the computer.

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

## Future Improvements

Possible features that can be added in future versions:

* Internet speed test
* More detailed CPU temperature monitoring
* More detailed GPU information
* More detailed storage information
* Export reports as `.csv` files
* System performance history
* Automatic health recommendations
* Process search and filtering
* Process monitoring with automatic refresh
* Network speed monitoring
* Detailed network adapter information
* Startup application information
* Automatic diagnostic report generation
* Graphs and charts for CPU and RAM usage
* Automatic temporary file cleanup
* Hardware inventory
* More advanced disk health information

## Disclaimer

This project is intended for **educational and personal use**. The diagnostic information displayed depends on the computer and operating system where the program is running.

Some features may provide different information depending on the operating system, available hardware, permissions, installed system components, and available system tools.

The program is designed primarily for monitoring and displaying information and should not be considered a professional hardware diagnostic or repair tool.

## Author

**Jose Navoa**

Aspiring Information Technology Student

Created as a Python learning project.
