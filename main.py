# Este arquivo importa o trabalho de todos os alunos
import modulo_1_auth
import modulo_2_logica
import modulo_3_logs

def iniciar_sistema():
    """
    Função principal que orquestra o fluxo completo do sistema.
    """
    while True:
        print("\n=================================================")
        print("SISTEMA DE CONTROLE DE ACESSO INTELIGENTE (v1.0)")
        print("[1] Tentar Acesso")
        print("[2] Ver Dashboard de Logs")
        print("[3] Sair")
        
        escolha = input("Digite sua opção: ")
        
        if escolha == '1':
            # --- Aluno 1 Apresenta (Módulo 1) ---
            id_usuario, senha = modulo_1_auth.exibir_login()
            autenticado = modulo_1_auth.autenticar(id_usuario, senha)
            
            if autenticado:
                print("\n[Módulo 1] -> Autenticação OK.")
                
                # --- Aluno 2 Apresenta (Módulo 2) ---
                # Módulo 1 "chama" o Módulo 2
                print("[Módulo 1] -> Enviando dados para Módulo 2...")
                status, mensagem = modulo_2_logica.verificar_permissao(id_usuario)
                
                # Módulo 2 retorna o resultado
                print(f"[Módulo 2] -> Resultado: {mensagem}")
                
                # (O Módulo 3 é chamado automaticamente pelo Módulo 2)
                # --- Aluno 3 Apresenta (Módulo 3) ---
                print("[Módulo 2] -> Enviando log para Módulo 3...")
                
            else:
                # Falha na autenticação (Módulo 1)
                print("\n[Módulo 1] -> Falha na Autenticação (Usuário ou Senha inválidos).")
                
                # --- Aluno 3 Apresenta (Módulo 3) ---
                # Mesmo se a autenticação falhar, NÓS DEVEMOS REGISTRAR O LOG.
                # O main() chama o Módulo 3 diretamente neste caso.
                print("[Módulo 1] -> Enviando log de falha para Módulo 3...")
                evento_falha = {
                    "id_usuario": id_usuario,
                    "status": False,
                    "mensagem": "Falha na Autenticação (Senha Incorreta)"
                }
                modulo_3_logs.registrar_log(evento_falha)

        elif escolha == '2':
            # --- Aluno 3 Apresenta (Dashboard) ---
            modulo_3_logs.exibir_dashboard_logs()
        
        elif escolha == '3':
            print("Desligando o sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# --- Ponto de Entrada Principal ---
if __name__ == "__main__":
    iniciar_sistema()