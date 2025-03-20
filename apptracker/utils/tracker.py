from __future__ import print_function
import sys
from apptracker.utils.linux import LinuxWindowTracker

if sys.platform in ["Windows", "win32", "cygwin"]:
    import win32gui
    import uiautomation as auto
elif sys.platform in ["Mac", "darwin", "os2", "os2emx"]:
    from AppKit import NSWorkspace
    from Foundation import *


def get_active_window_name():
    if sys.platform in ["Windows", "win32", "cygwin"]:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    elif sys.platform.startswith("linux"):
        window = LinuxWindowTracker.active_window()
        return window["title"] if window else "Unknown"
    elif sys.platform in ["Mac", "darwin", "os2", "os2emx"]:
        active_window_name = NSWorkspace.sharedWorkspace().activeApplication()[
            "NSApplicationName"
        ]
        return "Unknown" if active_window_name is None else active_window_name
    else:
        print(f"Unsupported platform: {sys.platform}")
        return None
