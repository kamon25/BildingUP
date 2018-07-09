class Connection():
    def __init__(self, legth):
        self.length=legth
    
    def getInfo(self):
        return "Ich bin eine Verbindung der Länge: " + str(self.length)

