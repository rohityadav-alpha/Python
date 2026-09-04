import os # [inbuilt module]
import sys # [inbuilt module] Python runtime state access ke liye

def get_resource_path(relative_path): # [def keyword] Final PROUSB logic
# [hasattr inbuilt function] Check karta hai ki '_MEIPASS' attribute sys me hai ya nahi
    if hasattr(sys, '_MEIPASS'):
# PyInstaller .exe execution mode:
        return os.path.join(sys._MEIPASS, relative_path)
# Normal development execution mode:
    return os.path.join(os.path.abspath(""), relative_path)

# Test execution:
print("Templates Dir:", get_resource_path("templates"))
print("App Icon File:", get_resource_path("app.ico"))     