from __future__ import print_function
from vlan import Vlan
from serialhelper import Serialhelper
import time

mgmtvlan = '30'
fakevlan = '30'
accessports = 46
uplinks = ['47', '48', '49', '50']
vlans = [
    Vlan.noip(key=mgmtvlan, description='crew'),
    Vlan.noip(key=fakevlan, description='access')
]

with Serialhelper() as serialhelper:
    name = raw_input('Edge switch name:')

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
        serialhelper.write('vlan name ' + vlan.key + ' ' + vlan.description)
    serialhelper.write('exit')
    serialhelper.write('ip ssh server enable')
    serialhelper.write('network mgmt_vlan ' + mgmtvlan)
    serialhelper.write('network protocol dhcp')
    serialhelper.write('y')
    serialhelper.write('configure')
    for interface in range(1, accessports):
        serialhelper.write('interface 0/' + str(interface))
        serialhelper.write('vlan participation include ' + fakevlan)
        serialhelper.write('vlan pvid ' + fakevlan)
        serialhelper.write('no shutdown')
        serialhelper.write('exit')
    for interface in uplinks:
        serialhelper.write('interface 0/' + str(interface))
        serialhelper.write('vlan participation include ' + fakevlan + ',' + mgmtvlan)
        serialhelper.write('vlan pvid ' + fakevlan)
        serialhelper.write('vlan tagging ' + mgmtvlan)
        serialhelper.write('no shutdown')
        serialhelper.write('exit')
    serialhelper.write('exit')
    serialhelper.write('write memory')
    serialhelper.write('y')

    print("Done echoing to device! Read output:")

    serialhelper.readtoinfinity('Configuration Saved!')
    print("Finished...sw")
