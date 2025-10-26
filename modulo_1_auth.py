import json

ARQUIVO_USUARIOS = 'usuarios.json'

def carregar_usuarios():
    """Carrega o 'banco de dados' de usuários do JSON."""
    try:
        with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo {ARQUIVO_USUARIOS} não encontrado.")
        return []

def autenticar(id_usuario, senha):
    """
    Verifica se o id_usuario e a senha correspondem a um usuário no banco.
    Retorna True se for válido, False caso contrário.
    """
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['id_usuario'] == id_usuario and usuario['senha'] == senha:
            return True
    return False

def exibir_login():
    """Exibe a interface de login e coleta as credenciais."""
    print("\n--- MÓDULO 1: Controle de Acesso ---")
    print("Por favor, identifique-se.")
    id_usuario = input("ID de Usuário: ")
    senha = input("Senha:         ")
    return id_usuario, senha

# --- Bloco de Teste do Aluno 1 ---
# Isso permite ao Aluno 1 testar seu módulo isoladamente.
if __name__ == "__main__":
    print("Executando teste do Módulo 1 (Autenticação)...")
    
    # Simula uma tentativa de login
    # id_teste, senha_teste = "a-001", "123" # Teste de Sucesso
    id_teste, senha_teste = "a-001", "senha_errada" # Teste de Falha
    
    print(f"Testando com ID: {id_teste} e Senha: {senha_teste}")
    
    sucesso = autenticar(id_teste, senha_teste)
    
    if sucesso:
        print("Resultado do Teste: SUCESSO na autenticação.")
        print(f"Próximo passo: Enviar '{id_teste}' para o Módulo 2.")
    else:
        print("Resultado do Teste: FALHA na autenticação.")