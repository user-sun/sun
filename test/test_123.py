import pytest


def testgg1():
    assert 1 =='1231'

def testgg2():
    assert 1 ==2

def testgg3():
    assert 1 ==3

def testgg4():
    assert 1 ==4

if __name__ == '__main__':
    # pytest.main(['-n','auto', 'test_123.py'])
    pytest.main(['--tb=line','test_123.py','--reruns-delay=2'])