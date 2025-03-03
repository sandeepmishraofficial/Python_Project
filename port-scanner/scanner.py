import sys
import socket
from datetime import datetime

# Check if the number of arguments is correct
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Get IP address from host name
else:
    print("Invalid arguments")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("_" * 50)
print("Scanning target " + target)
print("Time Started: " + str(datetime.now()))
print("_" * 50)

try:
    # Scan ports
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # Return an error indicator
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
except socket.gaierror:
    print("Hostname could not be resolved.")
except socket.error:
    print("Couldn't connect to server")
    sys.exit()
