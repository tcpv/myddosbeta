import socket
import time
import threading

# Configuration
server_ip = '5.252.101.227'
server_port = 7777
number_of_clients = 100
delay_between_connections = 0.1  # seconds

# Function to simulate a client
def simulate_client(client_id)
    try
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        
        # Example of a SAMP payload
        header = b'SAMP'
        ip = socket.inet_aton(server_ip)
        port = server_port.to_bytes(2, byteorder='big')
        query_type = b'i'  # 'i' for server info query

        payload = header + ip + port + query_type

        # Send payload to server
        sock.sendto(payload, (server_ip, server_port))

        # Receive response from server
        response, _ = sock.recvfrom(1024)
        print(f'Client {client_id} received {response}')

    except Exception as e
        print(f'Client {client_id} error {e}')
    finally
        sock.close()

# Creating and starting threads to simulate multiple clients
threads = []
for i in range(number_of_clients)
    thread = threading.Thread(target=simulate_client, args=(i,))
    threads.append(thread)
    thread.start()
    time.sleep(delay_between_connections)

# Wait for all threads to finish
for thread in threads
    thread.join()

print(Stress test completed.)