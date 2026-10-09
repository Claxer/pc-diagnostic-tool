# PC Diagnostic Tool

A simple **Python-based PC Diagnostic Tool** that runs in the terminal and provides a wide range of system diagnostic and monitoring features. The program can display information about the computer's hardware, operating system, CPU, RAM, storage, network, battery, running processes, Python environment, files, folders, and overall system health.

The project started as a basic system information program and was expanded into a more complete command-line diagnostic utility. It now includes **hardware monitoring, process management, storage analysis, network testing, file analysis, performance monitoring, health checks, and diagnostic report generation**.

This project was created as a beginner-friendly Python project to practice functions, loops, conditional statements, user input, lists, dictionaries, exception handling, file handling, directory traversal, process management, subprocess commands, system information, and external Python libraries.

---

## Features

### CPU Load Per Core

The tool can display CPU usage for each individual processor core.

* Displays each CPU core
* Shows CPU usage percentage
* Uses a loop to display each core
* Helps identify uneven CPU usage
* Provides more detailed CPU monitoring

### Virtual Memory and Swap

The program provides information about virtual memory and swap memory.

* Virtual memory total
* Virtual memory used
* Available virtual memory
* Virtual memory usage percentage
* Swap memory total
* Swap memory used
* Swap memory free space
* Swap memory usage percentage

### Disk Activity

The tool can display basic disk activity information.

* Total read operations
* Total write operations
* Total data read
* Total data written
* Disk I/O statistics

### Network Interface Details

The program can inspect available network interfaces.

* Network interface names
* IP addresses
* Network masks
* Broadcast addresses
* Available network adapters
* Address family information

### Hostname and DNS Information

The program can retrieve basic hostname and DNS-related information.

* Computer hostname
* Canonical hostname
* IP addresses
* Hostname lookup information
* Basic DNS information

### Windows Services

For Windows systems, the program can display available Windows services.

* Lists Windows services
* Displays service names
* Uses the Windows `sc` command
* Displays up to 30 services
* Handles systems where the command is unavailable

### Startup Programs

The program checks the Windows startup folders.

* User startup folder
* System startup folder
* Startup files
* Startup shortcuts
* Displays detected startup items

### System Architecture Details

Provides additional operating system and architecture information.

* Operating system
* OS release
* OS version
* Machine type
* Processor
* System architecture
* Platform information
* Python version

### Python Package Check

The program checks whether important Python packages and tools are installed.

Currently checked packages include:

* `psutil`
* `pip`
* `setuptools`

The feature uses Python's package manager through `subprocess` to check package availability.

### Folder File Counter

The program can count files and folders inside a selected directory.

* Counts files
* Counts folders
* Includes subfolders
* Uses `os.walk()`
* Displays total file count
* Displays total folder count

### File Extension Analyzer

The tool can analyze the types of files inside a folder.

* Detects file extensions
* Counts files by extension
* Supports subfolders
* Detects files without extensions
* Sorts file types based on file count

Example:

```text
.py : 18 file(s)
.txt : 25 file(s)
.jpg : 12 file(s)
.mp4 : 5 file(s)
```

### Duplicate File Finder

The program can search for possible duplicate files.

* Scans files inside a folder
* Groups files based on file size
* Displays possible duplicate groups
* Displays file paths
* Shows the size of possible duplicate files

> The current version identifies possible duplicates by comparing file sizes. It does not compare the actual contents or file hashes.

### Detailed Battery Health

Provides additional battery information.

* Battery percentage
* Charging status
* Estimated remaining time
* Battery condition
* High battery status
* Normal battery status
* Low battery status
* Critical battery status

### Diagnostic Checklist

The program performs a basic checklist of important system resources.

It checks:

* CPU usage
* RAM usage
* Disk usage
* Battery status

The program counts detected issues and displays a final diagnostic result.

### System Resource Monitor

The program can continuously monitor system resources.

* Real-time CPU usage
* Real-time RAM usage
* Continuous monitoring
* Updates every second
* Runs until manually stopped
* Uses `CTRL+C` to stop monitoring

Example:

