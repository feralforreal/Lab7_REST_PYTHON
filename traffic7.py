import argparse
import subprocess

def generate_traffic(start, end, controller_ip):
    for count in range(start, end + 1):
        # Send a PING request to the controller
        result = subprocess.Popen(['ping', '-c', '1', controller_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        
        if "1 packets transmitted, 1 received, 0% packet loss" in output.decode('utf-8'):
            print('Sent 1 packet to {}, received 1, no packet loss'.format(controller_ip))
        else:
            print('Failed to send packet to {}, error: {}'.format(controller_ip, error.decode('utf-8')))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', type=int, default=1, help='Start count')
    parser.add_argument('-e', '--end', type=int, required=True, help='End count')
    parser.add_argument('controller_ip', type=str, help='Controller IP address')
    args = parser.parse_args()

    generate_traffic(args.start, args.end, args.controller_ip)
