from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.0/24"
ehter_pack=Ether(dst="ff:ff:ff:ff:ff:ff")
arp_req = ARP(pdst=target_ip)

packet=ehter_pack/arp_req

answer, _ = srp(packet, timeout=2, verbose=False)

for send, response in answer:
    print(f'IP: [{response.psrc}], MAC: [{response.hwsrc}]')