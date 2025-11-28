import sys
import time
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
HONEY_FILE = "server_root_credentials.txt"  # The name of our trap file
MONITOR_DIR = "."  # Directory to monitor (Current directory)

class HoneyTrapHandler(FileSystemEventHandler):
    """
    Handles file system events.
    It triggers an alert only when the specific HONEY_FILE is interacted with.
    """
    
    def on_modified(self, event):
        if self._is_trap(event.src_path):
            self._trigger_alert("MODIFICATION", event.src_path)

    def on_deleted(self, event):
        if self._is_trap(event.src_path):
            self._trigger_alert("DELETION", event.src_path)
            print(f"[!] WARNING: Honeytoken file was deleted! Possible ransomware activity.")

    def on_moved(self, event):
        if self._is_trap(event.src_path):
            self._trigger_alert("RENAME", f"{event.src_path} -> {event.dest_path}")

    def _is_trap(self, path):
        """Checks if the event is related to our trap file."""
        # Using basename to match only the filename, ignoring the full path
        return os.path.basename(path) == HONEY_FILE

    def _trigger_alert(self, action, path):
        """Generates an alert when intrusion is detected."""
        print("\n" + "!"*50)
        print(f"[!!!] CYBER ATTACK DETECTED [!!!]")
        print(f"[*] Event Type:  {action}")
        print(f"[*] Target File: {path}")
        print(f"[*] Timestamp:   {time.ctime()}")
        print(f"[*] Action:      Log sent to Security Operations Center (SOC).")
        print("!"*50 + "\n")

class HoneyDeception:
    """
    Main class to deploy the trap and manage the monitoring process.
    """
    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename
        self.filepath = os.path.join(directory, filename)

    def deploy_trap(self):
        """Creates the fake honeytoken file."""
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                f.write("# RESTRICTED ACCESS\n")
                f.write("# This file contains root credentials for the production server.\n")
                f.write("Username: root\nPassword: SuperSecretPassword123!")
            print(f"[+] Honeytoken file created: {self.filename}")
        else:
            print(f"[i] Honeytoken file already exists: {self.filename}")

    def start_monitoring(self):
        """Starts the directory monitoring loop."""
        print(f"[+] Monitoring started. Directory: {os.path.abspath(self.directory)}")
        print(f"[+] Honey-Sentry is active and waiting... (Press CTRL+C to stop)")

        event_handler = HoneyTrapHandler()
        observer = Observer()
        observer.schedule(event_handler, self.directory, recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("\n[i] Monitoring stopped.")
        observer.join()

if __name__ == "__main__":
    # 1. Deploy the Trap
    trap = HoneyDeception(MONITOR_DIR, HONEY_FILE)
    trap.deploy_trap()
    
    # 2. Start Surveillance
    trap.start_monitoring()

