import socket
import struct

def main(controller_ip, switch_dpid,switch_port,threshold):
    packet_in_count = 0

    # Create a socket to listen for OpenFlow messages
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', switch_port))
    s.listen(5)

   #print(f"Monitoring switch IP: {switch_ip}, port: {switch_port}. Waiting for OpenFlow messages...")

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)

        # Extract OpenFlow header and message type
        of_header = struct.unpack('!BBHLL', data[:8])
        of_type = of_header[1]
        of_switch_ip = addr[0]

        if of_type == 10 and of_switch_ip == switch_ip:  # Packet_In message (OpenFlow 1.3)
            packet_in_count += 1

            if packet_in_count > threshold:
                print("")
                break

    print("Monitoring stopped.")

if __name__ == '__main__':
    controller_ip = '10.224.78.5'  # Controller IP
    switch_dpid = '0000000000000001'  # Switch IP
    switch_port = 6633  # Switch port
    threshold = 100  # Set the threshold

    main(controller_ip, switch_ip, switch_port, threshold)
