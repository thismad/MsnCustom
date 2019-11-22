class Deserializer:

    @staticmethod
    def deserializeMsg(msg):
        """ deserialize and decode the message"""
        msgDecoded = msg.decode()
        return msgDecoded[0:2], msgDecoded[2:]

