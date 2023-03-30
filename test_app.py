from app import *

def test_user():
    assert checarLogin("Carlos") == "Carlos"
    assert checarSenha("Senhademerda123!") == "Senhademerda123!"
    assert checarMensagem("sadgfsiodyufguisgudfs") == "sadgfsiodyufguisgudfs"

    assert checarLogin("jorge") == None
    assert checarSenha("senhadesgraçada") == None
