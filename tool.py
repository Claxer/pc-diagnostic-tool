import platform
import psutil
import socket
import os
import sys
import subprocess
import getpass
import uuid
import tempfile
import time
from datetime import datetime, timedelta


# =========================================================
# SYSTEM INFORMATION
# =========================================================

def show_system_information():
    print("\n---------- SYSTEM INFORMATION ----------")
    print("Operating System :", platform.system())
    print("System Version   :", platform.version())
    print("OS Release       :", platform.release())
    print("Computer Name    :", socket.gethostname())
    print("Machine          :", platform.machine())
    print("Architecture     :", platform.architecture()[0])
    print("Processor        :", platform.processor())
    print("Platform         :", platform.platform())


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
# CPU LOAD PER CORE
# =========================================================

def show_cpu_per_core():
    print("\n---------- CPU LOAD PER CORE ----------")

    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)

    for number, usage in enumerate(cpu_usage, start=1):
        print("CPU Core", number, ":", usage, "%")


# =========================================================
# CPU LOAD AVERAGE
# =========================================================

def show_cpu_load_average():
    print("\n---------- CPU LOAD AVERAGE ----------")

    try:
        load = os.getloadavg()

        print("1 Minute Load  :", round(load[0], 2))
        print("5 Minute Load  :", round(load[1], 2))
        print("15 Minute Load :", round(load[2], 2))

    except AttributeError:
        print("CPU load average is not available on this system.")

    except OSError:
        print("CPU load average could not be retrieved.")


# =========================================================
# RAM INFORMATION
# =========================================================

def show_ram_information():
    memory = psutil.virtual_memory()

    print("\n---------- RAM INFORMATION ----------")
    print("Total RAM        :", round(memory.total / (1024 ** 3), 2), "GB")
    print("Used RAM         :", round(memory.used / (1024 ** 3), 2), "GB")
    print("Available RAM    :", round(memory.available / (1024 ** 3), 2), "GB")
    print("Free RAM         :", round(memory.free / (1024 ** 3), 2), "GB")
    print("RAM Usage        :", memory.percent, "%")


# =========================================================
# DETAILED RAM INFORMATION
# =========================================================

def show_detailed_ram():
    print("\n---------- DETAILED RAM INFORMATION ----------")

    memory = psutil.virtual_memory()

    total = memory.total / (1024 ** 3)
    used = memory.used / (1024 ** 3)
    available = memory.available / (1024 ** 3)
    free = memory.free / (1024 ** 3)

    print("Total Memory     :", round(total, 2), "GB")
    print("Used Memory      :", round(used, 2), "GB")
    print("Available Memory :", round(available, 2), "GB")
    print("Free Memory      :", round(free, 2), "GB")
    print("Cached Memory    :", round(memory.cached / (1024 ** 3), 2), "GB")
    print("Buffers          :", round(memory.buffers / (1024 ** 3), 2), "GB")
    print("Usage            :", memory.percent, "%")

    print("\nRAM Status:")

    if memory.percent >= 90:
        print("CRITICAL - RAM usage is very high.")
    elif memory.percent >= 75:
        print("WARNING - RAM usage is getting high.")
    elif memory.percent >= 50:
        print("MODERATE - RAM usage is normal.")
    else:
        print("GOOD - Plenty of RAM is available.")


# =========================================================
# VIRTUAL MEMORY / SWAP
# =========================================================

def show_virtual_memory():
    print("\n---------- VIRTUAL MEMORY ----------")

    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    print("Virtual Memory Total :", round(memory.total / (1024 ** 3), 2), "GB")
    print("Virtual Memory Used  :", round(memory.used / (1024 ** 3), 2), "GB")
    print("Virtual Memory Free  :", round(memory.available / (1024 ** 3), 2), "GB")
    print("Virtual Memory Usage :", memory.percent, "%")

    print("\nSwap Memory Total    :", round(swap.total / (1024 ** 3), 2), "GB")
    print("Swap Memory Used     :", round(swap.used / (1024 ** 3), 2), "GB")
    print("Swap Memory Free     :", round(swap.free / (1024 ** 3), 2), "GB")
    print("Swap Memory Usage    :", swap.percent, "%")


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
            print("Mount :", partition.mountpoint)
            print("File System :", partition.fstype)
            print("Total :", round(usage.total / (1024 ** 3), 2), "GB")
            print("Used  :", round(usage.used / (1024 ** 3), 2), "GB")
            print("Free  :", round(usage.free / (1024 ** 3), 2), "GB")
            print("Usage :", usage.percent, "%")

        except PermissionError:
            print("Unable to access:", partition.device)

        except FileNotFoundError:
            print("Drive is no longer available:", partition.device)


# =========================================================
# DISK ACTIVITY
# =========================================================

def show_disk_activity():
    print("\n---------- DISK ACTIVITY ----------")

    disk = psutil.disk_io_counters()

    if disk is None:
        print("Disk activity information is not available.")
        return

    read_gb = disk.read_bytes / (1024 ** 3)
    write_gb = disk.write_bytes / (1024 ** 3)

    print("Total Read  :", round(read_gb, 2), "GB")
    print("Total Write :", round(write_gb, 2), "GB")
    print("Read Count  :", disk.read_count)
    print("Write Count :", disk.write_count)


