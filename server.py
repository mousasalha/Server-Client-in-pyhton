import socket
import subprocess
import time

def lock_screen():
    subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
    pass

def handle_client(client_socket, student_id):
    if student_id in group_members:
        print(f"Received valid student ID: {student_id}")
        
        # Server-side message
        print("Server: OS will lock screen after 10 seconds")
        
        # Client-side message
        client_socket.send("Server: OS will lock screen after 10 seconds\n".encode())

        # Wait for 10 seconds
        time.sleep(10)

        # Lock the screen
        lock_screen()

        print("Server: Screen locked.")
    else:
        print(f"Invalid student ID or message: {student_id}")
        client_socket.send("Server: Invalid student ID or message\n".encode())

    # Close the client socket
    client_socket.close()

# Define the group members' student IDs
group_members = {'1213215', '1200825','1200163'}

# Ip address of server 

localhost='0.0.0.0'
# Create a TCP socket (intialize the socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a specific address and port
server_socket.bind(('localhost', 9955))

# Listen for incoming connections (max 1 connection in the queue)
server_socket.listen(1)
print("Server listening on port 9955...")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024).decode()

    # Extract student ID from the received data
    student_id = data.strip()

    # Handle the client request
    handle_client(client_socket, student_id)
