from func import *

def test_user():

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

    assert True == checarLenSenha("Queromematar")
    assert False == checarLenSenha("odfh")

    assert True ==  checarCarSpecSenha("InfernoDesgraça!")
    assert True ==  checarCarSpecSenha("Inf ernoDesgraça")
    assert False ==  checarCarSpecSenha("ifudgsisodfhiudsgfisg")

    assert True == checarNumSenha("InfernoDesgraça123!")
    assert False == checarNumSenha("InfernoDesgraça!")

    assert True == checarAnyUpperSenha("InfernoDesgraça123!")
    assert False == checarAnyUpperSenha("infernodesgraça123!")

    assert True == checarAnyLowerSenha("InfernoDesgraça123!")
    assert False == checarAnyLowerSenha("INFERNODESGRAÇA123!")

    assert "InfernoDesgraça123!" == checarSenha("InfernoDesgraça123!")
    assert None == checarSenha("INFERNODESGRAÇA123!")
    assert None == checarSenha("infernodesgraça123!")
    assert "Inferno Desgraça123" == checarSenha("Inferno Desgraça123")
    assert None == checarSenha("Inferno1!")
    assert None == checarSenha("infernodesgraça")
    assert None == checarSenha("INFERNODESGRAÇA")

    assert True == checarLenMensagem("sdhfudshuihsdfiushidufhsiudhfuisdh")
    assert False == checarLenMensagem("sdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdh")

    assert None == checarMensagem("sdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdhsdhfudshuihsdfiushidufhsiudhfuisdh")
    assert "sdhfudshuihsdfiushidufhsiudhfuisdh" == checarMensagem("sdhfudshuihsdfiushidufhsiudhfuisdh")
    