# =========================================================
# DISK SPEED SNAPSHOT
# =========================================================

def disk_speed_snapshot():
    print("\n---------- DISK SPEED SNAPSHOT ----------")

    print("Measuring disk activity...")
    print("Please wait...")

    before = psutil.disk_io_counters()

    if before is None:
        print("Disk information is unavailable.")
        return

    start_time = time.time()

    time.sleep(2)

    after = psutil.disk_io_counters()

    if after is None:
        print("Disk information is unavailable.")
        return

    elapsed = time.time() - start_time

    read_bytes = after.read_bytes - before.read_bytes
    write_bytes = after.write_bytes - before.write_bytes

    read_mb = read_bytes / (1024 ** 2)
    write_mb = write_bytes / (1024 ** 2)

    read_speed = read_mb / elapsed
    write_speed = write_mb / elapsed

    print("\nRead Activity  :", round(read_speed, 2), "MB/s")
    print("Write Activity :", round(write_speed, 2), "MB/s")

    print("\nNote:")
    print("This is an activity snapshot, not a full disk benchmark.")


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
# NETWORK INTERFACE DETAILS
# =========================================================

def show_network_interfaces():
    print("\n---------- NETWORK INTERFACES ----------")

    interfaces = psutil.net_if_addrs()

    if not interfaces:
        print("No network interfaces found.")
        return

    for interface, addresses in interfaces.items():
        print("\nInterface:", interface)

        for address in addresses:
            print("  Family :", address.family)
            print("  Address:", address.address)

            if address.netmask:
                print("  Netmask:", address.netmask)

            if address.broadcast:
                print("  Broadcast:", address.broadcast)


# =========================================================
# NETWORK TRAFFIC
# =========================================================

def show_network_traffic():
    print("\n---------- NETWORK TRAFFIC ----------")

    network = psutil.net_io_counters()

    if network is None:
        print("Network traffic information is unavailable.")
        return

    sent = network.bytes_sent / (1024 ** 3)
    received = network.bytes_recv / (1024 ** 3)

    print("Data Sent     :", round(sent, 2), "GB")
    print("Data Received :", round(received, 2), "GB")
    print("Packets Sent  :", network.packets_sent)
    print("Packets Recv. :", network.packets_recv)
    print("Errors Sent   :", network.errout)
    print("Errors Recv.  :", network.errin)


# =========================================================
# NETWORK SPEED SNAPSHOT
# =========================================================

def network_speed_snapshot():
    print("\n---------- NETWORK SPEED SNAPSHOT ----------")

    before = psutil.net_io_counters()

    print("Measuring network activity...")
    time.sleep(2)

    after = psutil.net_io_counters()

    elapsed = 2

    sent_bytes = after.bytes_sent - before.bytes_sent
    received_bytes = after.bytes_recv - before.bytes_recv

    sent_kbps = (sent_bytes / 1024) / elapsed
    received_kbps = (received_bytes / 1024) / elapsed

    print("Upload Activity   :", round(sent_kbps, 2), "KB/s")
    print("Download Activity :", round(received_kbps, 2), "KB/s")

    print("\nNote:")
    print("This measures current network activity, not your maximum internet speed.")


# =========================================================
# NETWORK PACKET STATISTICS
# =========================================================

def show_network_packets():
    print("\n---------- NETWORK PACKET STATISTICS ----------")

    network = psutil.net_io_counters()

    if network is None:
        print("Network statistics are unavailable.")
        return

    print("Packets Sent       :", network.packets_sent)
    print("Packets Received   :", network.packets_recv)
    print("Errors Sent        :", network.errout)
    print("Errors Received    :", network.errin)
    print("Dropped Sent       :", network.dropout)
    print("Dropped Received   :", network.dropin)


# =========================================================
# HOSTNAME AND DNS
# =========================================================

def show_hostname_dns():
    print("\n---------- HOSTNAME AND DNS ----------")

    hostname = socket.gethostname()

    print("Hostname :", hostname)

    try:
        host_info = socket.gethostbyname_ex(hostname)

        print("Canonical Name :", host_info[0])
        print("IP Addresses   :")

        for address in host_info[2]:
            print(" -", address)

    except socket.error:
        print("DNS information could not be retrieved.")


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
# DETAILED BATTERY HEALTH
# =========================================================

def detailed_battery_health():
    print("\n---------- DETAILED BATTERY HEALTH ----------")

    battery = psutil.sensors_battery()

    if battery is None:
        print("Battery information is not available.")
        return

    print("Battery Percentage :", battery.percent, "%")

    if battery.power_plugged:
        print("Power Status       : Plugged In")
    else:
        print("Power Status       : Running on Battery")

    if battery.secsleft not in (
        psutil.POWER_TIME_UNLIMITED,
        psutil.POWER_TIME_UNKNOWN
    ):
        print(
            "Estimated Time Left:",
            str(timedelta(seconds=battery.secsleft))
        )

    if battery.percent >= 80:
        print("Battery Status     : High")
    elif battery.percent >= 40:
        print("Battery Status     : Normal")
    elif battery.percent >= 20:
        print("Battery Status     : Low")
    else:
        print("Battery Status     : Critical")


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
# CURRENT DATE AND TIME
# =========================================================

