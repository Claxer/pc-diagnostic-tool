import platform
import psutil
import socket
import os
import sys
import subprocess
import getpass
import uuid
import shutil
import tempfile
from datetime import datetime, timedelta


# =========================================================
# SYSTEM INFORMATION
# =========================================================

def show_system_information():
    print("\n---------- SYSTEM INFORMATION ----------")
    print("Operating System :", platform.system())
    print("System Version   :", platform.version())
    print("Computer Name    :", socket.gethostname())
    print("Machine          :", platform.machine())
    print("Architecture     :", platform.architecture()[0])
    print("Processor        :", platform.processor())


# =========================================================
# CPU INFORMATION
# =========================================================

def show_cpu_information():
    print("\n---------- CPU INFORMATION ----------")
    print("CPU Cores        :", psutil.cpu_count(logical=False))
    print("Logical CPUs     :", psutil.cpu_count(logical=True))
    print("CPU Usage        :", psutil.cpu_percent(interval=1), "%")

    frequency = psutil.cpu_freq()

    if frequency:
        print("CPU Frequency    :", round(frequency.current, 2), "MHz")
        print("Minimum Frequency:", round(frequency.min, 2), "MHz")
        print("Maximum Frequency:", round(frequency.max, 2), "MHz")


# =========================================================
# RAM INFORMATION
# =========================================================

def show_ram_information():
    memory = psutil.virtual_memory()

    print("\n---------- RAM INFORMATION ----------")
    print("Total RAM        :", round(memory.total / (1024 ** 3), 2), "GB")
    print("Used RAM         :", round(memory.used / (1024 ** 3), 2), "GB")
    print("Available RAM    :", round(memory.available / (1024 ** 3), 2), "GB")
    print("RAM Usage        :", memory.percent, "%")


# =========================================================
# DISK INFORMATION
# =========================================================

def show_disk_information():
    print("\n---------- DISK INFORMATION ----------")

    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            print("\nDrive :", partition.device)
            print("Total :", round(usage.total / (1024 ** 3), 2), "GB")
            print("Used  :", round(usage.used / (1024 ** 3), 2), "GB")
            print("Free  :", round(usage.free / (1024 ** 3), 2), "GB")
            print("Usage :", usage.percent, "%")

        except PermissionError:
            print("Unable to access:", partition.device)


# =========================================================
# NETWORK INFORMATION
# =========================================================

def show_network_information():
    print("\n---------- NETWORK INFORMATION ----------")

    computer_name = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(computer_name)
    except socket.error:
        ip_address = "Unavailable"

    print("Computer Name :", computer_name)
    print("IP Address    :", ip_address)


# =========================================================
# BATTERY INFORMATION
# =========================================================

def show_battery_information():
    print("\n---------- BATTERY INFORMATION ----------")

    battery = psutil.sensors_battery()

    if battery is None:
        print("Battery information is not available.")
    else:
        print("Battery Level :", battery.percent, "%")

        if battery.power_plugged:
            print("Power Status  : Plugged In")
        else:
            print("Power Status  : Running on Battery")

        if battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            if battery.secsleft != psutil.POWER_TIME_UNKNOWN:
                remaining = str(timedelta(seconds=battery.secsleft))
                print("Time Left     :", remaining)


# =========================================================
# SYSTEM UPTIME
# =========================================================

