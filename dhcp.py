from __future__ import print_function
import os
from subnet import Subnet

filename = 'output/dhpcd.conf'
os.makedirs(os.path.dirname(filename), exist_ok=True)
f = open(filename, 'w')


def output(data):
    print(data, file=f)


subnets = [
    Subnet(subnet='213.184.216.0', netmask='255.255.255.192', gateway='213.184.216.1', startip=None, stopip=None),
    Subnet(subnet='213.184.216.64', netmask='255.255.255.192', gateway='213.184.216.65', startip='213.184.216.66',
           stopip='213.184.216.126'),
    Subnet(subnet='213.184.216.128', netmask='255.255.255.192', gateway='213.184.216.129', startip='213.184.216.130',
           stopip='213.184.216.190'),
    Subnet(subnet='213.184.216.192', netmask='255.255.255.192', gateway='213.184.216.193', startip='213.184.216.194',
           stopip='213.184.216.254'),
    Subnet(subnet='213.184.217.0', netmask='255.255.255.192', gateway='213.184.217.1', startip='213.184.217.2',
           stopip='213.184.217.62'),
    Subnet(subnet='213.184.217.64', netmask='255.255.255.192', gateway='213.184.217.65', startip='213.184.217.66',
           stopip='213.184.217.126'),
    Subnet(subnet='213.184.217.128', netmask='255.255.255.192', gateway='213.184.217.129', startip='213.184.217.130',
           stopip='213.184.217.190'),
    Subnet(subnet='213.184.217.192', netmask='255.255.255.192', gateway='213.184.217.193', startip='213.184.217.194',
           stopip='213.184.217.254'),
    Subnet(subnet='213.184.218.0', netmask='255.255.255.192', gateway='213.184.218.1', startip='213.184.218.2',
           stopip='213.184.218.62'),
    Subnet(subnet='213.184.218.64', netmask='255.255.255.192', gateway='213.184.218.65', startip='213.184.218.66',
           stopip='213.184.218.126'),
    Subnet(subnet='213.184.218.128', netmask='255.255.255.192', gateway='213.184.218.129', startip='213.184.218.130',
           stopip='213.184.218.190'),
    Subnet(subnet='213.184.218.192', netmask='255.255.255.192', gateway='213.184.218.193', startip='213.184.218.194',
           stopip='213.184.218.254'),
    Subnet(subnet='213.184.219.0', netmask='255.255.255.192', gateway='213.184.219.1', startip='213.184.219.2',
           stopip='213.184.219.62'),
    Subnet(subnet='213.184.219.64', netmask='255.255.255.192', gateway='213.184.219.65', startip='213.184.219.66',
           stopip='213.184.219.126'),
    Subnet(subnet='213.184.219.128', netmask='255.255.255.192', gateway='213.184.219.129', startip='213.184.219.130',
           stopip='213.184.219.190'),
    Subnet(subnet='213.184.219.192', netmask='255.255.255.192', gateway='213.184.219.193', startip=None, stopip=None),
]

output("""log-facility local6;
    authoritative;
    group public {
    default-lease-time 600;
    max-lease-time 1200;
    option domain-name "lan.zargate.org";
    option domain-name-servers 213.184.216.2, 8.8.8.8, 8.8.4.8;""")
for subnet in subnets:
    output("""
    subnet {0} netmask {1} {{
        option routers {2};
        option subnet-mask {1};""".format(subnet.subnet, subnet.netmask, subnet.gateway))
    if subnet.startip and subnet.stopip:
        output("        range {0} {1};".format(subnet.startip, subnet.stopip))
    output("    }")
output("}")

output("""group crew {
    default-lease-time 1200;
    max-lease-time 3600;
    option domain-name "crew.lan.zargate.org";
    option domain-name-servers 172.16.0.1, 8.8.8.8, 8.8.4.8;
    subnet 172.16.0.0 netmask 255.255.252.0 {
        option routers 172.16.0.1;
        option subnet-mask 255.255.252.0;
        range 172.16.0.4 172.16.3.254;
    }
}""")

output("""group wlan {
    default-lease-time 1200;
    max-lease-time 3600;
    option domain-name "wlan.lan.zargate.org";
    option domain-name-servers 172.16.4.1, 8.8.8.8, 8.8.4.8;
    subnet 172.16.4.0 netmask 255.255.252.0 {
        option routers 172.16.4.1;
        option subnet-mask 255.255.252.0;
        range 172.16.4.4 172.16.7.254;
    }
}""")
