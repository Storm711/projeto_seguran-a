import datetime

ARQUIVO_LOG = 'acessos.log'
# Este dicionário "em memória" rastreia falhas consecutivas
falhas_consecutivas = {}

def registrar_log(evento):
    """
    Recebe um evento (do Módulo 2 ou Main) e o escreve no arquivo de log.
    """
    agora = datetime.datetime.now().isoformat()
    
    # Pega os dados do evento
    id_usuario = evento['id_usuario']
    status = evento['status']
    mensagem = evento['mensagem']
    
    log_line = f"[{agora}] - Usuário: {id_usuario} - Sucesso: {status} - Msg: {mensagem}\n"
    
    # Escreve no arquivo de log (modo 'a' = append/anexar)
    try:
        with open(ARQUIVO_LOG, 'a', encoding='utf-8') as f:
            f.write(log_line)
    except Exception as e:
        print(f"Erro Crítico no Módulo 3: Não foi possível escrever o log. {e}")

    # Imprime no console para efeito de "tempo real"
    print(f"\n--- MÓDULO 3 (LOG): {log_line.strip()} ---")
    
    # Chama a função de verificação de alertas
    verificar_alertas(id_usuario, status)

def verificar_alertas(id_usuario, status_sucesso):
    """Verifica se 3 falhas consecutivas ocorreram para este usuário."""
    global falhas_consecutivas
    
    if status_sucesso:
        # Se o acesso foi um sucesso, zera o contador de falhas
        falhas_consecutivas[id_usuario] = 0
    else:
        # Se foi uma falha, incrementa o contador
        count_falhas = falhas_consecutivas.get(id_usuario, 0) + 1
        falhas_consecutivas[id_usuario] = count_falhas
        
        print(f"--- MÓDULO 3 (ALERTA): {id_usuario} tem {count_falhas} falha(s) consecutiva(s). ---")
        
        # Dispara o alerta!
        if count_falhas >= 3:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"!!! ALERTA DE SEGURANÇA: 3 TENTATIVAS FALHAS !!!")
            print(f"!!! Usuário: {id_usuario}. Bloqueio temporário recomendado.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            # Reseta o contador após o alerta
            falhas_consecutivas[id_usuario] = 0

def exibir_dashboard_logs():
    """Lê o arquivo de log e exibe todo o histórico."""
    print("\n--- MÓDULO 3: Dashboard de Monitoramento (Histórico) ---")
    try:
        with open(ARQUIVO_LOG, 'r', encoding='utf-8') as f:
            logs = f.read()
            if not logs:
                print("Nenhum evento de acesso registrado ainda.")
            else:
                print(logs)
    except FileNotFoundError:
        print("Nenhum evento de acesso registrado ainda.")
    print("---------------------------------------------------------")

# --- Bloco de Teste do Aluno 3 ---
if __name__ == "__main__":
    print("Executando teste do Módulo 3 (Logs e Alertas)...")

    # Simula 3 falhas seguidas
    evento_falha_1 = {"id_usuario": "invasor-01", "status": False, "mensagem": "Falha 1"}
    evento_falha_2 = {"id_usuario": "invasor-01", "status": False, "mensagem": "Falha 2"}
    evento_falha_3 = {"id_usuario": "invasor-01", "status": False, "mensagem": "Falha 3"}
    
    # Simula um sucesso
    evento_sucesso = {"id_usuario": "a-001", "status": True, "mensagem": "Sucesso"}

    print("\nSimulando 3 falhas:")
    registrar_log(evento_falha_1)
    registrar_log(evento_falha_2)
    registrar_log(evento_falha_3) # O alerta deve disparar aqui
    
    print("\nSimulando 1 sucesso:")
    registrar_log(evento_sucesso)

    # Mostra o dashboard no final
    exibir_dashboard_logs()