```text
---------- SYSTEM RESOURCE MONITOR ----------
Press CTRL+C to stop the monitor.

CPU: 18.5% | RAM: 55.2%
CPU: 21.3% | RAM: 55.4%
CPU: 17.8% | RAM: 55.1%
```

### Process Search

The program can search for running processes.

* Allows the user to enter a process name
* Searches currently running processes
* Displays matching process IDs
* Displays process names
* Displays process status
* Handles processes that disappear during scanning

### Process Termination

The program provides a basic process termination feature.

* Accepts a process ID
* Displays the selected process name
* Requests user confirmation
* Attempts to terminate the process
* Handles invalid process IDs
* Handles missing processes
* Handles permission errors

Example:

```text
---------- PROCESS TERMINATION ----------
Enter process PID: 2210

Process Name: example.exe
Are you sure you want to terminate this process? (yes/no): no

Process termination cancelled.
```

### Clear Screen

The program can clear the terminal screen.

* Supports Windows
* Supports other operating systems
* Uses `cls` on Windows
* Uses `clear` on other systems

---

### Resource History Logger

The tool can record CPU, RAM, and system-drive usage over a selected period and save the measurements to a CSV file.

* Lets the user choose a recording duration from 5 to 300 seconds
* Records a timestamp for each sample
* Tracks CPU, RAM, and disk usage percentages
* Displays measurements while recording
* Supports stopping the recording early with `CTRL+C`
* Saves the results to `resource_history.csv` for later review

### Process Details by PID

The program can show detailed information about a selected running process.

* Accepts a process ID (PID)
* Displays process name and status
* Shows the executable path and parent PID
* Displays the process creation time
* Shows CPU usage, memory usage, and memory percentage
* Reports the number of threads when available
* Handles invalid PIDs, closed processes, and permission errors

### Search Files by Name

The tool can search a selected folder and its subfolders for files by name.

* Searches using a full or partial file name
* Ignores uppercase and lowercase differences in the search term
* Displays the matching file paths
* Checks that the selected folder exists before searching
* Limits the displayed results to 200 matches to keep output manageable

### Recent Windows Event Logs

On Windows, the program can display recent events from the System event log.

* Lets the user choose between 1 and 30 recent events
* Displays event time, event ID, level, source, and message
* Uses PowerShell to retrieve event information
* Handles unavailable PowerShell commands, timeouts, and access errors
* Shows a message if used on a non-Windows operating system

### Installed Applications List

On Windows, the program can list applications registered in common Windows uninstall registry locations.

* Displays application names
* Displays version information when available
* Checks system-wide and current-user registry locations
* Removes duplicate name/version entries from the results
* Sorts the application list by name
* Skips entries that cannot be accessed

### Export System Snapshot

The program can export a timestamped text file containing a snapshot of important system information.

* Includes operating system, computer name, architecture, processor, and Python version
* Includes CPU core counts, usage, and frequency when available
* Includes RAM and swap usage
* Includes system-drive capacity and usage
* Includes network data sent and received
* Includes battery level and power connection status when available
* Creates a file named like `system_snapshot_YYYYMMDD_HHMMSS.txt`

> The Windows Event Logs and Installed Applications features are intended for Windows. Some information may be unavailable depending on the operating system, hardware, permissions, or system configuration.

---

# Updated Menu

The current version contains **69 numbered tools**, plus the exit option. Some tools are operating-system-specific, as noted in their descriptions.

