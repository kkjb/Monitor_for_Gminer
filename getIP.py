import socket
import re
import threading
import datetime


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


def open_multithreaded_detect_ip(ip,port):
    threads = []
    for i in range(0,256):
        ip_tested =  re.sub("\d{1,3}$",str(i),ip)
        t = threading.Thread(target=is_port_open,args=(ip_tested,port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    


if __name__ == '__main__':
    starttime = datetime.datetime.now()

    ip = get_host_ip()
    port = 8848
    active_hosts = []
    open_multithreaded_detect_ip(ip,port)
    print(active_hosts)
    
    

#long running

    endtime = datetime.datetime.now()

    print (endtime - starttime)
