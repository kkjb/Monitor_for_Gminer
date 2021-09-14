import socket
import re
import threading

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('114.114.114.114', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
 
def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, int(port)))
    if result == 0:
        s.close()
        active_hosts.append(ip)       
        return True
    else:
        s.close()
        return False

def detect_active_host():
    ip = get_host_ip()
    active_hosts = []
    for i in range(0,256):
        ip_tested =  re.sub("\d{1,3}$",str(i),ip)
        ip_open_flag = is_port_open(ip_tested,8848)
        if ip_open_flag == True:
            active_hosts.append(ip_tested)
    
    return active_hosts


 

if __name__ == '__main__':
    ip = get_host_ip()
    port = 8848

    threads = []
    active_hosts = []

    for i in range(0,256):
        ip_tested =  re.sub("\d{1,3}$",str(i),ip)
        t = threading.Thread(target=is_port_open,args=(ip_tested,port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    
    print(active_hosts)