```text
========================================
          PC DIAGNOSTIC TOOL
========================================

--- SYSTEM ---
1.  System Information
2.  System Architecture Details
3.  System Summary
4.  Current Date and Time
5.  Boot Information
6.  System Uptime

--- CPU AND MEMORY ---
7.  CPU Information
8.  CPU Load Per Core
9.  CPU Load Average
10. RAM Information
11. Detailed RAM Information
12. Virtual Memory / Swap
13. System Temperature

--- STORAGE ---
14. Disk Information
15. Disk Activity
16. Disk Speed Snapshot
17. Storage Summary
18. Disk Space Warning
19. Folder Size Checker
20. Folder File Counter
21. Large File Finder
22. File Extension Analyzer
23. Duplicate File Finder
24. Temporary File Checker

--- NETWORK ---
25. Network Information
26. Network Interface Details
27. Network Traffic
28. Network Speed Snapshot
29. Network Packet Statistics
30. Network Connections
31. Hostname and DNS Information
32. Internet Connection Test
33. Ping Test
34. MAC Address

--- BATTERY ---
35. Battery Information
36. Detailed Battery Health

--- PROCESSES ---
37. Running Processes
38. Process Count Summary
39. Top CPU Processes
40. Top RAM Processes
41. Process Search
42. Process Termination

--- WINDOWS ---
43. GPU Information
44. Motherboard Information
45. Windows Services
46. Startup Programs

--- PYTHON ---
47. Python Information
48. Python Package Check

--- USER ---
49. User Information
50. User Session Information
51. Environment Variables

--- DIAGNOSTICS ---
52. Health Check
53. Performance Summary
54. System Health Score
55. Quick Diagnostic Scan
56. Diagnostic Checklist
57. System Resource Snapshot
58. System Resource Monitor
59. Full Diagnostic Report
60. Save Diagnostic Report

--- OTHER ---
61. Help
62. About
63. Clear Screen

--- ADDITIONAL TOOLS ---
64. Record Resource History
65. Process Details by PID
66. Search Files by Name
67. Recent Windows Event Logs
68. List Installed Applications
69. Export System Snapshot

0.  Exit
========================================
```
---

# What Was Added in Version 3.1

The current version has been expanded from a basic PC information program into a more complete diagnostic tool.

### Hardware Monitoring

Added:

* CPU load per core
* Virtual memory
* Swap memory
* Disk activity
* Detailed battery health
* Temperature monitoring
* GPU information
* Motherboard information

### Process Management

Added:

* Running process listing
* Top CPU processes
* Top RAM processes
* Process searching
* Process termination
* Continuous resource monitoring

### Network Diagnostics

Added:

* Network interfaces
* Hostname and DNS information
* Network connections
* Internet connection testing
* Ping testing
* MAC address detection

### Storage and File Analysis

Added:

* Folder size checking
* Folder file counting
* File extension analysis
* Large file searching
* Possible duplicate file detection
* Temporary file checking
* Storage summary
* Disk space warnings

### Windows System Tools

Added:

* Windows services
* Startup programs
* Windows-specific hardware information
* System architecture details

### Python Environment

Added:

* Python information
* Python installation path
* Python build information
* Python compiler information
* Python package checking

### Diagnostic Tools

Added:

* Quick diagnostic scan
* Diagnostic checklist
* Performance summary
* System health score
* System summary
* Full diagnostic report
* Saved text reports

---

### Additional Tools Added in Version 3.1

The latest update adds six additional diagnostic and reporting functions:

* **Record Resource History** — logs CPU, RAM, and system-drive usage to a CSV file over a selected period.
* **Process Details by PID** — shows expanded information about a running process using its process ID.
* **Search Files by Name** — finds files by full or partial name within a selected folder and its subfolders.
* **Recent Windows Event Logs** — retrieves recent entries from the Windows System event log using PowerShell.
* **List Installed Applications** — lists applications registered in common Windows uninstall registry locations, including versions when available.
* **Export System Snapshot** — saves a timestamped text report containing key system, CPU, memory, storage, network, and battery details.

These additions expand the project’s resource logging, process inspection, file search, Windows troubleshooting, application inventory, and report-export capabilities.

---

# Updated Learning Objectives

This project provides practice with several important Python programming concepts:

* Functions
* Function calls
* Variables
* Strings
* Integers and floating-point numbers
* Lists
* Dictionaries
* Tuples
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* `input()`
* String methods
* File handling
* Directory traversal
* `os.walk()`
* Sorting data
* Lambda functions
* Exception handling
* `try` and `except`
* Modules
* External libraries
* Process management
* Process IDs
* System resource monitoring
* Subprocess commands
* Environment variables
* Date and time handling
* Network connections
* File extensions
* System information
* Menu-driven programming
* Report generation

---

# Python Modules Used

The project uses both built-in Python modules and the external `psutil` library.

### Built-in Modules

```text
platform
socket
os
sys
subprocess
getpass
uuid
tempfile
datetime
```

### External Library

```text
psutil
```

