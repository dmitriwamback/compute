import socket
import time
import scapy.all as sc

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.17', 8080))

while True:

    p = sc.IP(dst="192.168.0.17")/sc.TCP(flags="S", sport=sc.RandShort(), dport=4444)/sc.Raw("Hallo world!")
    client.send(bytes(p))
    time.sleep(1)