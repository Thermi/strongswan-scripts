connectionCloser.py
====

Terminates all tunnels without timeout when called. The use case is to call the script
when strongSwan stops but the network is down, like when you shut down your system.
Without calling the script, shutdown takes forever, because strongSwan waits for the tunnels to be closed.
If the network is down, that effectively means until the tunnels time out and that can take a while.
Alternatively, until the init daemon decides to kill strongswan.

The script requires the vici gem for python and for strongSwan to be configured
to load the vici plugin and that plugin to be loaded. strongSwan must be allowed to execute the python script.

Configuration could look like this

```
charon {
	stop-scripts {
			kill-tunnels = kill-tunnels = /etc/swanctl/connectionCloser.py
	}

}
```

dummy-vip-init.sh
===


This script makes sure a dummy interface with name dummy-vip exists.
The use case is to make sure the dummy interface exists before strongSwan tries to bind a VIP (virtual IP) to it.
There are security reasons for configuring strongSwan to bind virtual IPs to a dummy interface.
It uses bash and iproute2.

Configuration is like with dummy-vip-init, but uses charon.start-scripts instead of charon.stop-scripts.

init-dhcp-route-bypass.sh
====

This script inserts routing rules for all packets marked with fwmark 0x11 to lookup the main table.
The use case is to make sure a DHCP daemon/client that uses an AF_INET or AF_INET6 socket without
specifying a source IP does not accidently try to send packets with the virtual IP as source.
This script works together with iptables/ip6tables/nftables rules that mark DHCP packets with fwmark 0x11 (-j MARK --set-mark 0x11)
It uses bash and iproute2.

Configuration is like with dummy-vip-init, but uses charon.start-scripts instead of charon.stop-scripts.
