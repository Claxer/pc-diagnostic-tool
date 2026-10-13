# PC Diagnostic Tool

A Python-based **PC Diagnostic Tool** designed to inspect, monitor, and analyze computer hardware, software, system resources, running processes, storage, network connections, and overall system performance.

The project includes two editions:

* **Command-Line Edition (Version 3.1)** — A terminal-based diagnostic application with 69 numbered tools for system inspection, hardware monitoring, process management, file analysis, network diagnostics, and report generation.
* **NEXUS GUI Ultimate Edition (Version 5.0.0)** — A modern graphical desktop application featuring a dashboard, diagnostic scans, process management, hardware information, network monitoring, folder analysis, and report exporting.

This project was developed as a beginner-friendly Python learning project to demonstrate how Python can interact with the operating system through built-in modules and external libraries.

---

## Table of Contents

* [Features](#features)
* [Command-Line Edition](#command-line-edition)
* [NEXUS GUI Ultimate Edition](#nexus-gui-ultimate-edition)
* [GUI Features](#gui-features)
* [Installation](#installation)
* [How to Run](#how-to-run)
* [Report Export](#report-export)
* [Python Concepts Used](#python-concepts-used)
* [Libraries and Modules](#libraries-and-modules)
* [Project Structure](#project-structure)
* [System Compatibility](#system-compatibility)
* [Safety Notes](#safety-notes)
* [Limitations](#limitations)
* [Future Improvements](#future-improvements)
* [Author](#author)

---

## Features

The project provides diagnostic and monitoring tools organized into several categories.

* System and operating system information
* CPU and memory monitoring
* Storage and disk activity analysis
* Network diagnostics
* Battery information and health checks
* Running process inspection and management
* Windows services and startup programs
* Python environment and package checking
* File and folder analysis
* System health checks
* Performance monitoring
* Diagnostic report generation
* Resource history logging
* Graphical dashboard and diagnostic interface

The available features depend on which edition is being used.

---

# Command-Line Edition

**Version 3.1**

The original command-line edition provides 69 numbered tools, plus an exit option.

### System Information

* System information and summary
* System architecture details
* Current date and time
* Boot information
* System uptime
* Operating system and Python information

### CPU and Memory

* CPU information
* CPU load per core
* CPU load average
* RAM information
* Detailed RAM information
* Virtual memory and swap usage
* System temperature information when supported

### Storage and File Analysis

* Disk information
* Disk activity statistics
* Disk speed snapshot
* Storage summary
* Disk space warnings
* Folder size checker
* Folder file counter
* Large file finder
* File extension analyzer
* Duplicate file finder
* Temporary file checker

### Network Diagnostics

* Network information
* Network interface details
* Network traffic statistics
* Network speed snapshot
* Network packet statistics
* Network connections
* Hostname and DNS information
* Internet connection test
* Ping test
* MAC address detection

### Battery Monitoring

* Battery information
* Battery percentage
* Charging status
* Estimated remaining time when available
* Detailed battery health status

### Process Management

* Running process listing
* Process count summary
* Top CPU processes
* Top RAM processes
* Process search
* Process termination
* Detailed process information by PID

### Windows System Tools

* GPU information
* Motherboard information
* Windows services
* Startup programs
* Recent Windows System event logs
* Installed applications list

Some hardware information depends on operating system support, installed utilities, and available hardware sensors.

### Python Environment

* Python information
* Python installation details
* Python build and compiler information
* Python package checking

### Diagnostics and Reports

* Health check
* Performance summary
* System health score
* Quick diagnostic scan
* Diagnostic checklist
* System resource snapshot
* Continuous resource monitoring
* Full diagnostic report
* Save diagnostic report
* Record resource history
* Export system snapshot

### Additional Tools

* User information
* User session information
* Environment variables
* File search by name
* Clear terminal screen
* Help and application information

---

# NEXUS GUI Ultimate Edition

**Version 5.0.0**

NEXUS is the graphical desktop edition of the PC Diagnostic Tool. It uses Python and CustomTkinter to provide a modern interface for inspecting computer resources and performing basic diagnostic tasks.

The interface uses a dark theme, sidebar navigation, dashboard cards, progress indicators, and organized diagnostic pages.

## GUI Features

### 1. Overview Dashboard

Provides a quick summary of the computer's current resource usage.

* CPU usage percentage
* RAM usage percentage
* Storage usage
* Running process count
* Resource usage indicators
* System health signals
* Quick overview of important system resources

### 2. Diagnostic Scan

Performs a basic rule-based scan of selected system resources.

* Checks CPU usage
* Checks memory usage
* Checks disk space
* Checks battery status when available
* Identifies resource usage that exceeds configured thresholds
* Displays diagnostic warnings and results

The scan provides basic indicators and is not a replacement for professional hardware diagnostics.

### 3. Process Manager

Allows users to inspect and manage running processes.

* Lists running processes
* Searches processes by name or process ID
* Displays process IDs and names
* Displays memory usage
* Sorts processes by memory consumption
* Allows a selected process to be terminated
* Requests confirmation before terminating a process
* Handles common process access and availability errors

**Important:** Terminating a process may cause an application or system component to stop working. Always verify the selected process before confirming.

### 4. Hardware and Operating System Information

Displays useful information about the computer's software environment and hardware resources.

* Operating system information
* System architecture
* Processor information
* Python version
* Memory information
* General system details

The amount of information available depends on the operating system and hardware.

### 5. Network Diagnostics

Provides basic information about network interfaces and connectivity.

* Network interface information
* Network traffic counters
* Data sent and received
* Basic HTTPS connectivity test
* Network connection troubleshooting information

The connectivity test checks whether a connection can be established. It does not provide a complete internet speed test.

### 6. Folder Analyzer

Analyzes a selected folder and its contents.

* Counts files
* Counts subfolders
* Calculates total folder size
* Analyzes file extensions
* Summarizes file types
* Helps users understand how storage is distributed within a folder

Results depend on folder permissions and the files that can be accessed.

### 7. Diagnostic Report Export

Allows users to save diagnostic information for later reference.

Supported export formats:

* **TXT** — Readable text reports
* **HTML** — Reports that can be opened in a web browser
* **CSV** — Structured data suitable for spreadsheets

Reports are saved locally in the `PCDiagnosticReports` folder inside the user's home directory.

---

# Installation

## Requirements

The GUI edition requires:

* Python 3.10 or newer recommended
* CustomTkinter
* psutil

Python versions compatible with the installed dependencies may also work.

## 1. Clone the Repository

```bash
git clone https://github.com/Claxer/PC-Diagnostic-Tool.git
```

Replace the repository URL with your actual GitHub repository URL if it differs.

## 2. Open the Project Folder

Open the downloaded project in PyCharm, Visual Studio Code, or another Python IDE.

## 3. Install Dependencies

Open a terminal in the project directory and run:

```bash
python -m pip install -r requirements.txt
```

If the `python` command is unavailable on Windows, try:

```bash
py -m pip install -r requirements.txt
```

---

# How to Run

## NEXUS GUI Ultimate Edition

Run the following command from the folder containing `main.py`:

```bash
python main.py
```

Alternatively, on Windows:

```bash
py main.py
```

The graphical application should open in a separate desktop window.

## Command-Line Edition

Run the Python file containing the original command-line menu:

```bash
python your_cli_filename.py
```

Replace `your_cli_filename.py` with the actual filename of the command-line program.

The command-line and GUI editions have separate implementations. Their features and entry-point filenames may differ.

---

# Report Export

The GUI edition can export diagnostic information in several formats.

| Format | Purpose                                             |
| ------ | --------------------------------------------------- |
| TXT    | Simple, readable diagnostic reports                 |
| HTML   | Reports viewable in a web browser                   |
| CSV    | Structured information for spreadsheet applications |

The command-line edition also includes resource history logging and system snapshot export.

These reports can help users review system information, compare recorded measurements manually, and keep diagnostic records.

---

# Python Concepts Used

This project demonstrates several fundamental and intermediate Python programming concepts.

* Variables and data types
* Strings and string methods
* Integers and floating-point numbers
* Lists and dictionaries
* Functions and function calls
* Conditional statements (`if`, `elif`, `else`)
* Loops (`for` and `while`)
* User input
* Exception handling (`try` and `except`)
* File handling
* Directory traversal
* Sorting and filtering data
* Modules and imports
* Date and time handling
* Operating system interaction
* Process inspection and management
* Subprocess commands
* Network connectivity checks
* CSV and HTML report generation
* Graphical user interfaces
* Event-driven programming
* External library integration

---

# Libraries and Modules

## CustomTkinter

Used by the GUI edition to create the desktop interface, navigation sidebar, dashboard, buttons, frames, and other graphical components.

## psutil

Used to retrieve system and process information, including:

* CPU usage
* Memory usage
* Disk usage
* Disk activity
* Network statistics
* Running processes
* Battery information when supported
* System uptime

## Built-in Python Modules

Depending on the edition and feature, the project uses modules such as:

* `os` — File and directory operations
* `sys` — Python runtime information
* `platform` — Operating system and architecture information
* `socket` — Network and hostname information
* `subprocess` — Running operating system commands
* `datetime` — Dates and timestamps
* `csv` — CSV report generation
* `html` — HTML-related utilities
* `pathlib` — File and folder path handling
* `tempfile` — Temporary directory information
* `uuid` — System-related identifier utilities

Not every module is used by every edition.

---

# Project Structure

The exact files may vary depending on the version of the project.

```text
PC-Diagnostic-Tool/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── PCDiagnosticReports/
    ├── diagnostic_report.txt
    ├── diagnostic_report.html
    └── diagnostic_report.csv
```

The `PCDiagnosticReports` folder is used for exported reports by the GUI edition. It is normally created when reports are saved, rather than being required before the application starts.

The command-line edition may use a different Python filename and may generate additional CSV or text files for resource history and system snapshots.

---

# System Compatibility

The project is primarily intended for Windows computers, but some general monitoring features may work on other operating systems.

| Feature                        | Compatibility                                    |
| ------------------------------ | ------------------------------------------------ |
| CPU and RAM monitoring         | Depends on platform and library support          |
| Disk usage                     | Depends on available drives and permissions      |
| Process inspection             | Depends on process permissions                   |
| Process termination            | May require additional permissions               |
| Battery information            | Requires supported battery hardware              |
| Windows services               | Windows-specific                                 |
| Windows event logs             | Windows-specific                                 |
| Installed application registry | Windows-specific                                 |
| Network diagnostics            | Requires available network interfaces            |
| Hardware sensor information    | Depends on hardware and operating system support |

Some diagnostic information may be unavailable on certain computers.

---

# Safety Notes

Most features inspect and display system information. However, process termination and some system-level diagnostic operations require caution.

Users should:

* Verify a process before terminating it.
* Avoid terminating unfamiliar Windows system processes.
* Avoid running the application with administrator privileges unless necessary.
* Understand that some processes cannot be inspected because of permission restrictions.
* Avoid interpreting basic diagnostic warnings as proof of hardware failure.
* Review exported reports before sharing them, since they may contain information about the computer or user environment.

The application is intended for learning and basic system inspection. It should not be treated as a replacement for professional repair tools, antivirus software, or comprehensive hardware diagnostics.

---

# Limitations

The current editions have different capabilities.

### Command-Line Edition

* Uses a text-based menu.
* Some features are specific to Windows.
* Hardware sensor information may not be available on every computer.
* Duplicate file detection based only on file size can identify possible duplicates but cannot confirm identical contents.
* Resource monitoring and reporting depend on the availability of system information.

### NEXUS GUI Ultimate Edition

* Provides a graphical interface for selected diagnostic features rather than all 69 command-line tools.
* Uses basic rule-based diagnostic thresholds.
* Does not provide a complete hardware stress test.
* Does not guarantee accurate GPU, motherboard, or temperature readings on all computers.
* Network traffic counters are not equivalent to an internet speed test.
* Process termination may fail when permissions are insufficient or the process has already closed.
* Historical comparisons and advanced performance charts are not included in the current feature set.

---

# Future Improvements

Possible future enhancements include:

* Real-time CPU usage graphs
* Real-time RAM usage graphs
* Disk activity charts
* Historical performance comparisons
* Automatic diagnostic history
* Advanced hardware inventory
* Improved GPU information and utilization monitoring
* CPU and GPU temperature monitoring
* Disk health and SMART information
* More accurate duplicate-file detection using file hashes
* Automatic process refresh
* Additional process filtering options
* Detailed network download and upload monitoring
* Internet speed testing
* More advanced health recommendations
* Scheduled diagnostic scans
* Additional report customization
* JSON report export
* More detailed battery health information
* Expanded graphical interface features
* Integration of more command-line tools into the GUI edition

---

# Version

**Project:** PC Diagnostic Tool

**Command-Line Edition:** Version 3.1

**NEXUS GUI Ultimate Edition:** Version 5.0.0

The project continues to evolve as additional diagnostic functions, monitoring features, and interface improvements are developed.

---

# Author

**Jose Navoa**

Aspiring Information Technology Student

Created as a Python learning project focused on system diagnostics, resource monitoring, process management, file analysis, network inspection, and desktop application development.
