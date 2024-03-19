import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('192.0.0.1', 9955))

# enter student ID
student_id = input("enter yout id ")

# Send the student ID to the server
client_socket.send(student_id.encode())

# Receive and print the server's response
response = client_socket.recv(1024).decode()
print(response)

# Close the socket
client_socket.close()
