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
        # Regular Expression for testing IP from 0 to 255
        ip_tested =  re.sub("\d{1,3}$",str(i),ip)
        t = threading.Thread(target=is_port_open,args=(ip_tested,port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    
def save_active_hosts_to_file(active_hosts):
    filename = "Active_miner_IP.txt"

    if active_hosts:
        # open and clean old content, if not exists a file will be created
        fw = open(filename, 'w')
        for element in active_hosts:    
            fw.write(element + "\n")
        fw.close()
    else:
        print("There is no active miner in this LAN：" + str(re.sub("\d{1,3}$","X",ip)))

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    # port must be set
    port = 8848

    # a global list for the multi-thread scannings of the active hosts
    active_hosts = []

    # get localhost IP in the LAN
    ip = get_host_ip()

    # multi-thread scan the open port in the LAN
    open_multithreaded_detect_ip(ip,port)
    
    # save detected active_hosts to file
    save_active_hosts_to_file(active_hosts)

    print(active_hosts)
    
    

#long running

    endtime = datetime.datetime.now()

    print (endtime - starttime)
