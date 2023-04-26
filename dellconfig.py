from __future__ import print_function
from vlan import Vlan
from interface import Interface
from serialhelper import Serialhelper
import time

mgmtvlan = '30'

vlans = [
    Vlan.noipnointerfaceid('30', 'crew'),
    Vlan.noipnointerfaceid('40', 'wlan'),
    Vlan.noipnointerfaceid('60', 'utilities'),
    Vlan.noipnointerfaceid('61', 'switch1'),
    Vlan.noipnointerfaceid('62', 'switch2'),
    Vlan.noipnointerfaceid('63', 'switch3'),
    Vlan.noipnointerfaceid('64', 'switch4'),
    Vlan.noipnointerfaceid('65', 'switch5'),
    Vlan.noipnointerfaceid('66', 'switch6'),
    Vlan.noipnointerfaceid('67', 'switch7'),
    Vlan.noipnointerfaceid('68', 'switch8'),
    Vlan.noipnointerfaceid('69', 'switch9'),
    Vlan.noipnointerfaceid('70', 'switch10'),
    Vlan.noipnointerfaceid('71', 'noname'),
    Vlan.noipnointerfaceid('72', 'noname'),
    Vlan.noipnointerfaceid('73', 'noname'),
    Vlan.noipnointerfaceid('74', 'noname'),
    Vlan.noipnointerfaceid('75', 'translation'),
]

interfaces = [
    Interface(key='g1', tagging=['30'], pvid='61'),
    Interface(key='g2', tagging=['30'], pvid='61'),

    Interface(key='g3', tagging=['30'], pvid='62'),
    Interface(key='g4', tagging=['30'], pvid='62'),

    Interface(key='g5', tagging=['30'], pvid='63'),
    Interface(key='g6', tagging=['30'], pvid='63'),

    Interface(key='g7', tagging=['30'], pvid='64'),
    Interface(key='g8', tagging=['30'], pvid='64'),

    Interface(key='g9', tagging=['30'], pvid='65'),
    Interface(key='g10', tagging=['30'], pvid='65'),

    Interface(key='g11', tagging=['30'], pvid='66'),
    Interface(key='g12', tagging=['30'], pvid='66'),

    Interface(key='g13', tagging=['30'], pvid='67'),
    Interface(key='g14', tagging=['30'], pvid='67'),

    Interface(key='g15', tagging=['30'], pvid='68'),
    Interface(key='g16', tagging=['30'], pvid='68'),

    Interface(key='g17', tagging=['30'], pvid='69'),
    Interface(key='g18', tagging=['30'], pvid='69'),

    Interface(key='g19', tagging=['30'], pvid='70'),
    Interface(key='g20', tagging=['30'], pvid='70'),

    Interface(key='g21', tagging=['30'], pvid='71'),
    Interface(key='g22', tagging=['30'], pvid='71'),

    Interface(key='g23', tagging=['30'], pvid='72'),
    Interface(key='g24', tagging=['30'], pvid='72'),

    Interface(key='g25', tagging=['30'], pvid='73'),
    Interface(key='g26', tagging=['30'], pvid='73'),

    Interface(key='g27', tagging=['30'], pvid='74'),
    Interface(key='g28', tagging=['30'], pvid='74'),

    Interface(key='g29', tagging=['30'], pvid='75'),
    Interface(key='g30', tagging=['30'], pvid='75'),

    Interface(key='g31', tagging=['30', '40'], pvid='30'),  # wlan 1
    Interface(key='g32', tagging=['30', '40'], pvid='30'),  # wlan 2
    Interface(key='g33', tagging=['30', '40'], pvid='30'),  # wlan 3
    Interface(key='g34', tagging=['30', '40'], pvid='30'),  # wlan 4
    Interface(key='g35', tagging=['30', '40'], pvid='30'),  # wlan 5
    Interface(key='g36', tagging=['30', '40'], pvid='30'),  # wlan 6
    Interface(key='g37', tagging=['30', '40'], pvid='30'),  # wlan 7
    Interface(key='g38', tagging=['30', '40'], pvid='30'),  # wlan 8

    Interface(key='g39', tagging=[], pvid='30'),  # common untagged management
    Interface(key='g40', tagging=[], pvid='30'),  # common untagged management
    Interface(key='g41', tagging=[], pvid='30'),  # common untagged management
    Interface(key='g42', tagging=[], pvid='30'),  # common untagged management

    Interface(key='g43', tagging=['30', '40', '74'], pvid='30'),  # common
    Interface(key='g44', tagging=['30', '40', '74'], pvid='30'),  # common
    Interface(key='g45', tagging=['30', '40', '74'], pvid='30'),  # common
    Interface(key='g46', tagging=['30', '40', '74'], pvid='30'),  # common
    Interface(key='g47', tagging=['30', '40', '74'], pvid='30'),  # common
    Interface(key='g48', tagging=['30', '40', '74'], pvid='30'),  # common



    Interface(key='xg1',
              tagging=['30', '40', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
                       '74', '75']),
    Interface(key='xg2',
              tagging=['30', '40', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
                       '74', '75']),
    Interface(key='xg3',
              tagging=['30', '40', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
                       '74', '75']),
    Interface(key='xg4',
              tagging=['30', '40', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
                       '74', '75']),
]

with Serialhelper() as serialhelper:
    def delaywrite(data):
        serialhelper.write(data)
        time.sleep(0.2)


    def fakesleep(seconds):
        for i in range(0, seconds):
            time.sleep(1)
            serialhelper.write('')


    name = raw_input('DELL subcore switch name:')

    delaywrite("")
    delaywrite("enable")
    delaywrite("")
    delaywrite('clear config')
    delaywrite('y')
    time.sleep(45)

    delaywrite("")
    delaywrite("")
    delaywrite("")
    delaywrite("")
    delaywrite("")
    delaywrite("enable")
    delaywrite("")
    delaywrite('configure')
    delaywrite("hostname " + name)
    delaywrite("vlan database")
    for vlan in vlans:
        delaywrite('vlan ' + vlan.key)
    delaywrite('exit')
    for vlan in vlans:
        delaywrite('interface vlan ' + vlan.key)
        delaywrite('name ' + vlan.description)
        delaywrite('exit')

    delaywrite('ip address vlan ' + mgmtvlan)
    delaywrite('ip address dhcp')
    delaywrite('crypto key generate rsa')
    delaywrite('y')  # in case of "do you want to overwrite?"
    print('Sleeping thread for 10 seconds while generating RSA')
    fakesleep(10)
    delaywrite('crypto key generate dsa')
    delaywrite('y')  # in case of "do you want to overwrite?"
    print('Sleeping thread for 30 seconds while generating RSA')
    fakesleep(30)

    delaywrite('ip ssh server')

    for interface in interfaces:
        delaywrite('interface ethernet 1/' + interface.key)
        delaywrite('switchport mode general')
        if interface.getallvlans():
            if interface.pvid:
                delaywrite('switchport general allowed vlan add ' + interface.pvid + ' untagged')
                delaywrite('switchport general pvid ' + interface.pvid)
            if interface.tagging:
                delaywrite('switchport general allowed vlan add ' + ','.join(interface.tagging) + ' tagged')
        delaywrite('no shutdown')
        delaywrite('power inline auto')
        delaywrite('exit')

    delaywrite('exit')
    delaywrite('copy running-config startup-config')
    delaywrite('y')

    print("Done echoing to device! Read output:")

    serialhelper.readtoinfinity('Configuration Saved!')
    print("Finished...sw")
