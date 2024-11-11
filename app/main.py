from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session
from models.usuario import Usuario
import os 
def main():
    usuario = Usuario()
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)


    # Create dados do usuário.
    print("\nAdicionando usuário: ")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Read dados do usuário sendo listado.
    print("\nListando usuários cadastrados: ")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} \nE-mail: {usuario.email} \nSenha: {usuario.senha}\n\n")


if __name__ == "__main__":
    os.system("cls || clear")
    main()
