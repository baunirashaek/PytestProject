from func import *

def test_username():
    assert False == checarUpper("jorge")
    assert True == checarUpper("Jorge")

    assert False == checarCarSpec("!Jorge")
    assert True == checarCarSpec("Jorge")

    assert True == checarLen("Jorge")
    assert False == checarLen("FKLDGSFUIODYGUIOSDFHGISDYGBOSDFHGBJPFODXHOFGUHÇDFGKOCHLGJHKLDFTUYHBRDXNGOJKHFGNHKLFTJYHNKLFJCPBOJTKLH")


    assert "Jorge" == checarLogin("Jorge")
    assert None == checarLogin("idiota123!")
    assert "Inferno" == checarLogin("Inferno")
    assert None == checarLogin("idiota")
