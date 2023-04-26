class Vlan:
    ip = None
    key = None
    subnet = None
    description = None
    routing = None
    interfaceid = None

    def __init__(self, key, description, ip, subnet, routing=True, tagged=None, untagged=None, interfaceid=None):
        self.untagged = untagged
        self.tagged = tagged
        self.ip = ip
        self.key = key
        self.subnet = subnet
        self.description = description
        self.routing = routing
        self.interfaceid = interfaceid

    @classmethod
    def noip(cls, key, description, interfaceid):
        return cls(key=key, description=description, ip=None, subnet=None, interfaceid=interfaceid)

    @classmethod
    def noipnointerfaceid(cls, key, description):
        return cls(key=key, description=description, ip=None, subnet=None, interfaceid=None)

    @classmethod
    def noipnoroute(cls, key, description, interfaceid):
        return cls(key=key, description=description, ip=None, subnet=None, routing=False, interfaceid=interfaceid)

    @classmethod
    def noipnorouteinterfaces(cls, key, description, tagged, untagged, interfaceid):
        return cls(key=key, description=description, ip=None, subnet=None, routing=False, tagged=tagged,
                   untagged=untagged, interfaceid=interfaceid)

    @classmethod
    def noipnorouteinterfacesnointerfaceid(cls, key, description, tagged, untagged):
        return cls(key=key, description=description, ip=None, subnet=None, routing=False, tagged=tagged,
                   untagged=untagged, interfaceid=None)
