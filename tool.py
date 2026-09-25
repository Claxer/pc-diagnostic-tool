import platform
import psutil
import socket
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
    print("CPU Frequency    :", round(psutil.cpu_freq().current, 2), "MHz")


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

    print("\n========================================")
    print("       DIAGNOSTIC COMPLETE")
    print("========================================")


def show_menu():
    print("\n========================================")
    print("          PC DIAGNOSTIC TOOL")
    print("========================================")
    print("1. System Information")
    print("2. CPU Information")
    print("3. RAM Information")
    print("4. Disk Information")
    print("5. Network Information")
    print("6. Battery Information")
    print("7. System Uptime")
    print("8. System Health Check")
    print("9. Full Diagnostic Report")
    print("0. Exit")
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

        elif choice == "0":
            print("\nThank you for using PC Diagnostic Tool!")
            break

        else:
            print("\nInvalid choice. Please select a number from 0 to 9.")


main()
