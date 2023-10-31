import argparse
import subprocess

def generate_traffic(start, end):
    # Replace 'controller_ip' with the actual IP address of your controller
    controller_ip = '10.224.78.5'
    
    for count in range(start, end + 1):
        # Send a PING request to the controller
        result = subprocess.Popen(['ping', '-c', '1', controller_ip], stdout=subprocess.PIPE)
        output, _ = result.communicate()
        output = output.decode('utf-8') if isinstance(output, bytes) else output
        print('Ping {}: {}'.format(count, output))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', type=int, default=1, help='Start count')
    parser.add_argument('-e', '--end', type=int, required=True, help='End count')
    args = parser.parse_args()

    generate_traffic(args.start, args.end)
