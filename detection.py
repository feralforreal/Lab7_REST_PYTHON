import socket
import struct

def main(datapath_id, threshold):
    packet_in_count = 0

    # Create a socket to listen for OpenFlow messages
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 6633))  # Listen on port 6633 (typical OpenFlow port)
    s.listen(5)

    print("Monitoring Datapath ID: {}. Waiting for OpenFlow messages...".format(datapath_id))

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)

        # Extract OpenFlow header and message type
        of_header = struct.unpack('!BBHLL', data[:8])
        of_type = of_header[1]
        of_datapath_id = of_header[2]

        if of_type == 10 and of_datapath_id == datapath_id:  # Packet_In message (OpenFlow 1.3)
            packet_in_count += 1

            if packet_in_count > threshold:
                print("Threshold ({}) exceeded: More than {} Packet_In messages received for Datapath ID {}".format(threshold, threshold, datapath_id))
                break

    print("Monitoring stopped.")

if __name__ == '__main__':
    datapath_id = 0000000000000001  # Replace with the actual Datapath ID of the switch you want to monitor
    threshold = 100  # Set the threshold

    main(datapath_id, threshold)
