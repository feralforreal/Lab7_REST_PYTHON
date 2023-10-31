wqimport subprocess

def add_iptables_rule(controller_ip, controller_port, switch_dpid, switch_port):
    try:
        # Define the iptables rule to block traffic from the switch to the controller
        iptables_rule = "sudo iptables -A INPUT -s {0} -p tcp --sport {1} -d {2} --dport {3} -j DROP".format(
            switch_dpid, switch_port, controller_ip, controller_port)
        
        # Execute the iptables rule
        subprocess.call(iptables_rule, shell=True)
        
        print("Iptables rule added to block traffic from {0}:{1} to {2}:{3}.".format(switch_dpid, switch_port, controller_ip, controller_port))
    
    except Exception as e:
        print("An error occurred: {0}".format(e))

if __name__ == '__main__':
    controller_ip = '10.224.78.5'  # Replace with the controller's IP
    controller_port = 6633  # Replace with the controller's port
    switch_dpid = '0000000000000001'  # Replace with the switch's DPID
    switch_port = 12345  # Replace with the switch's source port
    
    add_iptables_rule(controller_ip, controller_port, switch_dpid, switch_port)
