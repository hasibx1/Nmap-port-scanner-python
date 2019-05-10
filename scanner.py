import sys

def pass_scan(*args):

    ns, ip_addr, ports = args
    ns.scan(ip_addr, ports, '-vv -sS --open')
    print(ns.csv())




