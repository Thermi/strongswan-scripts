#! /bin/bash

if ! ip l show dummy-vip &>/dev/null
then
	ip l add dummy-vip type dummy &>/dev/null
	ip l set dummy-vip up &>/dev/null
fi
