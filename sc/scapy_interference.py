import scapy.all as sc

#sc.send(sc.IP(dst="192.168.0.17")/sc.TCP(flags="S", sport=sc.RandShort(),dport=8080)/sc.Raw("Halslo world!"))