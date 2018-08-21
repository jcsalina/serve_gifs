import glob
import sys
sys.path.append("gen-py")
sys.path.insert(0, glob.glob('../thrift-0.11.0/lib/py/build/lib*')[0])
from topgifs import TopGifsService
from src.DbInterface import DbInterface
from src.Gif import Gif
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class FetchGifHandler:
    def __init__(self):
        self.log = {}

    def fetchGif(self, gif_id):
        dbi = DbInterface()
        print("[Server] Handling client request")
        print("[Server] Consulted Gif ID: " + gif_id)
        dbi.getGifById("1")
        print("[Server] Creating Gif instance")
        gif = Gif(dbi.result)
        print("[Server] Answering request")
        # return gif
	my_list = []
	my_list.append(str(gif.gif_id))
	my_list.append(gif.url)
	my_list.append(gif.description)
	my_list.append(str(gif.count))
	return my_list
	
if __name__ == '__main__':
    handler = FetchGifHandler()
    proc = TopGifsService.Processor(handler)
    trans_svr = TSocket.TServerSocket(port=9090)
    trans_fac = TTransport.TBufferedTransportFactory()
    proto_fac = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(proc, trans_svr, trans_fac, proto_fac)
    print('Starting the server...')
    server.serve()
