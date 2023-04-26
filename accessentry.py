class AccessEntry:
    def __init__(self, name, mode, protocol, source, srcmask, destination):
        self.destination = destination
        self.srcmask = srcmask
        self.source = source
        self.protocol = protocol
        self.mode = mode
        self.name = name