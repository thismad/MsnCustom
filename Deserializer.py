class Deserializer:

    @staticmethod
    def deserializeMsg(msg):
        """ deserialize and decode the message"""
        if isinstance(msg,str):
            return msg[0:2], msg[2:]
        else :
            msgDecoded = msg.decode()
            return msgDecoded[0:2], msgDecoded[2:]


