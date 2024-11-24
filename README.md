# SSH Connection Script  

## Description  
This script facilitates SSH connections using Python's `pexpect` library. It allows users to connect to a remote server with a simple interactive interface. Default connection values are provided, but users can override them by entering their own details.

## Features  
- Handles SSH host authenticity checks automatically.  
- Securely sends the password for authentication.  
- Provides a color-coded user interface for better readability.  
- Interactive terminal session after a successful connection.  

## Requirements  
- Python 3.x  
- `pexpect` library (install with `pip install pexpect`)  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/kenijan/SSHRemote
   cd SSHRemote
   ```
2. Run file
   ```bash
      python sshremote.py
   ```
