# PC Diagnostic Tool

A simple **Python-based PC Diagnostic Tool** that runs in the terminal and displays basic information about a computer's system, CPU, RAM, disk, network, battery, uptime, and overall system health.

This project was created as a beginner-friendly Python project to practice functions, loops, conditional statements, user input, and the use of Python libraries.

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

* System Uptime

  * Boot time
  * Current time
  * System uptime

* System Health Check

  * CPU usage status
  * RAM usage status
  * Disk usage status
  * Basic health warnings
  * Overall system health status

* Process Information

  * Currently running processes
  * Process ID
  * Process name
  * Process status
  * CPU usage
  * Memory usage

* Top Resource-Using Processes

  * Processes using the most CPU
  * Processes using the most RAM
  * Resource usage percentages
  * Process identification

* Disk Health Check

  * Disk usage monitoring
  * Storage warnings
  * Available free space
  * Disk health status

* Network Status Check

  * Network interface information
  * Network connection status
  * IP address information
  * Basic network diagnostics

* System Performance Check

  * CPU performance status
  * RAM performance status
  * Disk usage status
  * Overall performance summary

* Diagnostic Summary

  * Summary of important system information
  * CPU status
  * RAM status
  * Disk status
  * Network status
  * Battery status
  * Overall diagnostic result

* Full Diagnostic Report

  * Displays all available diagnostic information in one report
  * Includes system information
  * Includes hardware information
  * Includes resource usage
  * Includes health checks
  * Includes performance information

* Refresh Information

  * Allows system information to be checked again
  * Updates CPU and RAM usage
  * Updates disk information
  * Updates process information
  * Updates system health information

* User-Friendly Menu

  * Number-based menu system
  * Easy navigation
  * Return to the main menu
  * Exit option

## Menu

```text
========================================
          PC DIAGNOSTIC TOOL
========================================
1. System Information
2. CPU Information
3. RAM Information
4. Disk Information
5. Network Information
6. Battery Information
7. System Uptime
8. System Health Check
9. Process Information
10. Top Resource-Using Processes
11. Disk Health Check
12. Network Status Check
13. System Performance Check
14. Diagnostic Summary
15. Full Diagnostic Report
0. Exit
========================================
```

## Technologies Used

* Python
* `psutil`
* `platform`
* `socket`
* `datetime`
* `os`

## Requirements

Before running the program, make sure you have:

* Python 3.x
* PyCharm, VS Code, or another Python editor
* Internet connection for installing the required library

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

When the program starts, it displays a menu where the user can choose which information they want to view.

Example:

```text
Enter your choice: 2

---------- CPU INFORMATION ----------
CPU Cores        : 4
Logical CPUs     : 8
CPU Usage        : 15.2 %
CPU Frequency    : 2394.0 MHz
```

A system health check may display:

```text
---------- SYSTEM HEALTH CHECK ----------

CPU Usage : 23.5 %
RAM Usage : 61.2 %
Disk Usage: 48.7 %

CPU Status : Normal
RAM Status : Normal
Disk Status: Normal

Overall Status: Healthy

Health Check Complete.
```

The process information feature may display:

```text
---------- PROCESS INFORMATION ----------

PID      NAME                 STATUS
------------------------------------------------
1024     chrome.exe           running
2456     explorer.exe         running
3812     python.exe           running
```

The top resource-using processes may display:

```text
---------- TOP RESOURCE-USING PROCESSES ----------

CPU Usage:
chrome.exe       : 18.4 %
python.exe       : 7.2 %

RAM Usage:
chrome.exe       : 12.5 %
Discord.exe      : 8.3 %
```

The diagnostic summary provides a quick overview:

```text
---------- DIAGNOSTIC SUMMARY ----------

CPU Status       : Normal
RAM Status       : Normal
Disk Status      : Normal
Network Status   : Connected
Battery Status   : Charging

Overall System Status: Healthy
```

## Learning Objectives

This project helps practice the following Python concepts:

* Functions
* Function parameters
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* Lists and system data
* Dictionaries
* User input using `input()`
* Modules and libraries
* Exception handling
* Basic calculations
* Working with system information
* Sorting system data
* Processing lists of processes
* Reading computer resource usage
* Creating menu-driven programs

## Purpose

The purpose of this project is to create a simple command-line tool that allows users to check basic computer information without using a graphical interface.

It is also a practice project for learning how Python can interact with information from the computer's operating system.

The project has also been expanded to provide basic **performance monitoring and diagnostic features**, allowing users to check running processes, resource usage, storage health, network status, and overall system condition.

## Future Improvements

Possible features that can be added in future versions:

* Internet speed test
* CPU temperature monitoring
* More detailed storage information
* Save diagnostic reports as `.txt` files
* Export reports as `.csv` files
* System performance history
* Automatic health recommendations
* More detailed hardware information
* Process search and filtering
* Process monitoring with automatic refresh
* Network speed monitoring
* Detailed network adapter information
* Hardware temperature information
* Startup application information
* System information export
* Automatic diagnostic report generation

## Disclaimer

This project is intended for **educational and personal use**. The diagnostic information displayed depends on the computer and operating system where the program is running.

Some features may provide different information depending on the operating system, available hardware, permissions, and installed system components.

## Author

**Jose Navoa**

Aspiring Information Technology Student

Created as a Python learning project.
