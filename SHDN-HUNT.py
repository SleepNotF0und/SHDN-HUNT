import shodan
import pyfiglet
import sys


# BANNER
#BANNER
print("         _______         ")
print("     .,-'\_____/`-.      ")
print("     /`..'\ _ /`.,'\     ")
print("    /  /`.,' `.,'\  \    ")
print("   /__/__/  O  \__\__\   ")
print("   \  \  \     /  /  /   ")
print("    \  \,'`._,'`./  /    ")
print("     \,'`./___\,'`./     ")
print("     '`-./_____\,-'`     ")
print("                         ")
print("Coded By Hazem Yasser | hackerone.com/0xr3dhunt\n\n")

# SHODAN API KEY
My_API = "--YOUR-API-KEY-HERE--"
API = shodan.Shodan(My_API)

# USAGE
if len(sys.argv) != 3:
    print(" >>>> python SHDN-HUNT.py -d <<-DOMAIN-NAME->>")
    print(" >>>> python SHDN-HUNT.py -l <<-DOMAINS.txt->>")
    sys.exit(0)


def remove_duplicates(nested_list):
    unique_domains = set()
    result = []

    for sublist in nested_list:
        filtered_sublist = []
        for domain in sublist:
            if 'googleusercontent.com' in domain or 'amazonaws.com' in domain:
                continue
            if domain not in unique_domains:
                unique_domains.add(domain)
                filtered_sublist.append(domain)
        result.append(filtered_sublist)
    return result


def hunt_domain(target, output_file):
    print(f"\n[+] Hunting: {target}")

    Query = f'ssl.cert.subject.CN:"*.{target}"'
    try:
        Result1 = API.search_cursor(Query)
    except shodan.APIError as error:
        print("!!! Error with Shodan API !!!")
        return

    Hostnames = []
    IPs = []

    for get_domain in Result1:
        hostnames = get_domain.get('hostnames', [])
        ip = get_domain.get('ip_str', None)
        if hostnames:
            Hostnames.append(hostnames)
        if ip and ':' not in ip:  # Only IPv4
            IPs.append(ip)

    final_hostnames = str(remove_duplicates(Hostnames)).replace('}', '').replace('{', '').replace('[', '').replace(']', '').replace("'", "").replace(',', '\n')
    cleaned_hostnames = "\n".join(line.strip() for line in final_hostnames.splitlines() if line.strip())

    unique_ips = sorted(set(ip.strip() for ip in IPs if ip and ':' not in ip))

    # Print results
    print("\n[+] Hostnames:\n" + cleaned_hostnames)
    print("\n[+] IPs:")
    for ip in unique_ips:
        print(ip)

    # Append to output file
    with open(output_file, 'a') as file:
        file.write(cleaned_hostnames + "\n")
        for ip in unique_ips:
            file.write(ip + "\n")


# Single Domain Mode
if sys.argv[1] == "-d":
    target = sys.argv[2]
    output_file = f"{target}_Shdn-hunt_.txt"
    hunt_domain(target, output_file)

# List Mode
elif sys.argv[1] == "-l":
    filename = sys.argv[2]
    output_file = f"{filename}_Shdn-hunt_.txt"  # All results in one file
    try:
        with open(filename, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]
            for domain in domains:
                hunt_domain(domain, output_file)
        print(f"\n>>>> All results saved in {output_file}")
    except FileNotFoundError:
        print("!!! File not found:", filename)
        sys.exit(1)
