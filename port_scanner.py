import socket
from datetime import datetime

# Ask the user for the target
target = input("Enter the IP address or hostname to scan: ")

# Port range
start_port = 1
end_port = 1024

print(f"\nScanning {target} from port {start_port} to {end_port}...")
start_time = datetime.now()

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nScan stopped by user.")
except socket.gaierror:
    print("Hostname could not be resolved.")
except socket.error:
    print("Couldn't connect to server.")

end_time = datetime.now()
duration = end_time - start_time
print(f"\nScanning completed in: {duration}")
