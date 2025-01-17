import subprocess

def ping_sweep(network):
    """
    Realizează un ping sweep pentru o rețea specificată.
    
    Args:
        network (str): Rețeaua de scanat (ex. '10.11.14.0/24').
    
    Returns:
        list: O listă de IP-uri active în rețea.
    """
    # Extrage prefixul rețelei și calculează intervalul IP-urilor
    prefix, _ = network.split('/')
    base_ip = '.'.join(prefix.split('.')[:3])
    active_ips = []

    print(f"Scanning VLAN: {network}...")

    # Ping fiecare IP din interval
    for i in range(1, 255):  # IP-uri din 10.11.14.1 până la 10.11.14.254
        ip = f"{base_ip}.{i}"
        try:
            # Rulează comanda ping pentru fiecare IP
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.DEVNULL)
            if result.returncode == 0:  # Dacă dispozitivul răspunde la ping
                active_ips.append(ip)
                print(f"Active IP found: {ip}")
        except Exception as e:
            print(f"Error scanning IP {ip}: {e}")

    return active_ips


if __name__ == "__main__":
    # Definește rețeaua VLAN (ex. '10.11.14.0/24')
    vlan_network = "10.11.14.0/24"

    # Obține IP-urile active
    active_ips = ping_sweep(vlan_network)

    # Afișează rezultatele
    print("\nActive devices in VLAN:")
    for ip in active_ips:
        print(ip)
