from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)
    #criando usuario
    service.criar_usuario("SALO","@gmail","1234")
    #listando usuario
    print("\nListando todos Usuarios.")
    lista_usuario = service.listar_todos_usuarios()
    for usuario in lista_usuario:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "main":
    main() # chamada para função.        