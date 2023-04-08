from func import *

def test_senhas_len():
    assert True == checarLenSenha("947811934159")
    assert False == checarLenSenha("odfh")

def test_senhas_car_spec():                    
    assert True ==  checarCarSpecSenha("GabrielKetterma!")
    assert True ==  checarCarSpecSenha("Gab rielKetterma")
    assert False ==  checarCarSpecSenha("ifudgsisodfhiudsgfisg")

def test_senhas_num():
    assert True == checarNumSenha("GabrielKetterma123!")
    assert False == checarNumSenha("GabrielKetterma!")

def test_senhas_any_upper():
    assert True == checarAnyUpperSenha("GabrielKetterma123!")
    assert False == checarAnyUpperSenha("gabrielketterma123!")

def test_senhas_any_lower():
    assert True == checarAnyLowerSenha("GabrielKetterma123!")
    assert False == checarAnyLowerSenha("GABRIELKETTERMA123!")

def test_senhas_final():
    assert "GabrielKetterma123!" == checarSenha("GabrielKetterma123!")
    assert None == checarSenha("INFERNODESGRAÇA123!")
    assert None == checarSenha("infernodesgraça123!")
    assert "Gabriel Ketterma123" == checarSenha("Gabriel Ketterma123")
    assert None == checarSenha("Gabriel1!")
    assert None == checarSenha("gabrielketterma")
    assert None == checarSenha("GABRIELKETTERMA")
