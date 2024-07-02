from scapy.all import *
import time

def traceroute(destination, max_hops=30, timeout=2):
    print(f"Traceroute to {destination} with max {max_hops} hops\n")
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=destination, ttl=ttl) / ICMP()
        start_time = time.time()
        reply = sr1(pkt, verbose=0, timeout=timeout)
        rtt = (time.time() - start_time) * 1000  # RTT in milliseconds

        if reply is None:
            print(f"{ttl:2}  *  *  *  (Request timed out)")
        else:
            print(f"{ttl:2}  {reply.src}  {rtt:.2f} ms")
            if reply.type == 0:  # ICMP Echo Reply (destination reached)
                break

if __name__ == "__main__":
    destination_ip = input("Enter the destination IP address: ")
    traceroute(destination_ip)
