# -*- coding:utf-8 -*-

import paramiko

def get_1000_lines():

    remotedir = '/home/ftp/lj/develer/logs'
    remotefile = '/home/ftp/lj/develer/logs/twicker.log'
    hostname = '47.100.21.123'
    port = 22
    username = 'root'
    password = 'asd467461dsa'


    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()

    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname,port,username,password)
    command =  'tail -100 /home/ftp/lj/develer/logs/posts/posts.log'#days/twicker.log'#posts/posts.log'  #/home/ftp/lj/develer/uwsgi/uwsgi.log，counts
    stdin,stdout,stderr = s.exec_command(command)
    #print(2,stdout.read())
    logs = stdout.readlines()
    s.close()
    # for i in range(len(logs)):
    #     logresult = []
        # print(logs[i].rstrip())
    return logs

