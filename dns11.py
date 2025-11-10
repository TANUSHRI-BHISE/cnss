import socket

def dns_lookup(query):
    try:
        # Check if input is an IP address
        socket.inet_aton(query)
        # If no exception, it's a valid IP → perform reverse lookup
        domain_name = socket.gethostbyaddr(query)
        print(f"IP Address: {query}")
        print(f"Domain Name: {domain_name[0]}")
    except socket.error:
        # Not a valid IP → treat it as a hostname
        try:
            ip_address = socket.gethostbyname(query)
            print(f"Domain Name: {query}")
            print(f"IP Address: {ip_address}")
        except socket.gaierror:
            print(" Invalid domain name or IP address. Lookup failed.")

# ---- Main Program ----
query = input("Enter a domain name or IP address: ")
dns_lookup(query)