def show_current_datetime():
    print("\n---------- CURRENT DATE AND TIME ----------")

    current_time = datetime.now()

    print(
        "Date :",
        current_time.strftime("%Y-%m-%d")
    )

    print(
        "Time :",
        current_time.strftime("%H:%M:%S")
    )

    print(
        "Day  :",
        current_time.strftime("%A")
    )


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
# PROCESS COUNT SUMMARY
# =========================================================

def process_count_summary():
    print("\n---------- PROCESS COUNT SUMMARY ----------")

    total = 0
    running = 0
    sleeping = 0
    stopped = 0
    other = 0

    for process in psutil.process_iter(["status"]):
        try:
            total += 1

            status = process.info["status"]

            if status == psutil.STATUS_RUNNING:
                running += 1

            elif status == psutil.STATUS_SLEEPING:
                sleeping += 1

            elif status == psutil.STATUS_STOPPED:
                stopped += 1

            else:
                other += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    print("Total Processes   :", total)
    print("Running Processes :", running)
    print("Sleeping Processes:", sleeping)
    print("Stopped Processes :", stopped)
    print("Other Processes   :", other)


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

    processes.sort(
        key=lambda process: process["cpu"],
        reverse=True
    )

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

    for process in psutil.process_iter(
        ["pid", "name", "memory_percent"]
    ):
        try:
            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "memory": process.info["memory_percent"]
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes.sort(
        key=lambda process: process["memory"],
        reverse=True
    )

    print("\nPID       RAM %      NAME")
    print("-----------------------------------------------")

    for process in processes[:10]:
        print(
            str(process["pid"]).ljust(10),
            str(round(process["memory"], 2)).ljust(10),
            str(process["name"])[:30]
        )


# =========================================================
# PROCESS SEARCH
# =========================================================

def search_process():
    print("\n---------- PROCESS SEARCH ----------")

    keyword = input("Enter process name to search: ").lower()

    if not keyword:
        print("No search term entered.")
        return

    found = False

    for process in psutil.process_iter(
        ["pid", "name", "status"]
    ):
        try:
            name = process.info["name"]

            if name and keyword in name.lower():
                print(
                    "PID:",
                    process.info["pid"],
                    "| Name:",
                    name,
                    "| Status:",
                    process.info["status"]
                )

                found = True

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    if not found:
        print("No matching process was found.")


# =========================================================
# PROCESS TERMINATION
# =========================================================

def terminate_process():
    print("\n---------- PROCESS TERMINATION ----------")

    try:
        pid = int(input("Enter process PID: "))

        process = psutil.Process(pid)

        print("Process Name:", process.name())

        confirmation = input(
            "Are you sure you want to terminate this process? (yes/no): "
        ).lower()

        if confirmation == "yes":
            process.terminate()
            print("Process termination requested.")

        else:
            print("Process termination cancelled.")

    except ValueError:
        print("Please enter a valid PID.")

    except psutil.NoSuchProcess:
        print("Process does not exist.")

    except psutil.AccessDenied:
        print("Access denied. Administrator permission may be required.")

    except Exception as error:
        print("Unable to terminate process:", error)


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
        print(
            "Access denied. Run the program as administrator "
            "to see all connections."
        )


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
# PYTHON PACKAGE CHECK
# =========================================================

def check_python_packages():
    print("\n---------- PYTHON PACKAGE CHECK ----------")

    packages = [
        "psutil",
        "pip",
        "setuptools"
    ]

    for package in packages:

        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "show",
                    package
                ],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("[INSTALLED]", package)
            else:
                print("[NOT FOUND]", package)

        except Exception:
            print("[ERROR]", package)


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

    score = (
        cpu_score +
        memory_score +
        disk_score
    ) / 3

    print("CPU Score  :", round(cpu_score, 2))
    print("RAM Score  :", round(memory_score, 2))
    print("Disk Score :", round(disk_score, 2))

    print(
        "\nOverall Health Score :",
        round(score, 2),
        "%"
    )

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
# FOLDER FILE COUNTER
# =========================================================

def count_folder_files():
    print("\n---------- FOLDER FILE COUNTER ----------")

    folder = input("Enter folder path: ")

    if not os.path.isdir(folder):
        print("Invalid folder.")
        return

    file_count = 0
    folder_count = 0

    for root, directories, files in os.walk(folder):

        folder_count += len(directories)
        file_count += len(files)

    print("\nFolder :", folder)
    print("Files  :", file_count)
    print("Folders:", folder_count)


# =========================================================
# FILE EXTENSION ANALYZER
# =========================================================

