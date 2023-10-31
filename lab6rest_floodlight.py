#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():
    net = Mininet( controller=RemoteController )
    net.addController( 'c0' )
    h1 = net.addHost( 'h1' )
    h2 = net.addHost( 'h2' )
    s1 = net.addSwitch( 's1' )
    net.addLink( h1, s1 )
    net.addLink( h2, s1 )
    
    net.start()
    s1.cmd('ovs-vsctl set-controller s1 ssl:10.224.78.5:6633')
    
    net.pingAll()
    CLI( net )
    net.stop()
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
