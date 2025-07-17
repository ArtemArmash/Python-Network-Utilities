from scapy.all import IP,TCP,sr1, send

target_ip = "scanme.nmap.org"
port_for_scan = 80
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
        elif response[TCP].flags == 0x14:
            print(f'Port [{port_for_scan}] is closed')
        else:
            print('Port error, i dont know he close or open')
    else:
        print('Response not from TCP')
else:
    print('Response is NONE')