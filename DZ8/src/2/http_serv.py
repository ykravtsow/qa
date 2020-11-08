import socket


class http_serv:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('0.0.0.0', 8888))
        self.sock.listen(1)
        self.run()

    def run(self):
        while True:
            self.conn, self.addr = self.sock.accept()
            self.conn.setblocking(True)
            self.conn.settimeout(1)
            print('connect from ', self.addr)
            buffer = b''
            while True:
                data = None
                try:
                    data = self.conn.recv(16)
                except socket.timeout:
                    pass
                if not data:
                    break
                buffer = buffer + data
            self.send_data(buffer)
            self.conn.close()

    def send_data(self, buffer):
        s = str(buffer, encoding='utf=8')
        pos = s.find('\n')
        s = s[pos:]
        buf = s.split('\r\n')
        s = ''
        for h in buf:
            if len(h) == 0:
                continue
            s = s + '<tr><td>' + h + '</td></tr>\r\n'
        print('send string:', s)
        payload = '<HTML><HEAD></HEAD><BODY><TABLE>' + s + '</TABLE></BODY></HTML>'
        output = 'HTTP/1.1 200 OK\r\nServer: MY\r\nAccept-Ranges: bytes\r\nContent-length: ' + \
                 str(len(payload)) + \
                 '\r\n\r\n' + \
                 payload
        self.conn.send(bytes(output, encoding='utf-8'))


H = http_serv()
