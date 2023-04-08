from func import *

def test_username_upper():
    assert False == checarUpper("jorge")
    assert True == checarUpper("Jorge")

def test_useranme_car_spec():
    assert False == checarCarSpec("!Jorge")
    assert True == checarCarSpec("Jorge")

def test_username_len():
    assert True == checarLen("Jorge")
    assert False == checarLen("FKLDGSFUIODYGUIOSDFHGISDYGBOSDFHGBJPFODXHOFGUHÇDFGKOCHLGJHKLDFTUYHBRDXNGOJKHFGNHKLFTJYHNKLFJCPBOJTKLH")

def test_username_final():
    assert "Jorge" == checarLogin("Jorge")
    assert None == checarLogin("ahsjdr123!")
    assert "Gabriel" == checarLogin("Gabriel")
    assert None == checarLogin("ahsjdr")
