from func import *

def test_mensagem():
    assert True == checarLenMensagem("sdhfudshuihsdfiushidufhsiudhfuisdh")
    assert False == checarLenMensagem("sdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdh")

    assert None == checarMensagem("sdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdh")
    assert "sdhfudshuihsdfiushidufhsiudhfuisdh" == checarMensagem("sdhfudshuihsdfiushidufhsiudhfuisdh")
