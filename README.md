

Conceito do Projeto: Sistema de Controle de Acesso Inteligente
O sistema simula a segurança de um escritório ou laboratório. Ele deve autenticar usuários, verificar suas permissões de acesso e registrar todas as tentativas de entrada.

Divisão dos Módulos (1 por Aluno)
Abaixo está a divisão do trabalho. O mais importante é que, no início, os três alunos devem se reunir por 15 minutos para definir a "interface" de comunicação entre os módulos (como um módulo "chama" o outro), que será muito simples.

Aluno 1: Módulo de Autenticação e Gestão de Usuários
Este módulo é a "porta de entrada" do sistema. Ele é responsável por saber quem é o usuário.

Objetivo: Criar a interface onde o usuário se identifica e gerenciar o banco de dados de usuários.

Tarefas de Desenvolvimento:

Banco de Dados de Usuários: Criar um banco de dados (pode ser um arquivo JSON, um CSV ou um banco SQL simples) para armazenar os usuários. Cada usuário deve ter:

id_usuario (ex: "aluno_1")

senha (ou um PIN)

nome_completo

Interface de Login: Criar uma tela simples (pode ser web, desktop ou até mesmo um prompt de comando) onde o usuário digita seu ID e senha.

Lógica de Autenticação: Uma função que recebe o id_usuario e a senha, verifica no banco de dados se eles estão corretos e retorna True (sucesso) ou False (falha).

Comunicação (Ação): Se a autenticação for um sucesso (True), este módulo deve "avisar" o Módulo 2, enviando o id_usuario que acabou de ser autenticado.

Apresentação (Dia 1): O Aluno 1 apresenta o sistema de cadastro e login. Ele demonstra:

Como adicionar um novo usuário ao banco de dados.

Uma tentativa de login com falha (senha errada).

Uma tentativa de login com sucesso.

Explica como seu módulo envia o ID do usuário autenticado para o Módulo 2 (mesmo que o Módulo 2 ainda não esteja "conectado").

Aluno 2: Módulo de Lógica de Acesso e Permissões (O "Cérebro")
Este módulo é o "cérebro" que toma as decisões. Ele recebe o usuário autenticado do Módulo 1 e decide se ele pode ou não pode entrar.

Objetivo: Implementar as regras de negócio que definem quem pode acessar e quando.

Tarefas de Desenvolvimento:

Banco de Dados de Regras: Criar um banco de dados de permissões. Exemplo:

id_usuario: "aluno_1", permissao: "laboratorio_A", horario: "08:00-18:00"

id_usuario: "professor_X", permissao: "laboratorio_A", horario: "24h"

id_usuario: "aluno_2", permissao: "laboratorio_B", horario: "09:00-17:00"

Lógica de Verificação: Criar uma função principal que recebe o id_usuario (do Módulo 1).

Essa função deve verificar no banco de regras se aquele usuário tem permissão para entrar naquele momento (pode usar a hora atual do sistema).

Comunicação (Ação):

Se o acesso for concedido: O módulo deve enviar um comando "ABRIR" (pode ser um simples print("Porta Aberta") ou uma simulação de hardware).

Em qualquer caso (concedido ou negado): O módulo deve enviar um registro do evento para o Módulo 3. (Ex: {"usuario": "aluno_1", "acao": "acesso_concedido", "timestamp": "..."}).

Apresentação (Dia 2): O Aluno 2 apresenta o motor de regras. Ele pode simular a entrada do Aluno 1 (não precisa do Módulo 1 funcionando). Ele demonstra:

Uma tentativa de acesso de um usuário dentro do seu horário permitido (resultado: Acesso Concedido).

A mesma tentativa fora do horário permitido (resultado: Acesso Negado).

Uma tentativa de acesso de um usuário sem permissão alguma (resultado: Acesso Negado).

Explica como seu módulo envia o resultado (log) para o Módulo 3.

Aluno 3: Módulo de Monitoramento, Logs e Alertas
Este módulo são os "olhos" do sistema. Ele não toma decisões, apenas registra tudo o que acontece e alerta sobre comportamentos estranhos.

Objetivo: Criar um histórico (log) de todas as tentativas de acesso e gerar alertas de segurança.

Tarefas de Desenvolvimento:

Receptor de Logs: Criar uma função que "escuta" as mensagens enviadas pelo Módulo 2.

Arquivo de Log: Armazenar todas as mensagens recebidas (seja acesso concedido ou negado) em um arquivo de texto (acessos.log), incluindo data e hora.

Dashboard de Monitoramento: Criar uma tela (web, desktop ou console) que lê o acessos.log e exibe os eventos em tempo real, mostrando quem tentou entrar, quando, e se conseguiu.

