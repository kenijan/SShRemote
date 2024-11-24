import pexpect

# ANSI escape sequences for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def get_user_input(prompt, default_value):
    # Prompt the user and return either the input or the default if empty
    user_input = input(f"{Colors.OKBLUE}{prompt} (default: {default_value}): {Colors.ENDC}")
    return user_input if user_input else default_value


def ssh_connect(ip, port, username, password):
    ssh_command = f"ssh -p {port} {username}@{ip}"
    print(ssh_command)
    child = pexpect.spawn(ssh_command)
    try:
        # Look for authenticity prompt and respond with "yes"
        i = child.expect(["Are you sure you want to continue connecting", "password:", pexpect.EOF, pexpect.TIMEOUT],
                         timeout=10)

        if i == 0:
            # Accept the authenticity of the host
            child.sendline("yes")
            # Look for the password prompt after saying "yes"
            child.expect("password:", timeout=10)

        if i == 1 or i == 0:
            # Send the password
            child.sendline(password)
            # Hand over to interactive mode
            print(f"{Colors.OKGREEN}Successfully connected to {ip} as {username}!{Colors.ENDC}")
            child.interact()

    except pexpect.EOF:
        print(f"{Colors.FAIL}SSH session terminated unexpectedly.{Colors.ENDC}")
    except pexpect.TIMEOUT:
        print(f"{Colors.WARNING}Connection timed out.{Colors.ENDC}")


# Gather user inputs with defaults if blank
ip_address = get_user_input("Enter Termux IP address")
port = int(get_user_input("Enter SSH port"))
username = get_user_input("Enter SSH username")
password = get_user_input("Enter SSH password")

# Connect with the specified or default values
ssh_connect(ip_address, port, username, password)
