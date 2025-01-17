import subprocess

def scan_services(ip):
    """
    Scanează o mașină specificată pentru porturi deschise și servicii.
    
    Args:
        ip (str): Adresa IP a mașinii de scanat.
    
    Returns:
        list: O listă cu porturile deschise, numele serviciilor și versiunile acestora.
    """
    try:
        # Rulează nmap pentru a identifica porturile și serviciile
        result = subprocess.check_output(['nmap', '-sV', ip], universal_newlines=True)
        print(f"Scanning services on {ip}...\n")
        
        services = []
        for line in result.split("\n"):
            # Caută linii care conțin informații despre servicii
            if "/tcp" in line or "/udp" in line:
                parts = line.split()
                port = parts[0]
                name = parts[2]
                version = " ".join(parts[3:]) if len(parts) > 3 else "Unknown"
                services.append((port, name, version))
        
        return services
    except FileNotFoundError:
        print("nmap nu este instalat. Instalează-l cu `sudo apt install nmap`.")
        return []
    except Exception as e:
        print(f"Eroare la scanarea serviciilor pe {ip}: {e}")
        return []


if __name__ == "__main__":
    # Alege IP-ul mașinii de scanat
    target_ip = "10.11.14.15"  # Înlocuiește cu IP-ul dorit
    
    # Scanează mașina pentru servicii
    services = scan_services(target_ip)

    # Afișează rezultatele
    if services:
        print(f"Services found on {target_ip}:")
        for port, name, version in services:
            print(f"Port: {port}, Service: {name}, Version: {version}")
    else:
        print(f"No services found on {target_ip}.")
