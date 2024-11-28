import socket  # Importing the socket library to handle network connections.

# Function to scan a single port on a target system
def scan_port(ip, port):
    """
    Scans a single port to check if it's open.
    """
    try:
        # Create a new socket object for the connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout of 1 second to prevent the scan from hanging
        sock.settimeout(1)
        
        # Attempt to connect to the target IP and port
        # connect_ex returns 0 if the connection is successful (port is open)
        result = sock.connect_ex((ip, port))
        
        # Close the socket after the attempt
        sock.close()
        
        # Return True if the port is open (result == 0)
        return result == 0
    except Exception as e:
        # If an error occurs (e.g., invalid IP), treat the port as closed
        return False

# Function to scan multiple ports and report which are open
def scan_ports(ip, ports):
    """
    Scans a list of ports on a given IP address.
    """
    print(f"\nScanning {ip} for open ports...\n")  # Inform the user that scanning has started
    open_ports = []  # List to store ports that are open

    # Loop through each port in the list of ports to scan
    for port in ports:
        # Check if the current port is open using the scan_port function
        if scan_port(ip, port):
            # If open, add the port to the open_ports list
            open_ports.append(port)

            # Try to get the service name for the port (e.g., HTTP for port 80)
            service = socket.getservbyport(port, "tcp") if port in range(1, 65536) else "Unknown"

            # Print the result for the user
            print(f"Port {port} is open (Service: {service})")
        else:
            # If the port is closed, notify the user
            print(f"Port {port} is closed")

    # After scanning all ports, summarize the results
    if open_ports:
        print(f"\nScan complete. Open ports: {open_ports}")  # List open ports if any are found
    else:
        print("\nScan complete. No open ports detected.")  # Notify if no open ports are found

    return open_ports  # Return the list of open ports

# Main program entry point
if __name__ == "__main__":
    # Ask the user to enter a target hostname or IP address
    target = input("Enter the target IP address or hostname: ")

    # Attempt to resolve the hostname to an IP address
    try:
        target_ip = socket.gethostbyname(target)  # Convert hostname to IP
    except socket.gaierror:
        # If the hostname is invalid or cannot be resolved, exit the program
        print("Invalid IP address or hostname.")
        exit()

    # Define a list of common ports to scan
    # These are commonly used ports like HTTP (80), HTTPS (443), SSH (22), etc.
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389]

    # Call the scan_ports function to scan the target IP on the defined ports
    scan_ports(target_ip, common_ports)
