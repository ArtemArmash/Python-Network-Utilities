from scapy.all import IP,TCP,sr1,send
import threading

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
            elif response[TCP].flags == 0x14:
                print(f'Port [{port_for_scan}] is closed')
            else:
                print('Port error, i dont know he close or open')
        else:
            print('Response not from TCP')
    else:   
        print('Response is NONE')

if __name__ == '__main__'  :      
    ip="scanme.nmap.org"
    ports=[80,443,2020,8888,"Hi",5555,4444,2222,1111,0,63222, "helllo"]
    threads=[]
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
        