`psutil` is used to access system and process information such as:

* CPU usage
* CPU frequency
* RAM usage
* Disk usage
* Disk activity
* Network interfaces
* Network connections
* Battery information
* Running processes
* System uptime
* Temperature sensors

---

# Project Statistics

The current version provides:

```text
69 Numbered Tools
60+ Python Functions
Hardware Diagnostics
Software Diagnostics
Network Diagnostics
Storage Analysis
Process Management
Performance Monitoring
Health Checking
Report Generation
```

The exact number of available features may increase as the project continues to be developed.

---

# Diagnostic Categories

The program can now be divided into several major categories:

```text
PC DIAGNOSTIC TOOL
        |
        +-- Hardware
        |     +-- CPU
        |     +-- RAM
        |     +-- Disk
        |     +-- GPU
        |     +-- Motherboard
        |     +-- Battery
        |     +-- Temperature
        |
        +-- Operating System
        |     +-- Windows Information
        |     +-- Services
        |     +-- Startup Programs
        |     +-- Architecture
        |     +-- Environment Variables
        |
        +-- Processes
        |     +-- Running Processes
        |     +-- CPU Processes
        |     +-- RAM Processes
        |     +-- Process Search
        |     +-- Process Termination
        |
        +-- Storage
        |     +-- Disk Usage
        |     +-- Folder Size
        |     +-- File Counter
        |     +-- File Extensions
        |     +-- Large Files
        |     +-- Duplicate Files
        |     +-- Temporary Files
        |
        +-- Network
        |     +-- IP Address
        |     +-- Network Interfaces
        |     +-- DNS
        |     +-- Connections
        |     +-- Internet Test
        |     +-- Ping
        |     +-- MAC Address
        |
        +-- Performance
        |     +-- CPU Usage
        |     +-- RAM Usage
        |     +-- Disk Activity
        |     +-- Resource Monitor
        |     +-- Health Score
        |
        +-- Reports
              +-- Quick Scan
              +-- Checklist
              +-- Full Report
              +-- Saved Report
```

---

# Updated Purpose

The purpose of this project is to create a beginner-friendly command-line application that demonstrates how Python can interact with a computer's operating system.

Instead of only displaying basic computer information, the program now provides several diagnostic categories that allow users to inspect **hardware resources, software information, running processes, network connections, storage usage, files, folders, and system performance**.

The project also demonstrates how Python can interact with operating-system commands through `subprocess`, work with files and directories using `os`, inspect processes using `psutil`, and generate diagnostic reports using standard Python file handling.

The project is designed mainly for **learning and basic system inspection**, rather than replacing professional diagnostic software.

---

# Safety Notes

Most features of the program only read and display information.

However, the **Process Termination** feature can affect currently running applications.

Users should:

* Check the process name before terminating it.
* Avoid terminating important Windows system processes.
* Avoid terminating processes they do not recognize.
* Use administrator permissions only when necessary.
* Understand that terminating some processes can cause applications or system components to stop working.

The program does **not automatically delete files**, clean temporary files, modify system settings, or change hardware configurations.

---

# Future Improvements

Possible future additions include:

* Real-time CPU graphs
* Real-time RAM graphs
* Real-time disk graphs
* Internet speed testing
* Network download/upload monitoring
* CPU temperature monitoring improvements
* GPU temperature monitoring
* GPU utilization monitoring
* Disk health monitoring
* SMART disk information
* File hash comparison
* More accurate duplicate-file detection
* Process filtering
* Process auto-refresh
* Process resource history
* Network adapter statistics
* Automatic health recommendations
* CSV report export
* JSON report export
* More detailed hardware inventory
* Diagnostic history
* Automatic report timestamps
* System performance logging
* Automatic diagnostic summaries
* More advanced Windows startup information
* Graphical user interface version
* Scheduled diagnostic scans

---

# Version

```text
PC Diagnostic Tool
Version: 3.1
```

Version 3.1 includes expanded **hardware monitoring, process management, file analysis, storage analysis, network diagnostics, performance monitoring, Windows system tools, and diagnostic features**.

---

# Author

**Jose Navoa**

Aspiring Information Technology Student

Created as a Python learning and system diagnostic project.
