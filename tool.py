import os
import sys
import csv
import time
import socket
import platform
import subprocess
import threading
import webbrowser
from pathlib import Path
from datetime import datetime, timedelta

import customtkinter as ctk
import psutil
from tkinter import messagebox, filedialog

APP_NAME = "NEXUS | PC DIAGNOSTICS"
APP_VERSION = "5.0.0"
REPORT_DIR = Path.home() / "PCDiagnosticReports"
REPORT_DIR.mkdir(exist_ok=True)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

BG = "#0b0d12"
PANEL = "#121620"
PANEL_ALT = "#181e2a"
BORDER = "#252d3b"
TEXT = "#f2f5fa"
MUTED = "#8d99ad"
ACCENT = "#6d8cff"
GREEN = "#40d6a0"
YELLOW = "#f4c66a"
RED = "#ff6b78"


def gb(value):
    return round(value / (1024 ** 3), 2)


def mb(value):
    return round(value / (1024 ** 2), 2)


def safe_disk_usage(path):
    try:
        return psutil.disk_usage(path)
    except (OSError, PermissionError):
        return None


def collect_snapshot():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    root_path = os.path.abspath(os.sep)
    disk = safe_disk_usage(root_path)
    battery = psutil.sensors_battery()
    net = psutil.net_io_counters()
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "computer": socket.gethostname(),
        "os": f"{platform.system()} {platform.release()}",
        "cpu_name": platform.processor() or "Not reported by system",
        "cpu_cores": psutil.cpu_count(logical=False) or "Unknown",
        "logical_cpus": psutil.cpu_count(logical=True) or "Unknown",
        "cpu": psutil.cpu_percent(interval=0.25),
        "ram_total": gb(memory.total),
        "ram_used": gb(memory.used),
        "ram_available": gb(memory.available),
        "ram_percent": memory.percent,
        "swap_total": gb(swap.total),
        "swap_used": gb(swap.used),
        "swap_percent": swap.percent,
        "disk_total": gb(disk.total) if disk else 0,
        "disk_used": gb(disk.used) if disk else 0,
        "disk_free": gb(disk.free) if disk else 0,
        "disk_percent": disk.percent if disk else 0,
        "network_sent": mb(net.bytes_sent) if net else 0,
        "network_received": mb(net.bytes_recv) if net else 0,
        "uptime": str(datetime.now() - datetime.fromtimestamp(psutil.boot_time())).split('.')[0],
        "battery_percent": battery.percent if battery else None,
        "battery_plugged": battery.power_plugged if battery else None,
        "python": platform.python_version(),
    }


def build_diagnostics(data):
    findings = []
    if data["cpu"] >= 90:
        findings.append(("CRITICAL", "CPU usage is very high", "Check the top CPU processes and close apps you recognize but do not need."))
    elif data["cpu"] >= 75:
        findings.append(("WARNING", "CPU usage is elevated", "Check whether a demanding app or background task is running."))
    else:
        findings.append(("OK", "CPU usage is within the normal range", "No action is needed based on this snapshot."))
    if data["ram_percent"] >= 90:
        findings.append(("CRITICAL", "Memory pressure is high", "Close unused applications and inspect the top memory-consuming processes."))
    elif data["ram_percent"] >= 80:
        findings.append(("WARNING", "RAM usage is elevated", "Review open applications and browser tabs."))
    else:
        findings.append(("OK", "RAM usage is within the normal range", "Available memory looks reasonable in this snapshot."))
    if data["disk_percent"] >= 95:
        findings.append(("CRITICAL", "System drive is nearly full", "Back up important files, then remove only files you know are safe to delete."))
    elif data["disk_percent"] >= 85:
        findings.append(("WARNING", "System drive has limited free space", "Review Downloads, large files, and installed apps before removing anything."))
    else:
        findings.append(("OK", "System drive has available space", "No storage warning was triggered."))
    if data["battery_percent"] is not None:
        if data["battery_percent"] <= 15 and not data["battery_plugged"]:
            findings.append(("WARNING", "Battery level is low", "Connect the charger if you need to keep working."))
        else:
            findings.append(("OK", "Battery level does not trigger a warning", "Battery wear/health cannot be confirmed from percentage alone."))
    return findings


class DiagnosticApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP_NAME}  v{APP_VERSION}")
        self.geometry("1240x820")
        self.minsize(1050, 700)
        self.configure(fg_color=BG)
        self.current_page = "Overview"
        self.monitoring = True
        self.history = {"CPU": [], "RAM": [], "Disk": []}
        self.process_rows = []
        self._build_shell()
        self.show_page("Overview")
        self.after(800, self.refresh_dashboard)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def _build_shell(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.sidebar = ctk.CTkFrame(self, width=230, corner_radius=0, fg_color="#0e1118", border_width=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        brand = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        brand.pack(fill="x", padx=20, pady=(24, 26))
        ctk.CTkLabel(brand, text="NEXUS", font=ctk.CTkFont(size=24, weight="bold"), text_color=TEXT).pack(anchor="w")
        ctk.CTkLabel(brand, text="PC DIAGNOSTICS  /  5.0", font=ctk.CTkFont(size=10, weight="bold"), text_color=ACCENT).pack(anchor="w", pady=(2, 0))
        ctk.CTkLabel(self.sidebar, text="WORKSPACE", text_color=MUTED, font=ctk.CTkFont(size=10, weight="bold")).pack(anchor="w", padx=22, pady=(0, 8))
        self.nav_buttons = {}
        for name, symbol in [("Overview", "◫"), ("Diagnostics", "⌁"), ("Processes", "▤"), ("Hardware", "▦"), ("Network", "⌘"), ("File Tools", "▧"), ("Reports", "▤")]:
            btn = ctk.CTkButton(self.sidebar, text=f"{symbol}    {name}", anchor="w", height=42, corner_radius=9,
                                fg_color="transparent", hover_color=PANEL_ALT, text_color=MUTED,
                                font=ctk.CTkFont(size=13), command=lambda page=name: self.show_page(page))
            btn.pack(fill="x", padx=12, pady=3)
            self.nav_buttons[name] = btn
        ctk.CTkFrame(self.sidebar, height=1, fg_color=BORDER).pack(fill="x", padx=18, pady=(24, 14))
        self.status_dot = ctk.CTkLabel(self.sidebar, text="●  SYSTEM READY", text_color=GREEN, font=ctk.CTkFont(size=10, weight="bold"))
        self.status_dot.pack(anchor="w", padx=20)
        ctk.CTkLabel(self.sidebar, text="Local diagnostics only\nNo telemetry is sent", text_color=MUTED, justify="left", font=ctk.CTkFont(size=10)).pack(side="bottom", anchor="w", padx=20, pady=20)
        self.main = ctk.CTkFrame(self, fg_color=BG, corner_radius=0)
        self.main.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.main.grid_rowconfigure(1, weight=1)
        self.main.grid_columnconfigure(0, weight=1)
        self.header = ctk.CTkFrame(self.main, fg_color=BG, corner_radius=0)
        self.header.grid(row=0, column=0, sticky="ew", padx=28, pady=(22, 12))
        self.header.grid_columnconfigure(0, weight=1)
        self.page_title = ctk.CTkLabel(self.header, text="Overview", font=ctk.CTkFont(size=26, weight="bold"), text_color=TEXT)
        self.page_title.grid(row=0, column=0, sticky="w")
        self.clock_label = ctk.CTkLabel(self.header, text="", text_color=MUTED, font=ctk.CTkFont(size=12))
        self.clock_label.grid(row=0, column=1, sticky="e", padx=(10, 0))
        self.content = ctk.CTkScrollableFrame(self.main, fg_color=BG, corner_radius=0)
        self.content.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        self.after(1000, self.update_clock)

    def update_clock(self):
        if not self.winfo_exists():
            return
        self.clock_label.configure(text=datetime.now().strftime("%a, %d %b %Y  •  %H:%M:%S"))
        self.after(1000, self.update_clock)

    def clear_content(self):
        for child in self.content.winfo_children():
            child.destroy()

    def show_page(self, page):
        self.current_page = page
        self.page_title.configure(text=page)
        for name, button in self.nav_buttons.items():
            button.configure(fg_color=PANEL_ALT if name == page else "transparent", text_color=TEXT if name == page else MUTED)
        self.clear_content()
        handlers = {
            "Overview": self.page_overview,
            "Diagnostics": self.page_diagnostics,
            "Processes": self.page_processes,
            "Hardware": self.page_hardware,
            "Network": self.page_network,
            "File Tools": self.page_file_tools,
            "Reports": self.page_reports,
        }
        handlers[page]()

    def section_label(self, parent, title, subtitle=None):
        ctk.CTkLabel(parent, text=title, text_color=TEXT, font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", pady=(12, 3))
        if subtitle:
            ctk.CTkLabel(parent, text=subtitle, text_color=MUTED, font=ctk.CTkFont(size=11)).pack(anchor="w", pady=(0, 8))

    def card(self, parent, title, value, detail, accent=ACCENT):
        frame = ctk.CTkFrame(parent, fg_color=PANEL, corner_radius=14, border_width=1, border_color=BORDER)
        ctk.CTkLabel(frame, text=title.upper(), text_color=MUTED, font=ctk.CTkFont(size=10, weight="bold")).pack(anchor="w", padx=16, pady=(15, 5))
        ctk.CTkLabel(frame, text=value, text_color=TEXT, font=ctk.CTkFont(size=26, weight="bold")).pack(anchor="w", padx=16)
        ctk.CTkLabel(frame, text=detail, text_color=accent, font=ctk.CTkFont(size=11)).pack(anchor="w", padx=16, pady=(3, 15))
        return frame

    def progress_panel(self, parent, title, percent, detail, color=ACCENT):
        panel = ctk.CTkFrame(parent, fg_color=PANEL, corner_radius=12, border_width=1, border_color=BORDER)
        panel.pack(fill="x", pady=5)
        row = ctk.CTkFrame(panel, fg_color="transparent")
        row.pack(fill="x", padx=15, pady=(12, 6))
        ctk.CTkLabel(row, text=title, text_color=TEXT, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left")
        ctk.CTkLabel(row, text=f"{percent:.1f}%", text_color=color, font=ctk.CTkFont(size=12, weight="bold")).pack(side="right")
        bar = ctk.CTkProgressBar(panel, height=8, progress_color=color, fg_color="#252c39")
        bar.pack(fill="x", padx=15, pady=(0, 6))
        bar.set(max(0, min(percent, 100)) / 100)
        ctk.CTkLabel(panel, text=detail, text_color=MUTED, font=ctk.CTkFont(size=10)).pack(anchor="w", padx=15, pady=(0, 12))
        return panel

    def page_overview(self):
        data = collect_snapshot()
        intro = ctk.CTkFrame(self.content, fg_color="transparent")
        intro.pack(fill="x", pady=(0, 10))
        ctk.CTkLabel(intro, text="System overview", text_color=TEXT, font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w")
        ctk.CTkLabel(intro, text=f"{data['computer']}  /  {data['os']}  /  Uptime {data['uptime']}", text_color=MUTED, font=ctk.CTkFont(size=11)).pack(anchor="w", pady=(3, 0))
        cards = ctk.CTkFrame(self.content, fg_color="transparent")
        cards.pack(fill="x")
        for col in range(4): cards.grid_columnconfigure(col, weight=1, uniform="cards")
        card_data = [
            ("CPU load", f"{data['cpu']:.1f}%", f"{data['cpu_cores']} physical cores", ACCENT),
            ("Memory", f"{data['ram_percent']:.1f}%", f"{data['ram_used']} / {data['ram_total']} GB used", GREEN),
            ("System drive", f"{data['disk_percent']:.1f}%", f"{data['disk_free']} GB free", YELLOW if data['disk_percent'] >= 85 else ACCENT),
            ("Processes", str(len(list(psutil.process_iter()))), "Currently detected", GREEN),
        ]
        for i, (title, value, detail, color) in enumerate(card_data):
            self.card(cards, title, value, detail, color).grid(row=0, column=i, sticky="nsew", padx=5, pady=5)
        columns = ctk.CTkFrame(self.content, fg_color="transparent")
        columns.pack(fill="x", pady=(14, 0))
        columns.grid_columnconfigure(0, weight=1, uniform="columns")
        columns.grid_columnconfigure(1, weight=1, uniform="columns")
        left = ctk.CTkFrame(columns, fg_color="transparent")
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        right = ctk.CTkFrame(columns, fg_color="transparent")
        right.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        self.section_label(left, "Resource utilization", "A current snapshot of your main system resources")
        self.progress_panel(left, "CPU", data["cpu"], "Processor activity at the time of scan", RED if data["cpu"] >= 90 else ACCENT)
        self.progress_panel(left, "RAM", data["ram_percent"], f"{data['ram_available']} GB available", RED if data["ram_percent"] >= 90 else GREEN)
        self.progress_panel(left, "System drive", data["disk_percent"], f"{data['disk_free']} GB free of {data['disk_total']} GB", RED if data["disk_percent"] >= 95 else YELLOW)
        self.section_label(right, "Quick actions", "Run a scan or open a focused tool")
        for label, desc, command in [
            ("Run full diagnostic", "Check CPU, RAM, disk and battery", lambda: self.show_page("Diagnostics")),
            ("Inspect processes", "Find applications using system resources", lambda: self.show_page("Processes")),
            ("Export system report", "Save a report for troubleshooting", lambda: self.save_report("txt")),
            ("View hardware details", "Processor, memory, OS and storage", lambda: self.show_page("Hardware")),
        ]:
            button = ctk.CTkButton(right, text=label + "   ›", anchor="w", height=38, fg_color=PANEL, hover_color=PANEL_ALT, border_width=1, border_color=BORDER, command=command)
            button.pack(fill="x", pady=4)
            ctk.CTkLabel(right, text=desc, text_color=MUTED, font=ctk.CTkFont(size=10)).pack(anchor="w", padx=8, pady=(0, 4))
        self.section_label(self.content, "Latest health signals", "Automated checks based on the current snapshot")
        for level, title, advice in build_diagnostics(data):
            self.finding_row(self.content, level, title, advice)

    def finding_row(self, parent, level, title, advice):
        color = GREEN if level == "OK" else (RED if level == "CRITICAL" else YELLOW)
        row = ctk.CTkFrame(parent, fg_color=PANEL, corner_radius=10, border_width=1, border_color=BORDER)
        row.pack(fill="x", pady=4)
        ctk.CTkLabel(row, text=level, width=86, text_color=color, font=ctk.CTkFont(size=10, weight="bold")).pack(side="left", padx=12, pady=12)
        body = ctk.CTkFrame(row, fg_color="transparent")
        body.pack(side="left", fill="x", expand=True, padx=(0, 12), pady=10)
        ctk.CTkLabel(body, text=title, text_color=TEXT, font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w")
        ctk.CTkLabel(body, text=advice, text_color=MUTED, font=ctk.CTkFont(size=10), wraplength=760, justify="left").pack(anchor="w", pady=(2, 0))

    def page_diagnostics(self):
        self.section_label(self.content, "Diagnostic scan", "Checks are advisory and reflect a snapshot, not a hardware certification.")
        actions = ctk.CTkFrame(self.content, fg_color="transparent")
        actions.pack(fill="x", pady=8)
        ctk.CTkButton(actions, text="Run scan now", height=40, fg_color=ACCENT, hover_color="#5675e5", command=self.run_diagnostics).pack(side="left")
        ctk.CTkButton(actions, text="Save report", height=40, fg_color=PANEL_ALT, hover_color=BORDER, command=lambda: self.save_report("html")).pack(side="left", padx=8)
        self.diag_results = ctk.CTkFrame(self.content, fg_color="transparent")
        self.diag_results.pack(fill="x")
        self.run_diagnostics()

    def run_diagnostics(self):
        for child in self.diag_results.winfo_children(): child.destroy()
        data = collect_snapshot()
        findings = build_diagnostics(data)
        critical = sum(1 for item in findings if item[0] == "CRITICAL")
        warnings = sum(1 for item in findings if item[0] == "WARNING")
        summary = ctk.CTkFrame(self.diag_results, fg_color=PANEL, corner_radius=12, border_width=1, border_color=BORDER)
        summary.pack(fill="x", pady=(4, 12))
        ctk.CTkLabel(summary, text=f"{len(findings)} checks completed", text_color=TEXT, font=ctk.CTkFont(size=17, weight="bold")).pack(anchor="w", padx=16, pady=(14, 3))
        ctk.CTkLabel(summary, text=f"{critical} critical  •  {warnings} warnings  •  {len(findings)-critical-warnings} normal", text_color=RED if critical else (YELLOW if warnings else GREEN), font=ctk.CTkFont(size=12)).pack(anchor="w", padx=16, pady=(0, 14))
        for level, title, advice in findings: self.finding_row(self.diag_results, level, title, advice)
        self.last_diagnostics = (data, findings)

    def page_processes(self):
        self.section_label(self.content, "Process manager", "Inspect running processes. Terminating a process can cause unsaved work to be lost.")
        controls = ctk.CTkFrame(self.content, fg_color="transparent")
        controls.pack(fill="x", pady=(6, 10))
        self.process_search = ctk.CTkEntry(controls, placeholder_text="Search by process name or PID", height=38, width=300)
        self.process_search.pack(side="left")
        ctk.CTkButton(controls, text="Refresh", width=90, height=38, command=self.refresh_processes).pack(side="left", padx=8)
        ctk.CTkButton(controls, text="Terminate selected", height=38, fg_color="#542630", hover_color="#75313d", command=self.terminate_selected).pack(side="right")
        self.process_summary = ctk.CTkLabel(self.content, text="", text_color=MUTED, font=ctk.CTkFont(size=11))
        self.process_summary.pack(anchor="w", pady=(0, 8))
        self.process_table = ctk.CTkTextbox(self.content, height=450, fg_color=PANEL, text_color=TEXT, border_width=1, border_color=BORDER, font=ctk.CTkFont(family="Consolas", size=11), wrap="none")
        self.process_table.pack(fill="both", expand=True)
        self.refresh_processes()

    def refresh_processes(self):
        if not hasattr(self, "process_table") or not self.process_table.winfo_exists(): return
        keyword = self.process_search.get().strip().lower() if hasattr(self, "process_search") else ""
        rows = []
        for proc in psutil.process_iter(["pid", "name", "username", "memory_percent", "status"]):
            try:
                info = proc.info
                name = info.get("name") or "Unknown"
                pid = info.get("pid")
                if keyword and keyword not in name.lower() and keyword not in str(pid): continue
                rows.append({"pid": pid, "name": name, "user": info.get("username") or "-", "ram": info.get("memory_percent") or 0, "status": info.get("status") or "unknown"})
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        rows.sort(key=lambda item: item["ram"], reverse=True)
        self.process_rows = rows
        self.process_table.configure(state="normal")
        self.process_table.delete("1.0", "end")
        self.process_table.insert("end", f"{'PID':<9}{'RAM %':<10}{'STATUS':<15}{'PROCESS NAME':<34}{'USER'}\n")
        self.process_table.insert("end", "─" * 100 + "\n")
        for row in rows[:250]:
            self.process_table.insert("end", f"{row['pid']:<9}{row['ram']:<10.2f}{row['status']:<15}{row['name'][:32]:<34}{row['user']}\n")
        self.process_table.configure(state="disabled")
        self.process_summary.configure(text=f"{len(rows)} matching processes • sorted by RAM usage • showing up to 250")

    def terminate_selected(self):
        selected = self.process_table.get("insert linestart", "insert lineend").strip() if hasattr(self, "process_table") else ""
        parts = selected.split()
        if not parts or not parts[0].isdigit():
            messagebox.showinfo("Select a process", "Click a process row in the table first, then choose Terminate selected.")
            return
        pid = int(parts[0])
        if pid == os.getpid():
            messagebox.showwarning("Not allowed", "The diagnostic tool cannot terminate itself.")
            return
        if not messagebox.askyesno("Confirm termination", f"Request termination of PID {pid}? Unsaved work in that process may be lost."):
            return
        try:
            process = psutil.Process(pid)
            process.terminate()
            try: process.wait(timeout=3)
            except psutil.TimeoutExpired: process.kill()
            messagebox.showinfo("Process action", f"Termination request sent for PID {pid}.")
        except psutil.NoSuchProcess:
            messagebox.showinfo("Process ended", "That process is no longer running.")
        except psutil.AccessDenied:
            messagebox.showerror("Access denied", "Windows denied access. Some processes require elevated permissions.")
        except Exception as error:
            messagebox.showerror("Unable to terminate", str(error))
        self.refresh_processes()

    def page_hardware(self):
        data = collect_snapshot()
        self.section_label(self.content, "Hardware & operating system", "Information reported by the operating system and psutil")
        groups = [
            ("SYSTEM", [("Computer name", data["computer"]), ("Operating system", data["os"]), ("Architecture", platform.machine()), ("Platform", platform.platform()), ("Boot time", datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")), ("Uptime", data["uptime"])]),
            ("PROCESSOR", [("Processor", data["cpu_name"]), ("Physical cores", str(data["cpu_cores"])), ("Logical processors", str(data["logical_cpus"])), ("Current frequency", self.cpu_frequency()), ("CPU usage", f"{data['cpu']:.1f}%")]),
            ("MEMORY & STORAGE", [("Installed RAM", f"{data['ram_total']} GB"), ("Available RAM", f"{data['ram_available']} GB"), ("Swap total", f"{data['swap_total']} GB"), ("System drive total", f"{data['disk_total']} GB"), ("System drive free", f"{data['disk_free']} GB"), ("Python version", data["python"])]),
        ]
        for title, items in groups:
            panel = ctk.CTkFrame(self.content, fg_color=PANEL, corner_radius=12, border_width=1, border_color=BORDER)
            panel.pack(fill="x", pady=6)
            ctk.CTkLabel(panel, text=title, text_color=ACCENT, font=ctk.CTkFont(size=10, weight="bold")).pack(anchor="w", padx=16, pady=(14, 8))
            for label, value in items:
                row = ctk.CTkFrame(panel, fg_color="transparent")
                row.pack(fill="x", padx=16, pady=5)
                ctk.CTkLabel(row, text=label, text_color=MUTED, font=ctk.CTkFont(size=11)).pack(side="left")
                ctk.CTkLabel(row, text=value, text_color=TEXT, font=ctk.CTkFont(size=11), wraplength=600).pack(side="right")
            ctk.CTkFrame(panel, height=8, fg_color="transparent").pack()
        ctk.CTkLabel(self.content, text="GPU, motherboard and temperature data depend on driver, Windows version, and hardware support. Missing values do not necessarily indicate a fault.", text_color=MUTED, wraplength=900, justify="left", font=ctk.CTkFont(size=10)).pack(anchor="w", pady=10)

    def cpu_frequency(self):
        try:
            freq = psutil.cpu_freq()
            return f"{freq.current:.0f} MHz" if freq else "Not reported"
        except Exception:
            return "Not available"

    def page_network(self):
        self.section_label(self.content, "Network diagnostics", "Local interface information and a lightweight connectivity check")
        net = psutil.net_io_counters()
        if net:
            cards = ctk.CTkFrame(self.content, fg_color="transparent")
            cards.pack(fill="x")
            for i, (title, value, detail, color) in enumerate([
                ("Data sent", f"{gb(net.bytes_sent * 1.0 / 1)} GB", "Since system counters started", ACCENT),
                ("Data received", f"{gb(net.bytes_recv * 1.0 / 1)} GB", "Since system counters started", GREEN),
                ("Packets sent", f"{net.packets_sent:,}", f"Errors: {net.errout}", YELLOW),
                ("Packets received", f"{net.packets_recv:,}", f"Errors: {net.errin}", GREEN),
            ]):
                cards.grid_columnconfigure(i, weight=1, uniform="net")
                self.card(cards, title, value, detail, color).grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
        ctk.CTkButton(self.content, text="Test internet connectivity", height=40, command=self.test_connection).pack(anchor="w", pady=12)
        self.network_result = ctk.CTkLabel(self.content, text="", text_color=MUTED, justify="left", font=ctk.CTkFont(size=12))
        self.network_result.pack(anchor="w", pady=5)
        self.section_label(self.content, "Network interfaces")
        box = ctk.CTkTextbox(self.content, height=280, fg_color=PANEL, border_width=1, border_color=BORDER, text_color=TEXT, font=ctk.CTkFont(family="Consolas", size=11))
        box.pack(fill="x")
        for interface, addresses in psutil.net_if_addrs().items():
            box.insert("end", f"{interface}\n")
            for address in addresses:
                box.insert("end", f"    {address.family}: {address.address}\n")
                if address.netmask: box.insert("end", f"    Netmask: {address.netmask}\n")
            box.insert("end", "\n")
        box.configure(state="disabled")

    def test_connection(self):
        self.network_result.configure(text="Testing connection to www.google.com ...", text_color=YELLOW)
        self.update_idletasks()
        start = time.perf_counter()
        try:
            with socket.create_connection(("www.google.com", 443), timeout=4): pass
            elapsed = (time.perf_counter() - start) * 1000
            self.network_result.configure(text=f"CONNECTED  •  HTTPS connection succeeded  •  Approx. connection setup: {elapsed:.0f} ms\nThis is not a full internet speed test.", text_color=GREEN)
        except OSError:
            self.network_result.configure(text="CONNECTION FAILED  •  Could not reach the test host. Check Wi-Fi, router, DNS, firewall, or internet service.", text_color=RED)

    def page_file_tools(self):
        self.section_label(self.content, "File & storage tools", "These tools inspect files; they do not delete or modify your personal files.")
        panel = ctk.CTkFrame(self.content, fg_color=PANEL, corner_radius=12, border_width=1, border_color=BORDER)
        panel.pack(fill="x", pady=8)
        ctk.CTkLabel(panel, text="Folder analyzer", text_color=TEXT, font=ctk.CTkFont(size=15, weight="bold")).pack(anchor="w", padx=16, pady=(16, 4))
        ctk.CTkLabel(panel, text="Count files and folders, calculate folder size, and group file extensions.", text_color=MUTED, font=ctk.CTkFont(size=11)).pack(anchor="w", padx=16, pady=(0, 12))
        ctk.CTkButton(panel, text="Choose folder and analyze", height=40, command=self.analyze_folder).pack(anchor="w", padx=16, pady=(0, 16))
        self.folder_results = ctk.CTkTextbox(self.content, height=300, fg_color=PANEL, border_width=1, border_color=BORDER, text_color=TEXT, font=ctk.CTkFont(family="Consolas", size=11))
        self.folder_results.pack(fill="both", expand=True, pady=8)

    def analyze_folder(self):
        folder = filedialog.askdirectory(title="Choose a folder to analyze")
        if not folder: return
        count_files = 0
        count_dirs = 0
        total_size = 0
        extensions = {}
        errors = 0
        for current, dirs, names in os.walk(folder):
            count_dirs += len(dirs)
            for name in names:
                path = os.path.join(current, name)
                try:
                    total_size += os.path.getsize(path)
                    count_files += 1
                    ext = Path(name).suffix.lower() or "[no extension]"
                    extensions[ext] = extensions.get(ext, 0) + 1
                except (OSError, PermissionError):
                    errors += 1
        output = ["FOLDER ANALYSIS", "=" * 60, f"Path: {folder}", f"Files: {count_files:,}", f"Subfolders: {count_dirs:,}", f"Total size: {gb(total_size * 1.0)} GB ({mb(total_size):,.2f} MB)", f"Files skipped due to access errors: {errors}", "", "FILE TYPES (most common first)", "-" * 60]
        for ext, count in sorted(extensions.items(), key=lambda item: item[1], reverse=True)[:40]: output.append(f"{ext:<22} {count:>8,}")
        self.folder_results.configure(state="normal")
        self.folder_results.delete("1.0", "end")
        self.folder_results.insert("end", "\n".join(output))
        self.folder_results.configure(state="disabled")

    def page_reports(self):
        self.section_label(self.content, "Reports & history", "Reports are saved locally on this computer.")
        ctk.CTkLabel(self.content, text=f"Default location: {REPORT_DIR}", text_color=MUTED, font=ctk.CTkFont(size=11), wraplength=900).pack(anchor="w", pady=(0, 12))
        row = ctk.CTkFrame(self.content, fg_color="transparent")
        row.pack(fill="x", pady=4)
        ctk.CTkButton(row, text="Export TXT report", height=42, command=lambda: self.save_report("txt")).pack(side="left", padx=(0, 8))
        ctk.CTkButton(row, text="Export HTML report", height=42, fg_color=PANEL_ALT, hover_color=BORDER, command=lambda: self.save_report("html")).pack(side="left", padx=8)
        ctk.CTkButton(row, text="Export CSV snapshot", height=42, fg_color=PANEL_ALT, hover_color=BORDER, command=lambda: self.save_report("csv")).pack(side="left", padx=8)
        ctk.CTkButton(row, text="Open report folder", height=42, fg_color=PANEL_ALT, hover_color=BORDER, command=lambda: os.startfile(REPORT_DIR) if platform.system() == "Windows" else webbrowser.open(REPORT_DIR.as_uri())).pack(side="left", padx=8)
        self.section_label(self.content, "Recent reports")
        self.report_list = ctk.CTkFrame(self.content, fg_color="transparent")
        self.report_list.pack(fill="x")
        self.refresh_report_list()

    def refresh_report_list(self):
        if not hasattr(self, "report_list") or not self.report_list.winfo_exists(): return
        for child in self.report_list.winfo_children(): child.destroy()
        files = sorted(REPORT_DIR.glob("*"), key=lambda path: path.stat().st_mtime, reverse=True)
        if not files:
            ctk.CTkLabel(self.report_list, text="No reports yet. Export a report to get started.", text_color=MUTED).pack(anchor="w", pady=8)
        for path in files[:15]:
            row = ctk.CTkFrame(self.report_list, fg_color=PANEL, corner_radius=8)
            row.pack(fill="x", pady=3)
            ctk.CTkLabel(row, text=path.name, text_color=TEXT, font=ctk.CTkFont(size=11)).pack(side="left", padx=12, pady=10)
            ctk.CTkLabel(row, text=datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M"), text_color=MUTED, font=ctk.CTkFont(size=10)).pack(side="right", padx=12)

    def save_report(self, file_type="txt"):
        data = collect_snapshot()
        findings = build_diagnostics(data)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base = f"pc_diagnostic_report_{stamp}"
        try:
            if file_type == "csv":
                path = REPORT_DIR / f"{base}.csv"
                with path.open("w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Metric", "Value"])
                    for key, value in data.items(): writer.writerow([key, value])
                    writer.writerow([]); writer.writerow(["Severity", "Finding", "Recommendation"])
                    writer.writerows(findings)
            elif file_type == "html":
                path = REPORT_DIR / f"{base}.html"
                rows = "".join(f"<tr><td>{key.replace('_',' ').title()}</td><td>{value}</td></tr>" for key, value in data.items())
                finding_rows = "".join(f"<tr><td>{level}</td><td>{title}</td><td>{advice}</td></tr>" for level, title, advice in findings)
                html = f"""<!doctype html><html><head><meta charset="utf-8"><title>PC Diagnostic Report</title><style>body{{font-family:Arial,sans-serif;background:#0b0d12;color:#edf2fb;margin:40px}}h1,h2{{color:#8ba2ff}}table{{border-collapse:collapse;width:100%;margin:18px 0 30px}}td,th{{padding:10px;border:1px solid #2a3242;text-align:left}}th{{background:#1a2130}}tr:nth-child(even){{background:#121722}}.meta{{color:#a5b0c4}}</style></head><body><h1>NEXUS PC Diagnostic Report</h1><p class="meta">Generated {data['time']} • {data['computer']}</p><h2>System snapshot</h2><table><tr><th>Metric</th><th>Value</th></tr>{rows}</table><h2>Diagnostic findings</h2><table><tr><th>Severity</th><th>Finding</th><th>Recommendation</th></tr>{finding_rows}</table><p class="meta">This report is an informational snapshot, not a hardware certification.</p></body></html>"""
                path.write_text(html, encoding="utf-8")
            else:
                path = REPORT_DIR / f"{base}.txt"
                lines = ["NEXUS PC DIAGNOSTIC REPORT", "=" * 64, f"Generated: {data['time']}", "", "SYSTEM SNAPSHOT", "-" * 64]
                lines.extend(f"{key.replace('_', ' ').title():<24}: {value}" for key, value in data.items())
                lines += ["", "DIAGNOSTIC FINDINGS", "-" * 64]
                lines.extend(f"[{level}] {title}\n  Recommendation: {advice}" for level, title, advice in findings)
                lines += ["", "Note: Findings are advisory and based on a single snapshot."]
                path.write_text("\n".join(lines), encoding="utf-8")
            messagebox.showinfo("Report exported", f"Report saved successfully:\n{path}")
            if self.current_page == "Reports": self.refresh_report_list()
        except OSError as error:
            messagebox.showerror("Export failed", f"Could not save the report.\n{error}")

    def refresh_dashboard(self):
        if not self.winfo_exists(): return
        if self.current_page == "Overview":
            # Keep the overview current without blocking the UI for long intervals.
            pass
        self.after(5000, self.refresh_dashboard)

    def on_close(self):
        self.monitoring = False
        self.destroy()


if __name__ == "__main__":
    app = DiagnosticApp()
    app.mainloop()
