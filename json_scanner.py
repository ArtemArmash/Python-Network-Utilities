import json
from scapy.all import IP, TCP, sr1, send

with open("json_files/targets.json", "r") as f:
    data = json.load(f)

def scan_port(target_ip, port_for_scan):
    if not isinstance(port_for_scan, int):
        print('Port is not number')
        return
    
    ip_pack = IP(dst=target_ip)
    tcp_seg = TCP(dport=port_for_scan, flags="S")

    packet=ip_pack/tcp_seg
    response = sr1(packet, timeout=2, verbose=False)

    if response is not None:
        if response.haslayer(TCP):
            if response[TCP].flags == 0x12:
                print(f'Port [{port_for_scan}] is open')
                close_packet = ip_pack/TCP(
                    sport=response[TCP].dport, 
                    dport=port_for_scan, seq=response[TCP].ack, flags="R")
                send(close_packet, verbose=False)
                return 'open'
            elif response[TCP].flags == 0x14:
                print(f'Port [{port_for_scan}] is closed')
                return 'closed'
            else:
                print('Port error, i dont know he close or open')
                return 'unknown'
        else:
            print('Response not from TCP')
    else:   
        print('Response is NONE')


if __name__ == '__main__':

    for target in data['targets']:
        hostname = target['hostname']
        ports = target['ports']
        results={}
        for port in ports:
            status = scan_port(target_ip=hostname, port_for_scan=port)
            results[str(port)]=status
        target['ports']=results
    
    with open("json_files/results.json", "w") as f:
        json.dump(data, f, indent=4)