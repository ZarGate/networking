class Subnet:
    def __init__(self, subnet, netmask, gateway, startip=None, stopip=None):
        self.subnet = subnet
        self.gateway = gateway
        self.netmask = netmask
        self.startip = startip
        self.stopip = stopip