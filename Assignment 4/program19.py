import re

def validate_ip(ip):
    # IPv4 pattern
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    # IPv6 pattern
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    # Check IPv4
    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')

        # Check each number is between 0 and 255
        if all(0 <= int(part) <= 255 for part in parts):
            return True

    # Check IPv6
    elif re.match(ipv6_pattern, ip):
        return True

    return False


# Accept IP address from user
ip = input("Enter IP address: ")

# Validate IP address
if validate_ip(ip):
    print("Valid IP Address")
else:
    print("Invalid IP Address")