def analyze_file_extensions():
    print("\n---------- FILE EXTENSION ANALYZER ----------")

    folder = input("Enter folder path: ")

    if not os.path.isdir(folder):
        print("Invalid folder.")
        return

    extensions = {}

    for root, directories, files in os.walk(folder):

        for file in files:

            extension = os.path.splitext(file)[1].lower()

            if extension == "":
                extension = "[No Extension]"

            if extension in extensions:
                extensions[extension] += 1

            else:
                extensions[extension] = 1

    if not extensions:
        print("No files found.")
        return

    print("\nFile Types:")

    sorted_extensions = sorted(
        extensions.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for extension, count in sorted_extensions:
        print(
            extension,
            ":",
            count,
            "file(s)"
        )


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

    large_files.sort(
        key=lambda item: item[1],
        reverse=True
    )

    if not large_files:
        print("No large files were found.")
        return

    print("\nLarge Files:")
    print("-----------------------------------------------")

    for file_path, file_size in large_files[:20]:

        size_mb = file_size / (1024 ** 2)

        print(
            round(size_mb, 2),
            "MB -",
            file_path
        )

    if len(large_files) > 20:
        print("\nShowing the first 20 large files.")


# =========================================================
# DUPLICATE FILE FINDER
# =========================================================

def find_duplicate_files():
    print("\n---------- DUPLICATE FILE FINDER ----------")

    folder = input("Enter folder path: ")

    if not os.path.isdir(folder):
        print("Invalid folder.")
        return

    files_by_size = {}

    for root, directories, files in os.walk(folder):

        for file in files:

            try:
                path = os.path.join(root, file)
                size = os.path.getsize(path)

                if size not in files_by_size:
                    files_by_size[size] = []

                files_by_size[size].append(path)

            except (PermissionError, FileNotFoundError):
                pass

    duplicate_groups = 0

    for size, files in files_by_size.items():

        if len(files) > 1:

            duplicate_groups += 1

            print("\nPossible duplicate group:")

            print(
                "File Size:",
                round(size / (1024 ** 2), 2),
                "MB"
            )

            for file in files:
                print("-", file)

    if duplicate_groups == 0:
        print("No possible duplicate files found.")

    else:
        print(
            "\nPossible duplicate groups:",
            duplicate_groups
        )

        print(
            "Files were grouped by size only."
        )


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

    print(
        "Total Size  :",
        round(total_size / (1024 ** 2), 2),
        "MB"
    )


# =========================================================
# BOOT INFORMATION
# =========================================================

def show_boot_information():
    print("\n---------- BOOT INFORMATION ----------")

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    current_time = datetime.now()

    uptime = current_time - boot_time

    print(
        "Last Boot Time :",
        boot_time.strftime("%Y-%m-%d %H:%M:%S")
    )

    print(
        "Current Time   :",
        current_time.strftime("%Y-%m-%d %H:%M:%S")
    )

    print("Uptime         :", uptime)


# =========================================================
# SYSTEM TEMPERATURE
# =========================================================

def show_temperature():
    print("\n---------- SYSTEM TEMPERATURE ----------")

    try:
        temperatures = psutil.sensors_temperatures()

        if not temperatures:
            print(
                "Temperature information is not available."
            )
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
        print(
            "Temperature sensors are not supported."
        )


# =========================================================
# DISK SPACE WARNING
# =========================================================

def disk_space_warning():
    print("\n---------- DISK SPACE WARNING ----------")

    partitions = psutil.disk_partitions()

    for partition in partitions:

        try:
            usage = psutil.disk_usage(
                partition.mountpoint
            )

            print("\nDrive :", partition.device)
            print("Usage :", usage.percent, "%")

            if usage.percent >= 90:
                print(
                    "Warning: Disk is almost full!"
                )

            elif usage.percent >= 75:
                print(
                    "Warning: Disk space is getting low."
                )

            else:
                print(
                    "Status: Disk space is okay."
                )

        except (
            PermissionError,
            FileNotFoundError
        ):
            pass


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
            usage = psutil.disk_usage(
                partition.mountpoint
            )

            total_storage += usage.total
            total_used += usage.used
            total_free += usage.free

        except (
            PermissionError,
            FileNotFoundError
        ):
            pass

    print(
        "Total Storage :",
        round(total_storage / (1024 ** 3), 2),
        "GB"
    )

    print(
        "Used Storage  :",
        round(total_used / (1024 ** 3), 2),
        "GB"
    )

    print(
        "Free Storage  :",
        round(total_free / (1024 ** 3), 2),
        "GB"
    )


# =========================================================
# GPU INFORMATION
# =========================================================

def show_gpu_information():
    print("\n---------- GPU INFORMATION ----------")

    if platform.system() != "Windows":
        print(
            "This feature is intended for Windows systems."
        )
        return

    try:
        result = subprocess.run(
            [
                "wmic",
                "path",
                "win32_VideoController",
                "get",
                "Name,AdapterRAM,DriverVersion"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)

        else:
            print(
                "GPU information could not be retrieved."
            )

    except FileNotFoundError:
        print(
            "GPU information command is not available."
        )


# =========================================================
# MOTHERBOARD INFORMATION
# =========================================================

def show_motherboard_information():
    print("\n---------- MOTHERBOARD INFORMATION ----------")

    if platform.system() != "Windows":
        print(
            "This feature is intended for Windows systems."
        )
        return

    try:
        result = subprocess.run(
            [
                "wmic",
                "baseboard",
                "get",
                "Manufacturer,Product,SerialNumber"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)

        else:
            print(
                "Motherboard information could not be retrieved."
            )

    except FileNotFoundError:
        print(
            "Motherboard information command is not available."
        )


# =========================================================
# USER INFORMATION
# =========================================================

def show_user_information():
    print("\n---------- USER INFORMATION ----------")

    print("Username       :", getpass.getuser())
    print("Home Directory :", os.path.expanduser("~"))
    print("Computer Name  :", socket.gethostname())


# =========================================================
# USER SESSION INFORMATION
# =========================================================

def show_session_information():
    print("\n---------- USER SESSION INFORMATION ----------")

    try:
        users = psutil.users()

        if not users:
            print("No user session information available.")
            return

        print("Active User Sessions:", len(users))

        for user in users:
            print("\nUsername :", user.name)
            print("Terminal :", user.terminal)
            print("Host     :", user.host)
            print(
                "Started  :",
                datetime.fromtimestamp(
                    user.started
                ).strftime("%Y-%m-%d %H:%M:%S")
            )

    except Exception as error:
        print(
            "Unable to retrieve user sessions:",
            error
        )


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
        print(
            "\nShowing the first 30 environment variables."
        )


# =========================================================
# INTERNET CONNECTION TEST
# =========================================================

def test_internet_connection():
    print("\n---------- INTERNET CONNECTION TEST ----------")

    host = "google.com"

    try:
        start_time = datetime.now()

        socket.create_connection(
            (host, 80),
            timeout=5
        )

        end_time = datetime.now()

        response_time = (
            end_time - start_time
        ).total_seconds()

        print(
            "Connection Status :",
            "Connected"
        )

        print(
            "Test Server       :",
            host
        )

        print(
            "Response Time     :",
            round(response_time * 1000, 2),
            "ms"
        )

    except OSError:
        print(
            "Connection Status : No Internet Connection"
        )


# =========================================================
# PING TEST
# =========================================================

def ping_test():
    print("\n---------- PING TEST ----------")

    host = input(
        "Enter website or IP address: "
    )

    if not host:
        print("No address entered.")
        return

    try:

        if platform.system() == "Windows":
            command = [
                "ping",
                "-n",
                "4",
                host
            ]

        else:
            command = [
                "ping",
                "-c",
                "4",
                host
            ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        print(result.stdout)

    except Exception as error:
        print(
            "Ping failed:",
            error
        )


# =========================================================
# MAC ADDRESS
# =========================================================

def show_mac_address():
    print("\n---------- MAC ADDRESS ----------")

    mac = uuid.getnode()

    mac_address = ":".join(
        f"{(mac >> element) & 0xff:02x}"
        for element in range(
            40,
            -1,
            -8
        )
    )

    print(
        "MAC Address :",
        mac_address.upper()
    )


# =========================================================
# ARCHITECTURE DETAILS
# =========================================================

def show_architecture_details():
    print("\n---------- SYSTEM ARCHITECTURE ----------")

    print(
        "Operating System :",
        platform.system()
    )

    print(
        "OS Release       :",
        platform.release()
    )

    print(
        "OS Version       :",
        platform.version()
    )

    print(
        "Machine Type     :",
        platform.machine()
    )

    print(
        "Processor        :",
        platform.processor()
    )

    print(
        "Architecture     :",
        platform.architecture()[0]
    )

    print(
        "Platform         :",
        platform.platform()
    )

    print(
        "Python Version   :",
        platform.python_version()
    )


# =========================================================
# WINDOWS SERVICES
# =========================================================

def show_windows_services():
    print("\n---------- WINDOWS SERVICES ----------")

    if platform.system() != "Windows":
        print(
            "This feature is intended for Windows systems."
        )
        return

    try:
        result = subprocess.run(
            [
                "sc",
                "query",
                "type=",
                "service"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            lines = result.stdout.splitlines()

            count = 0

            for line in lines:

                if "SERVICE_NAME:" in line:

                    print(line.strip())

                    count += 1

                    if count >= 30:
                        break

            print(
                "\nShowing up to 30 Windows services."
            )

        else:
            print(
                "Unable to retrieve Windows services."
            )

    except Exception as error:
        print(
            "Service check failed:",
            error
        )


# =========================================================
# STARTUP PROGRAMS
# =========================================================

def show_startup_programs():
    print("\n---------- STARTUP PROGRAMS ----------")

    if platform.system() != "Windows":
        print(
            "This feature is intended for Windows systems."
        )
        return

    startup_paths = [
        os.path.expandvars(
            r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
        ),
        os.path.expandvars(
            r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
        )
    ]

    found = False

    for folder in startup_paths:

        if os.path.isdir(folder):

            print(
                "\nStartup Folder:",
                folder
            )

            for item in os.listdir(folder):

                print("-", item)

                found = True

    if not found:
        print(
            "No startup files were found."
        )


# =========================================================
# QUICK DIAGNOSTIC SCAN
# =========================================================

def quick_diagnostic_scan():
    print("\n========================================")
    print("         QUICK DIAGNOSTIC SCAN")
    print("========================================")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(
        os.path.abspath(os.sep)
    )

    print("\nCPU Usage :", cpu, "%")
    print("RAM Usage :", memory.percent, "%")
    print("Disk Usage:", disk.percent, "%")

    print("\nChecking system status...")

    issues = 0

    if cpu >= 90:
        print(
            "[WARNING] CPU usage is very high."
        )
        issues += 1

    else:
        print(
            "[OK] CPU usage is normal."
        )

    if memory.percent >= 90:
        print(
            "[WARNING] RAM usage is very high."
        )
        issues += 1

    else:
        print(
            "[OK] RAM usage is normal."
        )

    if disk.percent >= 90:
        print(
            "[WARNING] Disk space is almost full."
        )
        issues += 1

    else:
        print(
            "[OK] Disk space is sufficient."
        )

    battery = psutil.sensors_battery()

    if battery:

        if (
            battery.percent <= 20
            and not battery.power_plugged
        ):
            print(
                "[WARNING] Battery level is low."
            )
            issues += 1

        else:
            print(
                "[OK] Battery level is acceptable."
            )

    print("\n----------------------------------------")

    if issues == 0:
        print(
            "No major problems detected."
        )

    else:
        print(
            "Potential issues detected:",
            issues
        )

    print("Quick scan complete.")


# =========================================================
# DIAGNOSTIC CHECKLIST
# =========================================================

def diagnostic_checklist():
    print(
        "\n---------- DIAGNOSTIC CHECKLIST ----------"
    )

    issues = 0

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(
        os.path.abspath(os.sep)
    )

    print("\nChecking CPU...")

    if cpu >= 90:
        print(
            "[WARNING] CPU usage is very high."
        )
        issues += 1

    else:
        print(
            "[OK] CPU usage is acceptable."
        )

    print("\nChecking RAM...")

    if memory.percent >= 90:
        print(
            "[WARNING] RAM usage is very high."
        )
        issues += 1

    else:
        print(
            "[OK] RAM usage is acceptable."
        )

    print("\nChecking Disk...")

    if disk.percent >= 90:
        print(
            "[WARNING] Disk space is almost full."
        )
        issues += 1

    else:
        print(
            "[OK] Disk space is acceptable."
        )

    print("\nChecking Battery...")

    battery = psutil.sensors_battery()

    if battery:

        if (
            battery.percent <= 20
            and not battery.power_plugged
        ):
            print(
                "[WARNING] Battery level is low."
            )
            issues += 1

        else:
            print(
                "[OK] Battery level is acceptable."
            )

    else:
        print(
            "[INFO] Battery information unavailable."
        )

    print("\n========================================")

    if issues == 0:
        print(
            "Diagnostic Checklist: No major issues found."
        )

    else:
        print(
            "Diagnostic Checklist:",
            issues,
            "issue(s) detected."
        )

    print("========================================")


# =========================================================
# SYSTEM RESOURCE MONITOR
# =========================================================

def resource_monitor():
    print(
        "\n---------- SYSTEM RESOURCE MONITOR ----------"
    )

    print(
        "Press CTRL+C to stop the monitor."
    )

    try:

        while True:

            cpu = psutil.cpu_percent(
                interval=1
            )

            memory = psutil.virtual_memory()

            disk = psutil.disk_usage(
                os.path.abspath(os.sep)
            )

            print(
                "CPU:",
                str(cpu) + "%",
                "| RAM:",
                str(memory.percent) + "%",
                "| Disk:",
                str(disk.percent) + "%"
            )

    except KeyboardInterrupt:
        print(
            "\nResource monitor stopped."
        )


# =========================================================
# SYSTEM SUMMARY
# =========================================================

def show_system_summary():
    print("\n========================================")
    print("          SYSTEM SUMMARY")
    print("========================================")

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage(
        os.path.abspath(os.sep)
    )

    print(
        "Computer Name :",
        socket.gethostname()
    )

    print(
        "Operating System:",
        platform.system()
    )

    print(
        "OS Version     :",
        platform.version()
    )

    print(
        "Processor      :",
        platform.processor()
    )

    print(
        "CPU Cores      :",
        psutil.cpu_count(logical=False)
    )

    print(
        "Logical CPUs   :",
        psutil.cpu_count(logical=True)
    )

    print(
        "CPU Usage      :",
        psutil.cpu_percent(interval=1),
        "%"
    )

    print(
        "Total RAM      :",
        round(memory.total / (1024 ** 3), 2),
        "GB"
    )

    print(
        "RAM Usage      :",
        memory.percent,
        "%"
    )

    print(
        "System Disk    :",
        round(disk.total / (1024 ** 3), 2),
        "GB"
    )

    print(
        "Disk Usage     :",
        disk.percent,
        "%"
    )

    print(
        "Python Version :",
        platform.python_version()
    )


# =========================================================
# SYSTEM RESOURCE SNAPSHOT
# =========================================================

def system_resource_snapshot():
    print("\n---------- RESOURCE SNAPSHOT ----------")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk = psutil.disk_usage(
        os.path.abspath(os.sep)
    )
    network = psutil.net_io_counters()

    print("\nCPU")
    print("Usage :", cpu, "%")

    print("\nRAM")
    print("Usage :", memory.percent, "%")
    print(
        "Used  :",
        round(memory.used / (1024 ** 3), 2),
        "GB"
    )

    print("\nSwap")
    print("Usage :", swap.percent, "%")

    print("\nDisk")
    print("Usage :", disk.percent, "%")

    print("\nNetwork")
    print(
        "Sent :",
        round(network.bytes_sent / (1024 ** 3), 2),
        "GB"
    )

    print(
        "Recv :",
        round(network.bytes_recv / (1024 ** 3), 2),
        "GB"
    )


# =========================================================
# SAVE DIAGNOSTIC REPORT
# =========================================================

def save_diagnostic_report():
    print(
        "\n---------- SAVE DIAGNOSTIC REPORT ----------"
    )

    filename = "diagnostic_report.txt"

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(
        os.path.abspath(os.sep)
    )

    network = psutil.net_io_counters()

    report = []

    report.append(
        "========================================"
    )

    report.append(
        "       PC DIAGNOSTIC REPORT"
    )

    report.append(
        "========================================"
    )

    report.append("")

    report.append(
        "System Information"
    )

    report.append(
        "------------------"
    )

    report.append(
        "Operating System : "
        + platform.system()
    )

    report.append(
        "System Version   : "
        + platform.version()
    )

    report.append(
        "Computer Name    : "
        + socket.gethostname()
    )

    report.append(
        "Architecture     : "
        + platform.architecture()[0]
    )

    report.append(
        "Processor        : "
        + platform.processor()
    )

    report.append("")

    report.append(
        "CPU Information"
    )

    report.append(
        "---------------"
    )

    report.append(
        "CPU Usage        : "
        + str(cpu)
        + "%"
    )

    report.append(
        "CPU Cores        : "
        + str(psutil.cpu_count(logical=False))
    )

    report.append(
        "Logical CPUs     : "
        + str(psutil.cpu_count(logical=True))
    )

    report.append("")

    report.append(
        "Memory Information"
    )

    report.append(
        "------------------"
    )

    report.append(
        "Total RAM        : "
        + str(
            round(
                memory.total / (1024 ** 3),
                2
            )
        )
        + " GB"
    )

    report.append(
        "Used RAM         : "
        + str(
            round(
                memory.used / (1024 ** 3),
                2
            )
        )
        + " GB"
    )

    report.append(
        "RAM Usage        : "
        + str(memory.percent)
        + "%"
    )

    report.append("")

    report.append(
        "Storage Information"
    )

    report.append(
        "-------------------"
    )

    report.append(
        "Disk Usage       : "
        + str(disk.percent)
        + "%"
    )

    report.append(
        "Total Disk       : "
        + str(
            round(
                disk.total / (1024 ** 3),
                2
            )
        )
        + " GB"
    )

    report.append(
        "Free Disk        : "
        + str(
            round(
                disk.free / (1024 ** 3),
                2
            )
        )
        + " GB"
    )

    report.append("")

    report.append(
        "Network Information"
    )

    report.append(
        "-------------------"
    )

    report.append(
        "Data Sent        : "
        + str(
            round(
                network.bytes_sent / (1024 ** 3),
                2
            )
        )
        + " GB"
    )

    report.append(
        "Data Received    : "
        + str(
            round(
                network.bytes_recv / (1024 ** 3),
                2
            )
        )
        + " GB"
    )

    report.append("")

    report.append(
        "Python Version : "
        + platform.python_version()
    )

    report.append(
        "Username       : "
        + getpass.getuser()
    )

    report.append(
        "Report Created : "
        + datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    report.append(
        "========================================"
    )

    try:

        with open(
            filename,
            "w"
        ) as file:

            for line in report:
                file.write(line + "\n")

        print(
            "Diagnostic report saved as:",
            filename
        )

    except PermissionError:
        print(
            "Permission denied. "
            "Unable to save the report."
        )


# =========================================================
# HELP
# =========================================================

def show_help():
    print("\n---------- HELP ----------")

    print("PC Diagnostic Tool")
    print()

    print(
        "Use the menu numbers to select "
        "a diagnostic function."
    )

    print()

    print(
        "The tool checks hardware, software,"
    )

    print(
        "network, storage, processes, and"
    )

    print(
        "system performance."
    )

    print()

    print(
        "Some functions may require administrator access."
    )

    print(
        "Some hardware information may not be available"
    )

    print(
        "depending on your computer."
    )


# =========================================================
# ABOUT
# =========================================================

def show_about():
    print("\n========================================")
    print("          ABOUT PC DIAGNOSTIC TOOL")
    print("========================================")

    print(
        "A beginner-friendly Python PC diagnostic program."
    )

    print()

    print(
        "Created using Python and psutil."
    )

    print(
        "Purpose: Practice functions, loops, conditions,"
    )

    print(
        "user input, system information, and file handling."
    )

    print()

    print("Version: 4.0")


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
    process_count_summary()
    show_network_traffic()

    print("\n========================================")
    print("       DIAGNOSTIC COMPLETE")
    print("========================================")


# =========================================================
# CLEAR SCREEN
# =========================================================

def clear_screen():

    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


# =========================================================
# MENU
# =========================================================

def show_menu():

    print("\n========================================")
    print("          PC DIAGNOSTIC TOOL")
    print("========================================")

    print("\n--- SYSTEM ---")
    print("1.  System Information")
    print("2.  System Architecture Details")
    print("3.  System Summary")
    print("4.  Current Date and Time")
    print("5.  Boot Information")
    print("6.  System Uptime")

    print("\n--- CPU AND MEMORY ---")
    print("7.  CPU Information")
    print("8.  CPU Load Per Core")
    print("9.  CPU Load Average")
    print("10. RAM Information")
    print("11. Detailed RAM Information")
    print("12. Virtual Memory / Swap")
    print("13. System Temperature")

    print("\n--- STORAGE ---")
    print("14. Disk Information")
    print("15. Disk Activity")
    print("16. Disk Speed Snapshot")
    print("17. Storage Summary")
    print("18. Disk Space Warning")
    print("19. Folder Size Checker")
    print("20. Folder File Counter")
    print("21. Large File Finder")
    print("22. File Extension Analyzer")
    print("23. Duplicate File Finder")
    print("24. Temporary File Checker")

    print("\n--- NETWORK ---")
    print("25. Network Information")
    print("26. Network Interface Details")
    print("27. Network Traffic")
    print("28. Network Speed Snapshot")
    print("29. Network Packet Statistics")
    print("30. Network Connections")
    print("31. Hostname and DNS Information")
    print("32. Internet Connection Test")
    print("33. Ping Test")
    print("34. MAC Address")

    print("\n--- BATTERY ---")
    print("35. Battery Information")
    print("36. Detailed Battery Health")

    print("\n--- PROCESSES ---")
    print("37. Running Processes")
    print("38. Process Count Summary")
    print("39. Top CPU Processes")
    print("40. Top RAM Processes")
    print("41. Process Search")
    print("42. Process Termination")

    print("\n--- WINDOWS ---")
    print("43. GPU Information")
    print("44. Motherboard Information")
    print("45. Windows Services")
    print("46. Startup Programs")

    print("\n--- PYTHON ---")
    print("47. Python Information")
    print("48. Python Package Check")

    print("\n--- USER ---")
    print("49. User Information")
    print("50. User Session Information")
    print("51. Environment Variables")

    print("\n--- DIAGNOSTICS ---")
    print("52. Health Check")
    print("53. Performance Summary")
    print("54. System Health Score")
    print("55. Quick Diagnostic Scan")
    print("56. Diagnostic Checklist")
    print("57. System Resource Snapshot")
    print("58. System Resource Monitor")
    print("59. Full Diagnostic Report")
    print("60. Save Diagnostic Report")

    print("\n--- OTHER ---")
    print("61. Help")
    print("62. About")
    print("63. Clear Screen")

    print("\n0.  Exit")

    print("========================================")


# =========================================================
# MAIN PROGRAM
# =========================================================

def main():

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":
            show_system_information()

        elif choice == "2":
            show_architecture_details()

        elif choice == "3":
            show_system_summary()

        elif choice == "4":
            show_current_datetime()

        elif choice == "5":
            show_boot_information()

        elif choice == "6":
            show_uptime()

        elif choice == "7":
            show_cpu_information()

        elif choice == "8":
            show_cpu_per_core()

        elif choice == "9":
            show_cpu_load_average()

        elif choice == "10":
            show_ram_information()

        elif choice == "11":
            show_detailed_ram()

        elif choice == "12":
            show_virtual_memory()

        elif choice == "13":
            show_temperature()

        elif choice == "14":
            show_disk_information()

        elif choice == "15":
            show_disk_activity()

        elif choice == "16":
            disk_speed_snapshot()

        elif choice == "17":
            show_storage_summary()

        elif choice == "18":
            disk_space_warning()

        elif choice == "19":
            check_folder_size()

        elif choice == "20":
            count_folder_files()

        elif choice == "21":
            find_large_files()

        elif choice == "22":
            analyze_file_extensions()

        elif choice == "23":
            find_duplicate_files()

        elif choice == "24":
            check_temp_folder()

        elif choice == "25":
            show_network_information()

        elif choice == "26":
            show_network_interfaces()

        elif choice == "27":
            show_network_traffic()

        elif choice == "28":
            network_speed_snapshot()

        elif choice == "29":
            show_network_packets()

        elif choice == "30":
            show_network_connections()

        elif choice == "31":
            show_hostname_dns()

        elif choice == "32":
            test_internet_connection()

        elif choice == "33":
            ping_test()

        elif choice == "34":
            show_mac_address()

        elif choice == "35":
            show_battery_information()

        elif choice == "36":
            detailed_battery_health()

        elif choice == "37":
            show_running_processes()

        elif choice == "38":
            process_count_summary()

        elif choice == "39":
            show_top_cpu_processes()

        elif choice == "40":
            show_top_ram_processes()

        elif choice == "41":
            search_process()

        elif choice == "42":
            terminate_process()

        elif choice == "43":
            show_gpu_information()

        elif choice == "44":
            show_motherboard_information()

        elif choice == "45":
            show_windows_services()

        elif choice == "46":
            show_startup_programs()

        elif choice == "47":
            show_python_information()

        elif choice == "48":
            check_python_packages()

        elif choice == "49":
            show_user_information()

        elif choice == "50":
            show_session_information()

        elif choice == "51":
            show_environment_variables()

        elif choice == "52":
            health_check()

        elif choice == "53":
            show_performance_summary()

        elif choice == "54":
            calculate_health_score()

        elif choice == "55":
            quick_diagnostic_scan()

        elif choice == "56":
            diagnostic_checklist()

        elif choice == "57":
            system_resource_snapshot()

        elif choice == "58":
            resource_monitor()

        elif choice == "59":
            full_diagnostic_report()

        elif choice == "60":
            save_diagnostic_report()

        elif choice == "61":
            show_help()

        elif choice == "62":
            show_about()

        elif choice == "63":
            clear_screen()

        elif choice == "0":
            print(
                "\nThank you for using "
                "PC Diagnostic Tool!"
            )
            break

        else:
            print(
                "\nInvalid choice."
                " Please select a number from 0 to 63."
            )


# =========================================================
# START PROGRAM
# =========================================================

if __name__ == "__main__":
    main()
