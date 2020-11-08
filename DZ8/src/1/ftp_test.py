import pytest
import sys
import os

sys.path.append('.')
import ftp


def test_ftp(server, port, user, passwd):
    if port is None:
        f = ftp.Ftp(server, user, passwd)
    else:
        f = ftp.Ftp(server, user, passwd, port)
    c = f.connect()
    assert '220' in c
    h = f.get_list()
    b = os.stat('/etc/services').st_size
    m = f.send_file('/etc/services', ' services ')
    assert '226' in m
    h = f.get_list()
    assert 'services' in ''.join(h)
    s = f.get_file('services')
    assert len(s[1]) >= b
    f.close()

