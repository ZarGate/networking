class Interface:
    key = None
    tagging = []
    pvid = None

    def __init__(self, key, tagging=[], pvid=None):
        self.key = key
        self.tagging = tagging
        self.pvid = pvid

    def getallvlans(self):
        res = set(self.tagging)
        if self.pvid:
            res.add(self.pvid)
        res = list(res)
        return res