def show_uptime():
    print("\n---------- SYSTEM UPTIME ----------")

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    current_time = datetime.now()

    uptime = current_time - boot_time

    print("Boot Time     :", boot_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Current Time  :", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("System Uptime :", uptime)


# =========================================================
# HEALTH CHECK
# =========================================================

def health_check():
    print("\n---------- SYSTEM HEALTH CHECK ----------")

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    print("CPU Usage :", cpu_usage, "%")
    print("RAM Usage :", memory_usage, "%")

    if cpu_usage >= 90:
        print("CPU Status : High Usage")
    elif cpu_usage >= 70:
        print("CPU Status : Moderate Usage")
    else:
        print("CPU Status : Normal")

    if memory_usage >= 90:
        print("RAM Status : High Usage")
    elif memory_usage >= 70:
        print("RAM Status : Moderate Usage")
    else:
        print("RAM Status : Normal")

    print("\nHealth Check Complete.")


# =========================================================
# RUNNING PROCESSES
# =========================================================

def show_running_processes():
    print("\n---------- RUNNING PROCESSES ----------")

    processes = []

    for process in psutil.process_iter(["pid", "name", "status"]):
        try:
            info = process.info
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    print("Total Processes :", len(processes))
    print("\nPID       NAME                         STATUS")
    print("-----------------------------------------------")

    for process in processes[:20]:
        print(
            str(process["pid"]).ljust(10),
            str(process["name"])[:27].ljust(28),
            process["status"]
        )

    if len(processes) > 20:
        print("\nShowing the first 20 processes.")


# =========================================================
# TOP CPU PROCESSES
# =========================================================

def show_top_cpu_processes():
    print("\n---------- TOP CPU PROCESSES ----------")

    processes = []

    for process in psutil.process_iter(["pid", "name"]):
        try:
            cpu = process.cpu_percent(interval=0.1)

            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "cpu": cpu
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes.sort(key=lambda process: process["cpu"], reverse=True)

    print("\nPID       CPU %      NAME")
    print("-----------------------------------------------")

    for process in processes[:10]:
        print(
            str(process["pid"]).ljust(10),
            str(round(process["cpu"], 2)).ljust(10),
            str(process["name"])[:30]
        )


# =========================================================
# TOP RAM PROCESSES
# =========================================================

def show_top_ram_processes():
    print("\n---------- TOP RAM PROCESSES ----------")

    processes = []

    for process in psutil.process_iter(["pid", "name", "memory_percent"]):
        try:
            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "memory": process.info["memory_percent"]
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes.sort(key=lambda process: process["memory"], reverse=True)

    print("\nPID       RAM %      NAME")
    print("-----------------------------------------------")

    for process in processes[:10]:
        print(
            str(process["pid"]).ljust(10),
            str(round(process["memory"], 2)).ljust(10),
            str(process["name"])[:30]
        )


# =========================================================
# NETWORK CONNECTIONS
# =========================================================

def show_network_connections():
    print("\n---------- NETWORK CONNECTIONS ----------")

    try:
        connections = psutil.net_connections()

        print("Active Connections :", len(connections))
        print("\nSTATUS       LOCAL ADDRESS")
        print("-----------------------------------------------")

        for connection in connections[:15]:
            status = connection.status

            if connection.laddr:
                local_address = str(connection.laddr)
            else:
                local_address = "Unknown"

            print(
                str(status).ljust(13),
                local_address
            )

        if len(connections) > 15:
            print("\nShowing the first 15 connections.")

    except psutil.AccessDenied:
        print("Access denied. Run the program as administrator to see all connections.")


# =========================================================
# PYTHON INFORMATION
# =========================================================

def show_python_information():
    print("\n---------- PYTHON INFORMATION ----------")

    print("Python Version :", platform.python_version())
    print("Python Path    :", sys.executable)
    print("Python Build   :", platform.python_build()[0])
    print("Python Compiler:", platform.python_compiler())


# =========================================================
# PERFORMANCE SUMMARY
# =========================================================

def show_performance_summary():
    print("\n---------- PERFORMANCE SUMMARY ----------")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(os.path.abspath(os.sep))

    print("CPU Usage  :", cpu, "%")
    print("RAM Usage  :", memory.percent, "%")
    print("Disk Usage :", disk.percent, "%")

    print("\nPerformance Status:")

    if cpu >= 90:
        print("- CPU usage is very high.")
    elif cpu >= 70:
        print("- CPU usage is moderately high.")
    else:
        print("- CPU usage is normal.")

    if memory.percent >= 90:
        print("- RAM usage is very high.")
    elif memory.percent >= 70:
        print("- RAM usage is moderately high.")
    else:
        print("- RAM usage is normal.")

    if disk.percent >= 90:
        print("- Disk space is almost full.")
    elif disk.percent >= 75:
        print("- Disk space is getting full.")
    else:
        print("- Disk space is normal.")


# =========================================================
# SYSTEM HEALTH SCORE
# =========================================================

def calculate_health_score():
    print("\n---------- SYSTEM HEALTH SCORE ----------")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage(os.path.abspath(os.sep)).percent

    cpu_score = max(0, 100 - cpu)
    memory_score = max(0, 100 - memory)
    disk_score = max(0, 100 - disk)

    score = (cpu_score + memory_score + disk_score) / 3

    print("CPU Score  :", round(cpu_score, 2))
    print("RAM Score  :", round(memory_score, 2))
    print("Disk Score :", round(disk_score, 2))
    print("\nOverall Health Score :", round(score, 2), "%")

    if score >= 80:
        print("Status : Good")
    elif score >= 60:
        print("Status : Fair")
    else:
        print("Status : Needs Attention")


# =========================================================
# FOLDER SIZE CHECKER
# =========================================================

def check_folder_size():
    print("\n---------- FOLDER SIZE CHECKER ----------")

    folder = input("Enter folder path: ")

    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    if not os.path.isdir(folder):
        print("The selected path is not a folder.")
        return

    total_size = 0

    for root, directories, files in os.walk(folder):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
            except (PermissionError, FileNotFoundError):
                pass

    size_mb = total_size / (1024 ** 2)
    size_gb = total_size / (1024 ** 3)

    print("\nFolder :", folder)
    print("Size   :", round(size_mb, 2), "MB")
    print("Size   :", round(size_gb, 2), "GB")


# =========================================================
# GPU INFORMATION
# =========================================================

def show_gpu_information():
    print("\n---------- GPU INFORMATION ----------")

    try:
        result = subprocess.run(
            ["wmic", "path", "win32_VideoController", "get",
             "Name,AdapterRAM,DriverVersion"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)
        else:
            print("GPU information could not be retrieved.")

    except FileNotFoundError:
        print("GPU information command is not available on this system.")


# =========================================================
# MOTHERBOARD INFORMATION
# =========================================================

def show_motherboard_information():
    print("\n---------- MOTHERBOARD INFORMATION ----------")

    try:
        result = subprocess.run(
            ["wmic", "baseboard", "get", "Manufacturer,Product,SerialNumber"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)
        else:
            print("Motherboard information could not be retrieved.")

    except FileNotFoundError:
        print("Motherboard information command is not available.")


# =========================================================
# USER INFORMATION
# =========================================================

def show_user_information():
    print("\n---------- USER INFORMATION ----------")

    print("Username       :", getpass.getuser())
    print("Home Directory :", os.path.expanduser("~"))
    print("Computer Name  :", socket.gethostname())


# =========================================================
# ENVIRONMENT VARIABLES
# =========================================================

def show_environment_variables():
    print("\n---------- ENVIRONMENT VARIABLES ----------")

    variables = os.environ

    print("Total Variables :", len(variables))
    print()

    for key, value in list(variables.items())[:30]:
        print(key, "=", value)

    if len(variables) > 30:
        print("\nShowing the first 30 environment variables.")


# =========================================================
# INTERNET CONNECTION TEST
# =========================================================

def test_internet_connection():
    print("\n---------- INTERNET CONNECTION TEST ----------")

    host = "google.com"

    try:
        start_time = datetime.now()

        socket.create_connection((host, 80), timeout=5)

        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()

        print("Connection Status : Connected")
        print("Test Server       :", host)
        print("Response Time     :", round(response_time * 1000, 2), "ms")

    except OSError:
        print("Connection Status : No Internet Connection")


# =========================================================
# PING TEST
# =========================================================

def ping_test():
    print("\n---------- PING TEST ----------")

    host = input("Enter website or IP address: ")

    if not host:
        print("No address entered.")
        return

    try:
        result = subprocess.run(
            ["ping", "-n", "4", host],
            capture_output=True,
            text=True
        )

        print(result.stdout)

    except Exception as error:
        print("Ping failed:", error)


# =========================================================
# MAC ADDRESS
# =========================================================

def show_mac_address():
    print("\n---------- MAC ADDRESS ----------")

    mac = uuid.getnode()

    mac_address = ":".join(
        f"{(mac >> element) & 0xff:02x}"
        for element in range(40, -1, -8)
    )

    print("MAC Address :", mac_address.upper())


# =========================================================
# STORAGE SUMMARY
# =========================================================

def show_storage_summary():
    print("\n---------- STORAGE SUMMARY ----------")

    partitions = psutil.disk_partitions()
    total_storage = 0
    total_used = 0
    total_free = 0

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            total_storage += usage.total
            total_used += usage.used
            total_free += usage.free

        except (PermissionError, FileNotFoundError):
            pass

    print("Total Storage :", round(total_storage / (1024 ** 3), 2), "GB")
    print("Used Storage  :", round(total_used / (1024 ** 3), 2), "GB")
    print("Free Storage  :", round(total_free / (1024 ** 3), 2), "GB")


# =========================================================
# LARGE FILE FINDER
# =========================================================

def find_large_files():
    print("\n---------- LARGE FILE FINDER ----------")

    folder = input("Enter folder path: ")

    if not os.path.isdir(folder):
        print("Invalid folder.")
        return

    try:
        minimum_size = float(
            input("Minimum file size in MB: ")
        )

        minimum_bytes = minimum_size * 1024 * 1024

    except ValueError:
        print("Please enter a valid number.")
        return

    large_files = []

    print("\nSearching...")

    for root, directories, files in os.walk(folder):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)

                if file_size >= minimum_bytes:
                    large_files.append(
                        (file_path, file_size)
                    )

            except (PermissionError, FileNotFoundError):
                pass

    large_files.sort(key=lambda item: item[1], reverse=True)

    if not large_files:
        print("No large files were found.")
        return

    print("\nLarge Files:")
    print("-----------------------------------------------")

    for file_path, file_size in large_files[:20]:
        size_mb = file_size / (1024 ** 2)

        print(round(size_mb, 2), "MB -", file_path)

    if len(large_files) > 20:
        print("\nShowing the first 20 large files.")


# =========================================================
# TEMPORARY FILE SIZE
# =========================================================

def check_temp_folder():
    print("\n---------- TEMPORARY FILE CHECK ----------")

    temp_folder = tempfile.gettempdir()

    print("Temp Folder :", temp_folder)

    total_size = 0
    file_count = 0

    for root, directories, files in os.walk(temp_folder):
        for file in files:
            try:
                file_path = os.path.join(root, file)

                total_size += os.path.getsize(file_path)
                file_count += 1

            except (PermissionError, FileNotFoundError):
                pass

    print("Files Found :", file_count)
    print("Total Size  :", round(total_size / (1024 ** 2), 2), "MB")


# =========================================================
# BOOT INFORMATION
# =========================================================

def show_boot_information():
    print("\n---------- BOOT INFORMATION ----------")

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    current_time = datetime.now()

    uptime = current_time - boot_time

    print("Last Boot Time :", boot_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Current Time   :", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Uptime         :", uptime)


# =========================================================
# SYSTEM TEMPERATURE
# =========================================================

def show_temperature():
    print("\n---------- SYSTEM TEMPERATURE ----------")

    try:
        temperatures = psutil.sensors_temperatures()

        if not temperatures:
            print("Temperature information is not available.")
            return

        for name, entries in temperatures.items():
            print("\nSensor:", name)

            for entry in entries:
                print(
                    "Temperature:",
                    entry.current,
                    "°C"
                )

    except AttributeError:
        print("Temperature sensors are not supported.")


# =========================================================
# DISK SPACE WARNING
# =========================================================

def disk_space_warning():
    print("\n---------- DISK SPACE WARNING ----------")

    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            print("\nDrive :", partition.device)
            print("Usage :", usage.percent, "%")

            if usage.percent >= 90:
                print("Warning: Disk is almost full!")

            elif usage.percent >= 75:
                print("Warning: Disk space is getting low.")

            else:
                print("Status: Disk space is okay.")

        except (PermissionError, FileNotFoundError):
            pass


# =========================================================
# QUICK DIAGNOSTIC SCAN
# =========================================================

def quick_diagnostic_scan():
    print("\n========================================")
    print("         QUICK DIAGNOSTIC SCAN")
    print("========================================")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(os.path.abspath(os.sep))

    print("\nCPU Usage :", cpu, "%")
    print("RAM Usage :", memory.percent, "%")
    print("Disk Usage:", disk.percent, "%")

    print("\nChecking system status...")

    issues = 0

    if cpu >= 90:
        print("[WARNING] CPU usage is very high.")
        issues += 1
    else:
        print("[OK] CPU usage is normal.")

    if memory.percent >= 90:
        print("[WARNING] RAM usage is very high.")
        issues += 1
    else:
        print("[OK] RAM usage is normal.")

    if disk.percent >= 90:
        print("[WARNING] Disk space is almost full.")
        issues += 1
    else:
        print("[OK] Disk space is sufficient.")

    battery = psutil.sensors_battery()

    if battery:
        if battery.percent <= 20 and not battery.power_plugged:
            print("[WARNING] Battery level is low.")
            issues += 1
        else:
            print("[OK] Battery level is acceptable.")

    print("\n----------------------------------------")

    if issues == 0:
        print("No major problems detected.")
    else:
        print("Potential issues detected:", issues)

    print("Quick scan complete.")


# =========================================================
# SYSTEM SUMMARY
# =========================================================

def show_system_summary():
    print("\n========================================")
    print("          SYSTEM SUMMARY")
    print("========================================")

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(os.path.abspath(os.sep))

    print("Computer Name :", socket.gethostname())
    print("Operating System:", platform.system())
    print("OS Version     :", platform.version())
    print("Processor      :", platform.processor())
    print("CPU Cores      :", psutil.cpu_count(logical=False))
    print("Logical CPUs   :", psutil.cpu_count(logical=True))
    print("CPU Usage      :", psutil.cpu_percent(interval=1), "%")
    print("Total RAM      :", round(memory.total / (1024 ** 3), 2), "GB")
    print("RAM Usage      :", memory.percent, "%")
    print("System Disk    :", round(disk.total / (1024 ** 3), 2), "GB")
    print("Disk Usage     :", disk.percent, "%")
    print("Python Version :", platform.python_version())


# =========================================================
# SAVE DIAGNOSTIC REPORT
# =========================================================

def save_diagnostic_report():
    print("\n---------- SAVE DIAGNOSTIC REPORT ----------")

    filename = "diagnostic_report.txt"

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(os.path.abspath(os.sep))

    report = []

    report.append("========================================")
    report.append("       PC DIAGNOSTIC REPORT")
    report.append("========================================")
    report.append("")
    report.append("System Information")
    report.append("------------------")
    report.append("Operating System : " + platform.system())
    report.append("System Version   : " + platform.version())
    report.append("Computer Name    : " + socket.gethostname())
    report.append("Architecture     : " + platform.architecture()[0])
    report.append("Processor        : " + platform.processor())
    report.append("")
    report.append("Performance")
    report.append("-----------")
    report.append("CPU Usage  : " + str(cpu) + "%")
    report.append("RAM Usage  : " + str(memory.percent) + "%")
    report.append("Disk Usage : " + str(disk.percent) + "%")
    report.append("")
    report.append("Python Version : " + platform.python_version())
    report.append("Username       : " + getpass.getuser())
    report.append("")
    report.append(
        "Report Created : "
        + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    report.append("========================================")

    with open(filename, "w") as file:
        for line in report:
            file.write(line + "\n")

    print("Diagnostic report saved as:", filename)


# =========================================================
# HELP
# =========================================================

def show_help():
    print("\n---------- HELP ----------")
    print("PC Diagnostic Tool")
    print()
    print("Use the menu numbers to select a diagnostic function.")
    print("The tool checks basic hardware, software,")
    print("network, storage, and system information.")
    print()
    print("Some functions may require administrator access.")
    print("Some hardware information may not be available")
    print("depending on your computer.")


# =========================================================
# ABOUT
# =========================================================

def show_about():
    print("\n========================================")
    print("          ABOUT PC DIAGNOSTIC TOOL")
    print("========================================")
    print("A beginner-friendly Python PC diagnostic program.")
    print()
    print("Created using Python and psutil.")
    print("Purpose: Practice functions, loops, conditions,")
    print("user input, system information, and file handling.")
    print()
    print("Version: 2.0")


# =========================================================
# FULL DIAGNOSTIC REPORT
# =========================================================

def full_diagnostic_report():
    print("\n========================================")
    print("       FULL DIAGNOSTIC REPORT")
    print("========================================")

    show_system_information()
    show_cpu_information()
    show_ram_information()
    show_disk_information()
    show_network_information()
    show_battery_information()
    show_uptime()
    health_check()
    show_performance_summary()
    calculate_health_score()

    print("\n========================================")
    print("       DIAGNOSTIC COMPLETE")
    print("========================================")


# =========================================================
# MENU
# =========================================================

def show_menu():
    print("\n========================================")
    print("          PC DIAGNOSTIC TOOL")
    print("========================================")
    print("1.  System Information")
    print("2.  CPU Information")
    print("3.  RAM Information")
    print("4.  Disk Information")
    print("5.  Network Information")
    print("6.  Battery Information")
    print("7.  System Uptime")
    print("8.  System Health Check")
    print("9.  Full Diagnostic Report")
    print("10. Running Processes")
    print("11. Top CPU Processes")
    print("12. Top RAM Processes")
    print("13. Network Connections")
    print("14. Python Information")
    print("15. Performance Summary")
    print("16. System Health Score")
    print("17. Folder Size Checker")
    print("18. Save Diagnostic Report")
    print("19. GPU Information")
    print("20. Motherboard Information")
    print("21. User Information")
    print("22. Environment Variables")
    print("23. Internet Connection Test")
    print("24. Ping Test")
    print("25. MAC Address")
    print("26. Storage Summary")
    print("27. Large File Finder")
    print("28. Temporary File Checker")
    print("29. Boot Information")
    print("30. System Temperature")
    print("31. Disk Space Warning")
    print("32. Quick Diagnostic Scan")
    print("33. System Summary")
    print("34. Help")
    print("35. About")
    print("0.  Exit")
    print("========================================")


# =========================================================
# MAIN PROGRAM
# =========================================================

def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            show_system_information()

        elif choice == "2":
            show_cpu_information()

        elif choice == "3":
            show_ram_information()

        elif choice == "4":
            show_disk_information()

        elif choice == "5":
            show_network_information()

        elif choice == "6":
            show_battery_information()

        elif choice == "7":
            show_uptime()

        elif choice == "8":
            health_check()

        elif choice == "9":
            full_diagnostic_report()

        elif choice == "10":
            show_running_processes()

        elif choice == "11":
            show_top_cpu_processes()

        elif choice == "12":
            show_top_ram_processes()

        elif choice == "13":
            show_network_connections()

        elif choice == "14":
            show_python_information()

        elif choice == "15":
            show_performance_summary()

        elif choice == "16":
            calculate_health_score()

        elif choice == "17":
            check_folder_size()

        elif choice == "18":
            save_diagnostic_report()

        elif choice == "19":
            show_gpu_information()

        elif choice == "20":
            show_motherboard_information()

        elif choice == "21":
            show_user_information()

        elif choice == "22":
            show_environment_variables()

        elif choice == "23":
            test_internet_connection()

        elif choice == "24":
            ping_test()

        elif choice == "25":
            show_mac_address()

        elif choice == "26":
            show_storage_summary()

        elif choice == "27":
            find_large_files()

        elif choice == "28":
            check_temp_folder()

        elif choice == "29":
            show_boot_information()

        elif choice == "30":
            show_temperature()

        elif choice == "31":
            disk_space_warning()

        elif choice == "32":
            quick_diagnostic_scan()

        elif choice == "33":
            show_system_summary()

        elif choice == "34":
            show_help()

        elif choice == "35":
            show_about()

        elif choice == "0":
            print("\nThank you for using PC Diagnostic Tool!")
            break

        else:
            print("\nInvalid choice. Please select a number from 0 to 35.")


# =========================================================
# START PROGRAM
# =========================================================

main()
