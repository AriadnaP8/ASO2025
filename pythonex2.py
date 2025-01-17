from scapy.all import ARP, Ether, srp

def scan_vlan(network): 
     
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC
    packet = ether / arp

    # Trimite pachetul si primeste raspunsuri
    result = srp(packet, timeout=2, verbose=False)[0]

    # Extrage IP-ul și MAC-ul dispozitivelor care au raspuns
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices


if __name__ == "__main__":
    vlan_network = "127.0.0.1/8"

    print(f"Scanning VLAN: {vlan_network}...")
    active_devices = scan_vlan(vlan_network)

    print("\nActive devices:")
    for device in active_devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")
