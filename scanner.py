import sys

def pass_scan(*args):

    ns, ip_addr, ports = args
    ns.scan(ip_addr, ports, '-vv -sS --open')
    print(ns.csv())


    '''
    def save_csv_data(ns_csv, path='.'):
        with open(path + '/output.csv', 'w') as output:
            output.write(ns_csv)
        
        if (len(sys.argv) > 1 and sys.argv[1]):
            save_csv_data(ns.csv(), path=sys.argv[1])
        else:
            save_csv_data(ns.csv())
    save_csv_data('')
    '''


