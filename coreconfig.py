from __future__ import print_function

import time

import serialhelper
from vlan import Vlan
from interface import Interface
from serialhelper import Serialhelper
from accessentry import AccessEntry

gateway = '213.184.211.149'
mgmtvlan = '30'
iphelper = '213.184.216.2'

vlans = [
    Vlan.noipnoroute('30', 'crew', '50'),
    Vlan.noipnoroute('40', 'wlan', '51'),
    Vlan('60', 'utilities', '213.184.216.1', '255.255.255.192', interfaceid='52'),
    Vlan('61', 'switch1', '213.184.216.65', '255.255.255.192', interfaceid='53'),
    Vlan('62', 'switch2', '213.184.216.129', '255.255.255.192', interfaceid='54'),
    Vlan('63', 'switch3', '213.184.216.193', '255.255.255.192', interfaceid='55'),
    Vlan('64', 'switch4', '213.184.217.1', '255.255.255.192', interfaceid='56'),
    Vlan('65', 'switch5', '213.184.217.65', '255.255.255.192', interfaceid='57'),
    Vlan('66', 'switch6', '213.184.217.129', '255.255.255.192', interfaceid='58'),
    Vlan('67', 'switch7', '213.184.217.193', '255.255.255.192', interfaceid='59'),
    Vlan('68', 'switch8', '213.184.218.1', '255.255.255.192', interfaceid='60'),
    Vlan('69', 'switch9', '213.184.218.65', '255.255.255.192', interfaceid='61'),
    Vlan('70', 'switch10', '213.184.218.129', '255.255.255.192', interfaceid='62'),
    Vlan('71', 'noname', '213.184.218.193', '255.255.255.192', interfaceid='63'),
    Vlan('72', 'noname', '213.184.219.1', '255.255.255.192', interfaceid='64'),
    Vlan('73', 'noname', '213.184.219.65', '255.255.255.192', interfaceid='65'),
    Vlan('74', 'extra', '213.184.219.129', '255.255.255.192', interfaceid='66'),
    Vlan('75', 'translation', '213.184.219.193', '255.255.255.192', interfaceid='67'),
    Vlan('10', 'tafjord', '213.184.211.150', '255.255.255.252', interfaceid='68'),
]

interfaces = [
    Interface(key='1', tagging=['30'], pvid='61'),
    Interface(key='2', tagging=['30'], pvid='62'),
    Interface(key='3', tagging=['30'], pvid='63'),
    Interface(key='4', tagging=['30'], pvid='64'),
    Interface(key='5', tagging=['30'], pvid='65'),
    Interface(key='6', tagging=['30'], pvid='66'),
    Interface(key='7', tagging=['30'], pvid='67'),
    Interface(key='8', tagging=['30'], pvid='68'),
    Interface(key='9', tagging=['30'], pvid='69'),
    Interface(key='10', tagging=['30'], pvid='70'),
    Interface(key='11', tagging=['30'], pvid='71'),
    Interface(key='12', tagging=['30'], pvid='72'),
    Interface(key='13', tagging=['30'], pvid='73'),
    Interface(key='14', tagging=['30'], pvid='74'),
    Interface(key='15', tagging=['30'], pvid='30'),
    Interface(key='20', tagging=['30', '40', '74', '75', '60']),
    Interface(key='21', tagging=['30', '40', '74', '75', '60']),
    Interface(key='22',
              tagging=['30', '40', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
                       '74', '75']),
    Interface(key='23',
              tagging=['30', '40', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
                       '74', '75']),
    Interface(key='24', pvid='10'),
    Interface(key='25', pvid='61'),
    Interface(key='26', pvid='74'),
    Interface(key='27', pvid='10'),

]

accesslists = [
    AccessEntry(name='internal', mode='permit', protocol='ip', source='172.16.0.0', srcmask='0.0.255.255',
                destination='any')
]

with Serialhelper() as serialhelper:
    name = raw_input('Core switch name:')

    serialhelper.write("admin")
    serialhelper.write("")
    serialhelper.write("enable")
    serialhelper.write("")
    serialhelper.write('clear config')
    serialhelper.write('y')
    time.sleep(8)

    serialhelper.write("admin")
    serialhelper.write("")
    serialhelper.write("enable")
    serialhelper.write("")
    serialhelper.write("set prompt " + name)
    serialhelper.write("vlan database")
    for vlan in vlans:
        serialhelper.write('vlan ' + vlan.key)
        if vlan.routing:
            serialhelper.write('vlan routing ' + vlan.key + ' ' + vlan.interfaceid)
        serialhelper.write('vlan name ' + vlan.key + ' ' + vlan.description)
    serialhelper.write('exit')
    serialhelper.write('ip ssh server enable')
    serialhelper.write('network mgmt_vlan ' + mgmtvlan)
    serialhelper.write('network protocol dhcp')
    serialhelper.write('y')
    serialhelper.write('configure')
    serialhelper.write('ip routing')
    serialhelper.write('ip helper enable')
    serialhelper.write('ip helper-address ' + iphelper)
    serialhelper.write('ip default-gateway ' + gateway)
    for accessentry in accesslists:
        serialhelper.write('ip access-list ' + accessentry.name)
        serialhelper.write('{0} {1} {2} {3} {4}'.format(accessentry.mode, accessentry.protocol, accessentry.source,
                                                        accessentry.srcmask, accessentry.destination))
        serialhelper.write('exit')
    for interface in interfaces:
        serialhelper.write('interface 0/' + interface.key)
        if interface.getallvlans():
            serialhelper.write('vlan participation include ' + ','.join(interface.getallvlans()))
            if interface.pvid:
                serialhelper.write('vlan pvid ' + interface.pvid)
            if interface.tagging:
                serialhelper.write('vlan tagging ' + ','.join(interface.tagging))
        serialhelper.write('no shutdown')
        serialhelper.write('exit')
    for vlan in vlans:
        if not vlan.routing:
            continue
        serialhelper.write('interface 2/' + vlan.interfaceid)
        serialhelper.write('ip address ' + vlan.ip + ' ' + vlan.subnet)
        serialhelper.write('exit')
    serialhelper.write('router ospf')
    serialhelper.write('no enable')
    serialhelper.write('exit')
    serialhelper.write('router rip')
    serialhelper.write('no enable')
    serialhelper.write('exit')
    serialhelper.write('exit')
    serialhelper.write('write memory')
    serialhelper.write('y')

    print("Done echoing to device! Read output:")

    serialhelper.readtoinfinity('Configuration Saved!')
    print("Finished...sw")
