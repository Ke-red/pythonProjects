import socket
import IPy
a = 0

def isIP(host):
    try:
        IPy.IP(host)
        ip = 1
        return ip
    except ValueError:
        ip = 0
        return ip
    
def main():
    
    print("NSLookup in Python")
    
    while a == 0:
        host = input("\nEnter an IP address or domain: ")
        
        ip = isIP(host)
        
        if ip == 1:
            print (f"Domain Name: {socket.gethostbyaddr(host)}")
        else:
            print (f"IP Address: {socket.gethostbyname(host)}")
    
main()