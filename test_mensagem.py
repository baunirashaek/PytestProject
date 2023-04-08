from func import *

def test_mensagem():
    assert True == checarLenMensagem("sdhfudshuihsdfiushidufhsiudhfuisdh")
    assert False == checarLenMensagem("sdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdh")

def test_mensagem_final():
    assert None == checarMensagem("sdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdh")
    assert "sdhfudshuihsdfiushidufhsiudhfuisdh" == checarMensagem("sdhfudshuihsdfiushidufhsiudhfuisdh")
