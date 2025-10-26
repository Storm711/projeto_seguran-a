import json
import datetime
# O Aluno 2 precisa "chamar" o Aluno 3
import modulo_3_logs 

ARQUIVO_REGRAS = 'regras.json'

def carregar_regras():
    """Carrega o 'banco de dados' de regras do JSON."""
    try:
        with open(ARQUIVO_REGRAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo {ARQUIVO_REGRAS} não encontrado.")
        return {}

def verificar_permissao(id_usuario):
    """
    Verifica se o usuário autenticado tem permissão de acesso
    baseado nas regras (sala e horário).
    """
    regras = carregar_regras()
    hora_atual = datetime.datetime.now().hour
    
    if id_usuario not in regras:
        mensagem = "Acesso Negado: Usuário não possui regras de acesso."
        status = False
    else:
        regra_usuario = regras[id_usuario]
        sala = regra_usuario['sala']
        inicio = regra_usuario['horario_inicio']
        fim = regra_usuario['horario_fim']
        
        # Verifica a regra de horário
        if inicio <= hora_atual < fim:
            mensagem = f"Acesso Concedido: Bem-vindo(a) à {sala}."
            status = True
        else:
            mensagem = f"Acesso Negado: Fora do horário permitido ({inicio}h-{fim}h)."
            status = False

    # --- Ponto de Comunicação (Módulo 2 -> Módulo 3) ---
    # Cria o "evento" para enviar ao módulo de logs
    evento = {
        "id_usuario": id_usuario,
        "status": status,
        "mensagem": mensagem
    }
    # Envia o evento para o Módulo 3 registrar
    modulo_3_logs.registrar_log(evento)
    # ----------------------------------------------------

    return status, mensagem

# --- Bloco de Teste do Aluno 2 ---
if __name__ == "__main__":
    print("Executando teste do Módulo 2 (Lógica de Acesso)...")
    
    # Simula a entrada do Módulo 1
    # id_teste = "a-001" # Teste de acesso (depende da hora do dia)
    # id_teste = "b-002" # Teste de acesso (depende da hora do dia)
    id_teste = "usuario_inexistente" # Teste de falha (sem regra)

    print(f"Testando permissão para: {id_teste}")
    
    # (Para este teste, o modulo_3_logs.py deve existir no mesmo diretório)
    status, msg = verificar_permissao(id_teste)
    
    print(f"\nResultado do Teste do Módulo 2:")
    print(f"Status: {status}")
    print(f"Mensagem: {msg}")
    print("(Verifique o 'acessos.log' para ver se o evento foi registrado)")