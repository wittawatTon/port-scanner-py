import port_scanner


#ret = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
#ret = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
#ret = port_scanner.get_open_ports("scanme.nmap", [22, 42], False)
ret = port_scanner.get_open_ports("266.255.9.10", [22, 42], False)
print("return:", "\n" ,ret, "\n")