Sistema de Alertas: Implementar uma lógica simples de alerta. Exemplo: Se o sistema registrar 3 tentativas de acesso "negado" do mesmo usuário (ou do mesmo local) em menos de 1 minuto, ele deve disparar um alerta (ex: print("ALERTA: POSSÍVEL INVASÃO!") ou enviar um e-mail).

Apresentação (Dia 3): O Aluno 3 apresenta o painel de controle e segurança. Ele pode simular a entrada de eventos do Módulo 2. Ele demonstra:

O dashboard mostrando os logs em tempo real.

O que acontece quando ele simula 3 falhas de login seguidas (o sistema de alerta disparando).

Como o histórico de acessos fica salvo para auditoria.

Como Garantir que Não Haja Complicações
A independência é garantida pela definição clara das Interfaces de Comunicação (APIs):

Interface (Aluno 1 -> Aluno 2):

O Aluno 1 só precisa "chamar" uma função do Aluno 2.

Exemplo: Aluno2.verificar_permissao(id_usuario="aluno_1")

Interface (Aluno 2 -> Aluno 3):

O Aluno 2 só precisa "chamar" uma função do Aluno 3.

Exemplo: Aluno3.registrar_log(evento={"usuario": "aluno_1", "acao": "negado", "timestamp": "..."})

Cada aluno pode criar uma "versão falsa" (um mock) dos outros módulos para testar o seu.

O Aluno 1 pode criar um Aluno2.verificar_permissao falso que só imprime "Recebido!" na tela.

O Aluno 2 pode testar o seu módulo chamando-o manualmente, sem precisar do Aluno 1.

O Aluno 3 pode testar o seu módulo chamando Aluno3.registrar_log manualmente.

Apresentação Final (Todos Juntos)
No dia da apresentação final, vocês conectam os três módulos. O fluxo será completo:

O Aluno 1 digita um usuário e senha.

O Módulo 1 autentica e chama o Módulo 2.

O Módulo 2 verifica as regras e nega o acesso (ex: fora de hora).

O Módulo 2 chama o Módulo 3.

O Módulo 3 (apresentado pelo Aluno 3) mostra o "Acesso Negado" no dashboard em tempo real.

Isso cobre todos os requisitos, permite trabalho paralelo e cria um projeto de segurança coeso e completo.

A estrutura do projeto será esta:

projeto_seguranca/
├── usuarios.json        (Banco de dados do Aluno 1)
├── regras.json          (Banco de dados do Aluno 2)
├── acessos.log          (Arquivo de log do Aluno 3)
│
├── modulo_1_auth.py     (Código do Aluno 1)
├── modulo_2_logica.py   (Código do Aluno 2)
├── modulo_3_logs.py     (Código do Aluno 3)
│
└── main.py              (Arquivo da Apresentação Final)
Passo 1: Os "Bancos de Dados" (Arquivos JSON)
Crie estes dois arquivos primeiro.

usuarios.json
(Este arquivo é usado pelo Aluno 1)

JSON
[
  {
    "id_usuario": "a-001",
    "nome": "Alice Silva",
    "senha": "123"
  },
  {
    "id_usuario": "b-002",
    "nome": "Bruno Costa",
    "senha": "456"
  },
  {
    "id_usuario": "g-003",
    "nome": "Gabriel Lima (Admin)",
    "senha": "789"
  }
]
regras.json
(Este arquivo é usado pelo Aluno 2. Note que usamos horas em formato 24h como números inteiros para simplificar)

JSON
{
  "a-001": {
    "sala": "Laboratório A",
    "horario_inicio": 8,
    "horario_fim": 18
  },
  "b-002": {
    "sala": "Biblioteca",
    "horario_inicio": 9,
    "horario_fim": 17
  },
  "g-003": {
    "sala": "Sala dos Servidores",
    "horario_inicio": 0,
    "horario_fim": 24
  }
}
(Não é preciso criar o acessos.log, o Aluno 3 o criará automaticamente)

Passo 2: Os Módulos dos Alunos
Cada aluno pode copiar e colar seu código em seu próprio arquivo .py.

modulo_1_auth.py (Trabalho do Aluno 1)
Python
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
modulo_2_logica.py (Trabalho do Aluno 2)
Python
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
modulo_3_logs.py (Trabalho do Aluno 3)
Python
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
Passo 3: A Apresentação Final (Integrando Tudo)
Este é o arquivo que junta o trabalho de todos.

main.py
Python
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
Como Executar
Salve todos os 6 arquivos na mesma pasta.

Cada aluno pode testar seu módulo individualmente primeiro:

python modulo_1_auth.py

python modulo_2_logica.py

python modulo_3_logs.py

Para a apresentação final, rodem o arquivo main.py:
