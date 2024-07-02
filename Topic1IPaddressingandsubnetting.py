import ipaddress

def get_network_info(ip_cdir):
    try:
        network = ipaddress.ip_network(ip_cdir, strict=False)
        subnet_address = network.network_address
        broadcast_address = network.broadcast_address

        if network.num_addresses > 2:
            first_host = network.network_address + 1
            last_host = network.broadcast_address - 1

        else:
            first_host = last_host = "No valid hosts"

        return {
            "subnet_address": subnet_address,
            "broadcast_address": broadcast_address,
            "first_host": first_host,
            "last_host": last_host
        }
    except ValueError:
        return None
def main():
    #ask user to enter an IP adress with CDIR notation
    ip_cdir = input("Enter an IP address with CIDR notation (e.g., 192.168.0.0/24):")

    #get network info
    info = get_network_info(ip_cdir)

    if info:
        #display results
        print(f"Subnet Address: {info['subnet_address']}")
        print(f"Broadcast Address: {info['broadcast_address']}")
        print(f"Valid Host Range: {info['first_host']} - {info['last_host']}")

    else:
        print("Invalid IP address or CIDR notation. Please try again.")

if __name__== "__main__":
    main()
