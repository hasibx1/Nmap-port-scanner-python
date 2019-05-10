from scanner import pass_scan
from SecondaryScript import *
from dbmodule import db




class Ip_input():


    def pass_ip(self):



        global ns
        global ip_addr
        global ports


        ip_addr = input(" Enter ip address to scan: ")
        type(ip_addr)
        ports = input(" Enter port or range of ports: (22) or (1-100) ")
        ports.split(",")
        type(ports)

    pass_ip('')
    pass_scan(ns, ip_addr, ports)
    db(ns, ip_addr, ports)



pass
