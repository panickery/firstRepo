from scapy.all import*  
  
def showPacket(packet):  
    a = packet.show()  
    print(a)

def sniffing(filter):  
    sniff(filter = filter, prn = showPacket, count = 1)  
  
if __name__ == '__main__':  
    filter = 'ip'  
    sniffing(filter)  


# # 출처: https://secretpack.tistory.com/112 [secretpack's blog]

# from scapy.all import *
# r = sr1(IP(dst="8.8.8.8")/ICMP()/'HelloWorld')
# r.show()

from scapy.all import*  
