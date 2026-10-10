import ipaddress

ip = input("Enter IP address: ")

try:
    ipaddress.ip_address(ip)
    print("Valid IP address")
except ValueError:
    print("Invalid IP address")