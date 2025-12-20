#!/bin/bash
NA="N/A"

echo "Network Health Summary"

hostname_val=$(hostname 2>/dev/null)
echo "Hostname        : ${hostname_val:-$NA}"

iface=$(ip route 2>/dev/null | grep default | awk '{print $5}')
echo "Interface       : ${iface:-$NA}"

ip_addr=$(ip addr show "$iface" 2>/dev/null | grep inet | awk '{print $2}' | cut -d/ -f1)
echo "IP_Address      : ${ip_addr:-$NA}"

gateway=$(ip route 2>/dev/null | grep default | awk '{print $3}')
echo "Default_Gateway : ${gateway:-$NA}"

dns=$(cat /etc/resolv.conf 2>/dev/null | grep nameserver | awk '{print $2}' | tr '\n' ',' | sed 's/,$//')
echo "DNS Servers     : ${dns:-$NA}"

tcp=$(ss -tan 2>/dev/null | grep ESTAB | wc -l)
echo "TCP Established : ${tcp:-$NA}"

