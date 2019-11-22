class Serializer():
    textEntry = "01"
    pseudo = "00"
    disconnected = "10"
    pseudoList = "02"

    @staticmethod
    def serializeTextEntry(msg):
        msg = Serializer.textEntry + msg
        return msg.encode()

    @staticmethod
    def serializePseudo(msg):
        msg = Serializer.pseudo + msg
        return msg.encode()

    @staticmethod
    def serializeDisconnection():
        return Serializer.disconnected.encode()

    @staticmethod
    def serializePseudoList(pseudoList):
        pseudosString = Serializer.pseudoList
        for string in pseudoList:
            pseudosString = pseudosString + string + "/"
        return pseudosString.encode()


