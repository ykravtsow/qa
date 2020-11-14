import pytest
import sys

sys.path.append('.')
import ssh


def test_ssh(server, port, user, passwd):
    if port is None:
        f = ssh.Ssh(server, user, passwd)
    else:
        f = ssh.Ssh(server, user, passwd, port)
    c = f.connect()
    l = f.command('rm -f /tmp/ssh_test.txt')
    assert 0 == len(l[2].readlines())
    l = f.command('echo "test" >> /tmp/ssh_test.txt')
    assert 0 == len(l[2].readlines())
    l = f.command('cat /tmp/ssh_test.txt')
    assert 0 == len(l[2].readlines())
    assert 'test\n' in l[1].readlines()
    f.close()
