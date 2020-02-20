import time 
import datetime, threading
import subprocess
import socket
import sys
import os

output_file = "output.txt"
#This function will be executed after every x minutes
def get_output_path():
    try:
        path = sys.argv[2]
    except:
        path = str(input("Output file: "))
    return path

def get_input_path():
    try:
        path = sys.argv[1]
    except:
        path = str(input("Input file: "))
    return path

def show_file():
    with open(get_input_path(), "r") as source:
        print(source.readline())

def rewrite(output_file, message):
    with open(output_file, 'w') as result:
        result.write(message + '\n')

def traceroute(hostname):
    hostname = ' '+ hostname
    route = subprocess.Popen(['traceroute' + ' -w' + ' 7' + ' --resolve-hostname '+ hostname], shell=True, stderr=subprocess.PIPE)
    while (True):
        out = route.stderr.read(1)
        if out == '' and route.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()
            
def get_dns(hostname):
    try:
        dns = subprocess.Popen(['nslookup ' + hostname], shell=True, stderr=subprocess.PIPE)
    except: 
        dns = 'Non DNS'
    return dns

def main():
    input_file = get_input_path()
    output_file = get_output_path()

    with open(input_file, "r") as source:
       while True:
            hostname = source.readline()
            if hostname == '':
                break;
            #print(get_dns(hostname))
            print('\n')
            print(hostname + ':')
            traceroute(hostname)


main()
