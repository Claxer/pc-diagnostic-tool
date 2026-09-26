import platform
import psutil
import socket
import os
import sys
from datetime import datetime, timedelta


def show_system_information():
    print("\n---------- SYSTEM INFORMATION ----------")
    print("Operating System :", platform.system())
    print("System Version   :", platform.version())
    print("Computer Name    :", socket.gethostname())
    print("Machine          :", platform.machine())
    print("Architecture     :", platform.architecture()[0])
    print("Processor        :", platform.processor())


def show_cpu_information():
    print("\n---------- CPU INFORMATION ----------")
    print("CPU Cores        :", psutil.cpu_count(logical=False))
    print("Logical CPUs     :", psutil.cpu_count(logical=True))
    print("CPU Usage        :", psutil.cpu_percent(interval=1), "%")

    frequency = psutil.cpu_freq()

    if frequency:
        print("CPU Frequency    :", round(frequency.current, 2), "MHz")


def show_ram_information():
    memory = psutil.virtual_memory()

    print("\n---------- RAM INFORMATION ----------")
    print("Total RAM        :", round(memory.total / (1024 ** 3), 2), "GB")
    print("Used RAM         :", round(memory.used / (1024 ** 3), 2), "GB")
    print("Available RAM    :", round(memory.available / (1024 ** 3), 2), "GB")
    print("RAM Usage        :", memory.percent, "%")


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


def show_network_information():
    print("\n---------- NETWORK INFORMATION ----------")

    computer_name = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(computer_name)
    except socket.error:
        ip_address = "Unavailable"

    print("Computer Name :", computer_name)
    print("IP Address    :", ip_address)


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


def show_uptime():
    print("\n---------- SYSTEM UPTIME ----------")

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    current_time = datetime.now()

    uptime = current_time - boot_time

    print("Boot Time     :", boot_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Current Time  :", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("System Uptime :", uptime)


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


def show_python_information():
    print("\n---------- PYTHON INFORMATION ----------")

    print("Python Version :", platform.python_version())
    print("Python Path    :", sys.executable)
    print("Python Build   :", platform.python_build()[0])


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
    report.append("Report Created : " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    report.append("========================================")

    with open(filename, "w") as file:
        for line in report:
            file.write(line + "\n")

    print("Diagnostic report saved as:", filename)


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
    print("0.  Exit")
    print("========================================")


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

        elif choice == "0":
            print("\nThank you for using PC Diagnostic Tool!")
            break

        else:
            print("\nInvalid choice. Please select a number from 0 to 18.")


main()
