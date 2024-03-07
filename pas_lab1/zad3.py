import ipaddress
import sys

inp = input("Enter IP Address: ")


try:
    ip = ipaddress.ip_address(inp)
    print("valid")
except ValueError:
    print("invalid")