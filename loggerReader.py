# -*- coding:utf-8 -*-

import paramiko
from config import remotedir,remotefile,password,port,hostname,username,command

def get_1000_lines():

    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()

    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname,port,username,password)
    #days/twicker.log'#posts/posts.log'  #/home/ftp/lj/develer/uwsgi/uwsgi.log，counts
    stdin,stdout,stderr = s.exec_command(command)
    #print(2,stdout.read())
    logs = stdout.readlines()
    s.close()
    # for i in range(len(logs)):
    #     logresult = []
        # print(logs[i].rstrip())
    return logs





def getfile():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password, compress=True)
    sftp_client = client.open_sftp()
    remote_file = sftp_client.open(remotefile)#文件路径
    remote_file.close()
    return remotefile
