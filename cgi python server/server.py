from http.server import HTTPServer, CGIHTTPRequestHandler
import time
server_address = ('192.168.123.95', 800)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
begin_time = time.asctime()
print('Server started on', begin_time)
print('Server is running on address', server_address[0], 'on port', server_address[1])
httpd.serve_forever()
