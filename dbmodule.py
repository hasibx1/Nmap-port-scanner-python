
import sqlite3
import pandas as pd
import numpy
from sqlalchemy import create_engine

def db(*args):

    with sqlite3.connect('Test.db') as db:
        cursor = db.cursor()
    ns, ip_addr, ports = args


    for proto in ns[ip_addr].all_protocols():

        lport = ns[ip_addr][proto].keys()

        sorted(lport)
        port2 = ','
        port1= port2.join(str(port) for port in lport)



        cursor.execute('''
    CREATE TABLE IF NOT EXISTS Scaninfo(
    scanID INTEGER PRIMARY KEY,
    ip_address VARCHAR(40) NOT NULL,
    scanned_ports VARCHAR(100) NOT NULL,
    Opened_ports INTEGER(100),
    Hostname VARCHAR(100) NOT NULL,
    ipaddress_state VARCHAR(100) NOT NULL);
    ''')

    cursor.execute("insert into Scaninfo (ip_address, scanned_ports, Opened_ports ,Hostname, ipaddress_state) values (?, ?, ?, ?, ?)",
                   (ip_addr, ports, port1, ns[ip_addr].hostname(), ns[ip_addr].state() ))

    db.commit()

    def Report_csv():
        db_name = 'Test.db'

        engine = create_engine('sqlite:///' + db_name)
        df = pd.read_sql_table('Scaninfo', engine)
        df.to_csv('test.csv')
    Report_csv()

