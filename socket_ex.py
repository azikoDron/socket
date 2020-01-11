import socket

sock = socket.socket()
sock.bind(('', 8089))
sock.listen()
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break   # anything u wont  
    conn.send(data.upper())
conn.close()


#
# addr = ("", 8089)  # all interfaces, port 8080
# if socket.has_dualstack_ipv6():
#     s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
# else:
#     s = socket.create_server(addr)

# import SimpleHTTPServer
# import SocketServer

# PORT = 8089

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# httpd = SocketServer.TCPServer(("", PORT), Handler)

# print "serving at port", PORT
# httpd.serve_forever()
