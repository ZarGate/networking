from __future__ import print_function
import os
from vlan import Vlan

mgmtvlan = '30'
ports = int(raw_input('Number of common ports'))

uplinks = raw_input('Comma separated uplink')

vlans = [
    Vlan.noipnorouteinterfacesnointerfaceid('30', 'crew', untagged='1-' + str(ports / 2), tagged=uplinks),
    Vlan.noipnorouteinterfacesnointerfaceid('74', 'extra', untagged=str((ports / 2) + 1) + '-' + str(ports),
                                            tagged=uplinks),
]

filename = 'output/hp.conf'
os.makedirs(os.path.dirname(filename), exist_ok=True)
file = open(filename, 'w')


def helperwrite(data):
    print(data, file=file)


name = raw_input('HP common switch name:')
helperwrite('configure')
helperwrite('hostname "' + name + '"')
helperwrite('banner motd "zargate.org"')
helperwrite('time timezone 60')
helperwrite('sntp server 81.226.218.187')
helperwrite('timesync sntp')
helperwrite('sntp unicast')
helperwrite('crypto key generate ssh')
helperwrite('aaa authenticate ssh enable local')
helperwrite('ip ssh')
helperwrite('ip ssh version 2')
helperwrite('ip ssh filetransfer')
helperwrite('no tftp client')
helperwrite('no tftp server')
helperwrite('no telnet-server')
helperwrite('no web-management')
helperwrite('no stack')
helperwrite('console inactivity-timer 5')
helperwrite('no snmpv3 enable')
helperwrite('snmp-server community public restricted')
helperwrite('snmp-server contact "tech@zargate.org"')
for vlan in vlans:
    helperwrite('vlan ' + vlan.key)
    helperwrite('name "' + vlan.description + '"')
    if vlan.untagged:
        helperwrite('untagged ' + vlan.untagged)
    if vlan.tagged:
        helperwrite('tagged ' + vlan.tagged)
    if vlan.key == mgmtvlan:
        helperwrite('ip address dhcp-bootp')
    helperwrite('exit')
helperwrite('loop-protect 1-' + str(ports))
helperwrite('password manager user-name zargate')
helperwrite('zgswitch')
helperwrite('zgswitch')
helperwrite('write memory')
helperwrite('boot system')
helperwrite('y')
print("Finished...sw")
print("Now connect to the switch, and paste the contents of hp.conf to the terminal!")
