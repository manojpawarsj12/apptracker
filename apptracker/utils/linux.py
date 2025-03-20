import os
import re
import json
import subprocess
from typing import Dict, List, Optional, Any


class LinuxWindowTracker:

    @staticmethod
    def get_active_window_id() -> Optional[int]:
        try:
            output = subprocess.check_output(
                ["xprop", "-root", "\t$0", "_NET_ACTIVE_WINDOW"],
                env={**os.environ, "LC_ALL": "C.utf8"},
                universal_newlines=True,
            )
            return int(output.split("\t")[1], 16)
        except (subprocess.SubprocessError, IndexError, ValueError):
            return None

    @staticmethod
    def process_output(output: str) -> Dict[str, str]:
        """Process the output from xprop or xwininfo into a dictionary"""
        result = {}
        for row in output.strip().split("\n"):
            if "=" in row:
                key, value = row.split("=", 1)
                result[key.strip()] = value.strip()
            elif ":" in row:
                key, value = row.split(":", 1)
                result[key.strip()] = value.strip()
        return result

    @staticmethod
    def get_memory_usage_by_pid(pid: int) -> Optional[int]:
        """Get memory usage for a process by its PID"""
        try:
            with open(f"/proc/{pid}/statm", "r") as f:
                statm = f.read()
            return int(statm.split(" ")[1]) * 4096
        except (FileNotFoundError, IOError, IndexError, ValueError):
            return None

    @staticmethod
    def get_path_by_pid(pid: int) -> Optional[str]:
        """Get the executable path for a process by its PID"""
        try:
            return os.readlink(f"/proc/{pid}/exe")
        except (FileNotFoundError, IOError):
            return None

    @classmethod
    def get_window_information(cls, window_id: int) -> Optional[Dict[str, Any]]:
        """Get detailed window information by window ID"""
        try:
            # Get window properties
            xprop_output = subprocess.check_output(
                ["xprop", "-id", hex(window_id)],
                env={**os.environ, "LC_ALL": "C.utf8"},
                universal_newlines=True,
            )

            xwininfo_output = subprocess.check_output(
                ["xwininfo", "-id", hex(window_id)], universal_newlines=True
            )

            properties = cls.process_output(xprop_output)
            geometry = cls.process_output(xwininfo_output)

            pid_match = re.search(r"_NET_WM_PID\(CARDINAL\) = (\d+)", xprop_output)
            if not pid_match:
                return None

            process_id = int(pid_match.group(1))

            title_match = re.search(
                r'_NET_WM_NAME\(UTF8_STRING\) = "(.*)"', xprop_output
            )
            if not title_match:
                title_match = re.search(r'WM_NAME\(STRING\) = "(.*)"', xprop_output)

            title = title_match.group(1) if title_match else "Unknown"

            class_match = re.search(
                r'WM_CLASS\(STRING\) = "([^"]+)", "([^"]+)"', xprop_output
            )
            app_name = class_match.group(2) if class_match else "Unknown"

            # Create window information object
            window_info = {
                "platform": "linux",
                "title": title,
                "id": window_id,
                "owner": {
                    "name": app_name,
                    "processId": process_id,
                    "path": cls.get_path_by_pid(process_id),
                },
                "bounds": {
                    "x": int(geometry.get("Absolute upper-left X", 0)),
                    "y": int(geometry.get("Absolute upper-left Y", 0)),
                    "width": int(geometry.get("Width", 0)),
                    "height": int(geometry.get("Height", 0)),
                },
                "memoryUsage": cls.get_memory_usage_by_pid(process_id),
            }

            return window_info

        except (subprocess.SubprocessError, ValueError, AttributeError):
            return None

    @classmethod
    def active_window(cls) -> Optional[Dict[str, Any]]:
        """Get information about the currently active window"""
        window_id = cls.get_active_window_id()
        if not window_id:
            return None

        return cls.get_window_information(window_id)

    @classmethod
    def open_windows(cls) -> Optional[List[Dict[str, Any]]]:
        """Get information about all open windows"""
        try:
            output = subprocess.check_output(
                ["xprop", "-root", "_NET_CLIENT_LIST_STACKING"], universal_newlines=True
            )

            match = re.search(
                r"_NET_CLIENT_LIST_STACKING\(WINDOW\): window id # (.*)", output
            )
            if not match:
                return None

            window_ids_str = match.group(1)
            window_ids = [int(wid.strip(), 16) for wid in window_ids_str.split(",")]

            # Get information for each window
            windows = []
            for window_id in window_ids:
                window_info = cls.get_window_information(window_id)
                if window_info:
                    windows.append(window_info)

            return windows

        except (subprocess.SubprocessError, ValueError, AttributeError):
            return None
