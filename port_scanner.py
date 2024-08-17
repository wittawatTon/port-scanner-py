import socket
import re
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    def is_valid_ip(ip):
        pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
        return pattern.match(ip) is not None

    def is_valid_url(url):
        pattern = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return pattern.match(url) is not None

    def get_ip_from_url(url):
        try:
            return socket.gethostbyname(url)
        except socket.error:
            return None

    def check_port(ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                s.connect((ip, port))
                return True
            except socket.error:
                return False
            
    def get_hostname_by_ip(ip):
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            return hostname
        except socket.herror:
            return None
        
    # Validate target
    if is_valid_ip(target):
        ip = target
    elif is_valid_url(target):
        ip = get_ip_from_url(target)
        if ip is None:
            return "Error: Invalid hostname"
    else:
        return "Error: Invalid IP address"

    if ip is None:
        return "Error: Invalid IP address"

    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        if check_port(ip, port):
            open_ports.append(port)
            #print("Open port:" + str(port))

    if verbose:
        service_lines = []
        for port in open_ports:
            service = ports_and_services.get(port, 'unknown')
            service_lines.append(f"{port:<8} {service}")
        
        
        host_name = get_hostname_by_ip(ip)
        if host_name is None:
            result = f"Open ports for {ip}\nPORT     SERVICE\n" + "\n".join(service_lines)
        else:
            result = f"Open ports for {host_name} ({ip})\nPORT     SERVICE\n" + "\n".join(service_lines)
        
            
        return result

    return open_ports


