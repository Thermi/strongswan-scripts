#! /bin/sh
# Init dhcp bypass routing table and rules

if [ ! `ip rule show | fgrep "0x11" | wc -l` ]
then
	exit
fi

ip -6 rule add fwmark 0x11 lookup main prio 10
ip rule add fwmark 0x11 lookup main prio 10
