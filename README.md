# Honey-Sentry

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat)
![License](https://img.shields.io/badge/License-MIT-green)

Honey-Sentry is a lightweight, Python-based Deception Technology tool designed for Blue Team operations. It deploys a honeytoken (decoy file) on the system and performs real-time File Integrity Monitoring (FIM) to detect unauthorized access, lateral movement, or ransomware activity.

Unlike traditional Intrusion Detection Systems (IDS) that rely on signatures, Honey-Sentry relies on behavioral analysis: legitimate users have no reason to access the decoy file. Any interaction with it is considered a high-fidelity Indicator of Compromise (IoC).

## Key Features

* **Automated Deployment:** Automatically generates a realistic-looking honeytoken (default: `server_root_credentials.txt`) upon startup.
* **Real-Time Surveillance:** Utilizes the `watchdog` library to monitor file system events (Modification, Deletion, Renaming) instantaneously.
* **Ransomware Detection:** Capable of detecting file deletion or encryption attempts, simulating early-warning signals for ransomware attacks.
* **Low False Positives:** Monitors only the specific trap file, ensuring that normal system operations do not trigger false alarms.
* **Cross-Platform:** Compatible with Windows, Linux, and macOS.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Honey-Sentry.git](https://github.com/YOUR_USERNAME/Honey-Sentry.git)
    cd Honey-Sentry
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script using Python. The tool will create the trap file and enter monitoring mode immediately.

```bash
python main.py
Example Output
Plaintext

[+] Honeytoken file created: server_root_credentials.txt
[+] Monitoring started. Directory: /home/user/projects/Honey-Sentry
[+] Honey-Sentry is active and waiting... (Press CTRL+C to stop)
Simulation
To test the functionality, simulate an attacker's behavior:

Start the tool.

Navigate to the project directory.

Open the newly created server_root_credentials.txt.

Modify the content and save, or delete the file entirely.

Alert Output:

Plaintext

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[!!!] CYBER ATTACK DETECTED [!!!]
[*] Event Type:  MODIFICATION
[*] Target File: .\server_root_credentials.txt
[*] Timestamp:   Fri Nov 28 16:20:00 2025
[*] Action:      Log sent to Security Operations Center (SOC).
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Project Structure
Plaintext

Honey-Sentry/
├── main.py                 # Core detection logic and event handling
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignored files
