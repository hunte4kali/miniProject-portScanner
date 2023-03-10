import sys
from datetime import datetime
import socket

# define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # converting target name to ipv4
else:
    print("Invalid amount of arguments!")
    print("Command Syntax: python3 PortScanner.py <ip>")
time= str(datetime.now())
# banner
print("X" * 70)
print(" " * 70)
print(f"   Scanning {target} for open port")
print(f"   Time started: {time}")
print(" " * 70)
print("X" * 70)



try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # return
        if result == 0:
            print(f" [+] {port} is open")
            s.close()
except KeyboardInterrupt:
    print("\nExiting program")
    exit()
except socket.gaierror:
    print("Host can't be resolved")
    exit()
except socket.error:
    print("Can't connect to the server")
    exit()
