import SocketServer
import SimpleHTTPServer

class HttpReqHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path=='/admin':
			self.wfile.write('This page is for admins')
			self.wfile.write(self.headers)
		else:
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpserver = SocketServer.TCPServer(('',1004), HttpReqHandler)
httpserver.serve_forever()
