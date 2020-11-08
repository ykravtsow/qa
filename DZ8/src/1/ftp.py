import ftplib


class Ftp:

    def __init__(self, ip, user, passwd, port=21):
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.port = port
        self.ftp = ftplib.FTP()

    def connect(self):
        self.ftp.connect(self.ip, self.port)
        self.ftp.login(self.user, self.passwd)
        w = self.ftp.getwelcome()
        #self.ftp.sendcmd('PORT')
        self.ftp.set_pasv(True)
        return w

    def command(self, command):
        return self.ftp.sendcmd(command)

    def send_file(self, name, remote=None):
        if remote is None:
            remote = name
        f = ''
        with open(name, 'rb') as r:
            f = self.ftp.storbinary('STOR '+remote, r)
        return f

    def get_file(self, remote):
        content = []
        return self.ftp.retrbinary('RETR '+remote, content.append), ''.join(map(str, content))

    def get_list(self):
        files = []
        self.ftp.dir(files.append)
        return files

    def close(self):
        self.ftp.close()
