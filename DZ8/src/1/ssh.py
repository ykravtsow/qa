import paramiko
import os


class Ssh:

    def __init__(self, ip, user, passwd=None, port=22):
        self.ip = ip
        self.user = user
        self.port = port
        self.passwd = passwd
        self.paramiko = paramiko.client.SSHClient()
        self.paramiko.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

    def connect(self):
        self.paramiko.connect(self.ip, self.port, self.user, self.passwd)

    def command(self, command):
        cin, cout, cerr = self.paramiko.exec_command(command, timeout=20)
        return cin, cout, cerr

    def close(self):
        self.paramiko.close()

