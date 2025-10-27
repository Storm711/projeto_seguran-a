

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

por favor, gere o código

Com certeza!

Aqui está o código-fonte completo para o projeto, dividido em arquivos separados. A linguagem usada será Python, por ser simples e excelente para prototipagem.

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

python main.py

por favor, faça uma descrição do projeto, não precisa ser de forma resumida

Aqui está uma descrição de projeto detalhada e completa, cobrindo os objetivos, arquitetura, funcionalidades e a estratégia de desenvolvimento em equipe que você solicitou.

Descrição de Projeto: Sistema de Controle de Acesso Inteligente (SCAI)
1. Introdução
Este documento descreve o projeto, a arquitetura e a implementação do "Sistema de Controle de Acesso Inteligente" (SCAI). O SCAI é uma solução de software desenvolvida como um protótipo para simular, gerenciar e monitorar o acesso físico a áreas restritas, como laboratórios, escritórios ou salas de servidores.

O principal desafio deste projeto não é apenas criar um sistema de segurança funcional, mas também estruturá-lo de forma a permitir que uma equipe de três desenvolvedores (alunos) trabalhe de forma paralela, independente e sem conflitos. Para alcançar isso, o sistema é fundamentado em uma arquitetura modular de três componentes, onde cada componente é fracamente acoplado e se comunica através de interfaces (APIs) simples e bem definidas.

Os três módulos principais são:

Módulo de Autenticação e Gestão de Identidade: O "porteiro" que valida quem é o usuário.

Módulo de Lógica e Permissões: O "cérebro" que decide se o usuário pode entrar com base em regras.

Módulo de Monitoramento e Logs: O "vigilante" que registra tudo e dispara alertas.

2. Justificativa e Problema Solucionado
No mundo real, o controle de acesso físico é uma pedra angular da segurança. Sistemas legados baseados em chaves físicas são falhos — chaves podem ser perdidas, copiadas ou roubadas. Um sistema inteligente resolve isso ao centralizar o controle, permitindo não apenas a identificação, mas também a aplicação de regras complexas (como restrições de horário) e a criação de um registro de auditoria infalível.

Do ponto de vista acadêmico e de desenvolvimento, o projeto aborda um problema comum em engenharia de software: como coordenar uma equipe para construir um único produto. A falha em gerenciar dependências leva a atrasos, conflitos de código (merge conflicts) e frustração. A arquitetura modular proposta resolve isso ao aplicar o princípio da Separação de Preocupações (Separation of Concerns). Cada aluno se torna especialista em um domínio (identidade, regras, vigilância), permitindo desenvolvimento focado e testes isolados.

3. Objetivos
Objetivo Geral
Desenvolver um protótipo funcional de um sistema de controle de acesso, demonstrando um fluxo completo desde a identificação do usuário até o registro da tentativa de acesso, utilizando uma arquitetura que facilita o desenvolvimento paralelo e a integração.

Objetivos Específicos
Para o Aluno 1: Implementar um microsserviço de autenticação capaz de validar credenciais de usuário (ID e senha) contra um banco de dados persistente (JSON).

Para o Aluno 2: Criar um motor de regras flexível que ingere um ID de usuário autenticado e determina seus privilégios de acesso com base em regras de negócio (ex: sala permitida, faixa de horário).

Para o Aluno 3: Construir um sistema de auditoria e alerta que registre todas as tentativas de acesso (concedidas ou negadas) em um log persistente e identifique padrões de comportamento suspeitos (ex: múltiplas falhas consecutivas).

Para a Equipe: Integrar os três módulos de forma coesa, provando que a definição de interfaces claras permite que componentes desenvolvidos independentemente funcionem como um único sistema.

4. Arquitetura Detalhada do Sistema
O sistema é dividido em três arquivos Python principais (modulo_1_auth.py, modulo_2_logica.py, modulo_3_logs.py) e um orquestrador (main.py) que simula a interação do usuário e integra os módulos.

Módulo 1: Gestão de Identidade e Autenticação ("O Porteiro")
Responsável: Aluno 1

Componentes: modulo_1_auth.py, usuarios.json

Descrição: Este módulo é a porta de entrada do sistema. Sua única responsabilidade é responder à pergunta: "Este usuário é quem ele diz ser?". Ele não sabe sobre permissões, horários ou logs.

Banco de Dados (usuarios.json): Armazena uma lista de objetos de usuário, cada um contendo id_usuario, nome e senha. Para este protótipo, a senha está em texto plano, mas em um sistema real, estaria hashed.

Função Principal (autenticar(id_usuario, senha)):

Recebe um id_usuario e uma senha.

Lê o usuarios.json.

Itera pela lista e procura uma correspondência exata.

Retorna True se a combinação for encontrada, ou False caso contrário.

Interface (Saída): Um valor booleano (sucesso/falha da autenticação).

Módulo 2: Lógica de Negócio e Permissões ("O Cérebro")
Responsável: Aluno 2

Componentes: modulo_2_logica.py, regras.json

Descrição: Este é o motor de decisão. Ele só entra em ação após o Módulo 1 confirmar a identidade do usuário. Sua responsabilidade é responder: "Este usuário autenticado tem permissão para entrar agora?"

Banco de Dados (regras.json): Armazena um dicionário onde as chaves são os id_usuario. Cada valor é um objeto de regra contendo sala, horario_inicio e horario_fim.

Função Principal (verificar_permissao(id_usuario)):

Recebe um id_usuario (que já foi validado pelo M1).

Obtém a hora atual do sistema.

Lê o regras.json e busca as regras para aquele id_usuario.

Lógica 1 (Existência): O usuário existe nas regras? Se não, acesso negado.

Lógica 2 (Horário): A hora atual está dentro da janela horario_inicio e horario_fim? Se não, acesso negado.

Se ambas as lógicas passarem, o acesso é concedido.

Interface (Entrada): id_usuario.

Interface (Saída): Um status (Concedido/Negado) e uma mensagem explicativa.

Dependência: Este módulo chama o Módulo 3 para registrar sua decisão.

Módulo 3: Monitoramento, Logs e Alertas ("O Vigilante")
Responsável: Aluno 3

Componentes: modulo_3_logs.py, acessos.log

Descrição: Este módulo é o sistema de auditoria. Ele não toma decisões. Sua função é "ouvir" os eventos do sistema e registrá-los de forma imutável, além de analisar esses eventos em busca de ameaças.

Arquivo de Log (acessos.log): Um arquivo de texto simples onde cada linha é um evento de acesso, formatado com timestamp, ID do usuário, status (sucesso/falha) e mensagem.

Função Principal (registrar_log(evento)):

Recebe um objeto evento (um dicionário Python contendo todos os detalhes da tentativa de acesso).

Formata esses dados em uma linha de log.

Anexa (append) essa linha ao arquivo acessos.log.

Exibe o log no console (simulando um painel em tempo real).

Chama a função verificar_alertas.

Função de Alerta (verificar_alertas(id_usuario, status)):

Usa um dicionário em memória (falhas_consecutivas) para rastrear falhas.

Se o status for sucesso, zera o contador daquele usuário.

Se o status for falha, incrementa o contador.

Se o contador atingir um limite (ex: 3), ele dispara um alerta de segurança no console.

Interface (Entrada): Um objeto evento.

5. Fluxo de Dados e Estratégia de Apresentação
O projeto é estruturado para três apresentações individuais, seguidas por uma apresentação final integrada.

Apresentação 1 (Aluno 1 - Módulo de Autenticação):

Foco: Identidade.

Demonstração: O aluno executa modulo_1_auth.py diretamente (if __name__ == "__main__").

Cenários:

Sucesso: O script testa um login com ID e senha corretos (ex: "a-001", "123") e imprime "SUCESSO na autenticação".

Falha: O script testa um login com senha errada (ex: "a-001", "senha_errada") e imprime "FALHA na autenticação".

Explicação: O aluno explica a estrutura do usuarios.json e a lógica simples de verificação da função autenticar.

Apresentação 2 (Aluno 2 - Módulo de Lógica):

Foco: Regras de Negócio.

Demonstração: O aluno executa modulo_2_logica.py diretamente.

Cenários:

Usuário Válido (Dentro do Horário): O script simula a entrada de "a-001" (assumindo que a hora atual está entre 8h e 18h). A saída é "Acesso Concedido".

Usuário Válido (Fora do Horário): O aluno pode alterar temporariamente o regras.json para que o horário de "a-001" seja inválido. Ao re-executar, a saída é "Acesso Negado: Fora do horário".

Usuário Inexistente: O script testa um "usuario_inexistente". A saída é "Acesso Negado: Usuário não possui regras".

Explicação: O aluno explica como o regras.json define as permissões e como a função verificar_permissao usa a biblioteca datetime para tomar decisões.

Apresentação 3 (Aluno 3 - Módulo de Monitoramento):

Foco: Auditoria e Segurança Ativa.

Demonstração: O aluno executa modulo_3_logs.py diretamente.

Cenários:

Registro de Eventos: O script simula o recebimento de vários eventos (um sucesso, uma falha). O aluno abre o arquivo acessos.log para provar que os dados foram persistidos.

Disparo de Alerta: O script simula 3 eventos de falha consecutivos para o mesmo usuário ("invasor-01"). Na terceira chamada, o console exibe o "ALERTA DE SEGURANÇA" em destaque.

Dashboard: O aluno mostra a execução da função exibir_dashboard_logs para exibir todo o histórico.

Explicação: O aluno explica a importância de um log imutável para auditoria e como o sistema de alerta simples detecta padrões de ataque de força bruta.

Apresentação Final (Equipe Completa - Integração):

Foco: O Sistema Coeso.

Demonstração: A equipe executa o orquestrador main.py.

Fluxo Completo:

O main.py pede o [1] Tentar Acesso.

Aluno 1: Um membro da equipe digita um ID e senha válidos. O Módulo 1 autentica (log visível no console).

Aluno 2: O Módulo 2 recebe o ID, verifica as regras e (assumindo estar no horário) concede o acesso.

Aluno 3: O Módulo 3 imediatamente imprime o log de "Acesso Concedido" no console.

A equipe repete o processo 3x com uma senha errada.

Aluno 3: Na terceira falha, o Módulo 3 dispara o "ALERTA DE SEGURANÇA" em tempo real.

Finalmente, a equipe seleciona [2] Ver Dashboard e o Aluno 3 explica o histórico completo de acessos que acabou de ocorrer.

6. Conclusão
O projeto SCAI é um exemplo prático de engenharia de software eficaz. Ele não apenas entrega uma ferramenta de segurança funcional (em nível de protótipo), mas, mais importante, valida uma arquitetura de desenvolvimento que mitiga riscos de colaboração. Ao definir "contratos" (interfaces) claros entre os módulos, cada aluno pôde desenvolver e testar sua parte do sistema de forma independente, garantindo que a integração final fosse suave e sem complicações.

você poderia fazer a documentação do projeto?

Claro. Aqui está uma documentação técnica completa para o projeto, formatada como um arquivo README.md ou um documento oficial.

Este documento detalha a arquitetura, funcionalidades e guias de uso do Sistema de Controle de Acesso Inteligente (SCAI).

Documentação do Projeto: Sistema de Controle de Acesso Inteligente (SCAI)
1. Visão Geral
O Sistema de Controle de Acesso Inteligente (SCAI) é um protótipo de software que simula um sistema de segurança moderno para gerenciamento de acesso físico. O projeto foi desenvolvido sobre uma arquitetura modular de três componentes principais, permitindo o desenvolvimento paralelo, testes isolados e integração simplificada.

Os três pilares do sistema são:

Autenticação: Validação da identidade do usuário (login e senha).

Autorização: Verificação de permissões de acesso com base em regras de negócio (ex: horário, local).

Auditoria: Registro (log) de todas as tentativas de acesso e geração de alertas para atividades suspeitas.

2. Funcionalidades Principais
Autenticação de Usuário: O sistema valida usuários com base em um ID e senha armazenados de forma persistente.

Controle de Acesso Baseado em Regras (RBAC): O sistema concede ou nega acesso não apenas com base na identidade, mas também em regras de horário e local.

Registro e Auditoria (Logging): Todas as tentativas de acesso, bem-sucedidas ou falhas, são registradas em um arquivo de log imutável (acessos.log) com data e hora.

Detecção de Intrusão (Alerta): O sistema monitora falhas de login consecutivas do mesmo usuário e dispara um alerta de segurança (simulando um ataque de força bruta).

Dashboard de Monitoramento: Uma visualização de console que exibe todo o histórico de logs de acesso.

Arquitetura Modular: O código é desacoplado em três módulos que podem ser testados e desenvolvidos independentemente.

3. Arquitetura do Sistema
O SCAI é composto por 3 módulos de software principais e um orquestrador (main.py) que gerencia o fluxo de dados entre eles.

Fluxo de Dados
O fluxo de uma tentativa de acesso padrão é o seguinte:

[Usuário] → [main.py] → (1. Autenticação) → [Módulo 1] → (2. Autorização) → [Módulo 2] → (3. Auditoria) → [Módulo 3]

O main.py coleta as credenciais e as envia ao Módulo 1.

O Módulo 1 valida as credenciais. Se forem válidas, ele informa o id_usuario ao Módulo 2.

O Módulo 2 verifica as regras de negócio (horário/local). Ele toma a decisão (Concedido/Negado).

O Módulo 2 envia o resultado da decisão (o "evento") para o Módulo 3 para registro.

O Módulo 3 escreve o evento no acessos.log e verifica se um alerta deve ser disparado.

Detalhamento dos Módulos
Módulo 1: Autenticação e Gestão de Identidade
Arquivo: modulo_1_auth.py

Banco de Dados: usuarios.json

Responsabilidade: "O Porteiro". Responde à pergunta: "Este usuário é quem diz ser?".

Função Principal: autenticar(id_usuario, senha)

Módulo 2: Lógica de Acesso e Permissões
Arquivo: modulo_2_logica.py

Banco de Dados: regras.json

Responsabilidade: "O Cérebro". Responde à pergunta: "Este usuário pode entrar agora?".

Função Principal: verificar_permissao(id_usuario)

Módulo 3: Monitoramento, Logs e Alertas
Arquivo: modulo_3_logs.py

Banco de Dados: acessos.log (gerado automaticamente)

Responsabilidade: "O Vigilante". Responde à pergunta: "O que aconteceu e isso é suspeito?".

Função Principal: registrar_log(evento)

4. Tecnologias Utilizadas
Linguagem de Programação: Python 3.x

Bibliotecas Padrão (Built-in):

json: Utilizada para serializar e desserializar os "bancos de dados" (usuarios.json, regras.json).

datetime: Utilizada pelo Módulo 2 para verificar as regras de horário.

Formato de Dados:

JSON: Para persistência de dados estruturados (usuários e regras).

.log (Texto Plano): Para o registro de auditoria.

5. Estrutura de Arquivos
projeto_seguranca/
│
├── usuarios.json        # Banco de dados de usuários e senhas (Módulo 1)
├── regras.json          # Banco de dados de permissões e horários (Módulo 2)
├── acessos.log          # Arquivo de log gerado automaticamente (Módulo 3)
│
├── modulo_1_auth.py     # Código do Módulo 1: Autenticação
├── modulo_2_logica.py   # Código do Módulo 2: Lógica de Regras
├── modulo_3_logs.py     # Código do Módulo 3: Logs e Alertas
│
└── main.py              # Orquestrador principal para integração e apresentação
6. Instalação e Configuração
Pré-requisitos
Python 3.6 ou superior.

Instalação
Nenhuma instalação de biblioteca externa (via pip) é necessária, pois o projeto utiliza apenas bibliotecas padrão do Python.

Clone ou baixe os arquivos .py para um diretório local.

Crie o arquivo usuarios.json no mesmo diretório com o seguinte conteúdo:

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
Crie o arquivo regras.json no mesmo diretório com o seguinte conteúdo:

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
7. Como Executar
O projeto pode ser executado de duas formas: testes individuais de módulo ou o sistema integrado.

7.1. Teste de Módulos (Execução Individual)
Cada módulo contém um bloco if __name__ == "__main__": que permite testá-lo isoladamente.

Bash
# Para testar o Módulo de Autenticação
python modulo_1_auth.py

# Para testar o Módulo de Lógica de Acesso
python modulo_2_logica.py

# Para testar o Módulo de Logs e Alertas
python modulo_3_logs.py
7.2. Execução do Sistema Integrado (Apresentação Final)
Para rodar o projeto completo, execute o arquivo main.py.

Bash
python main.py
Ao executar, um menu de console será apresentado:

=================================================
SISTEMA DE CONTROLE DE ACESSO INTELIGENTE (v1.0)
[1] Tentar Acesso
[2] Ver Dashboard de Logs
[3] Sair
Digite sua opção:
Opção 1: Inicia o fluxo completo de tentativa de acesso (M1 → M2 → M3).

Opção 2: Exibe o conteúdo do arquivo acessos.log (Função do Módulo 3).

Opção 3: Encerra o programa.

8. API Interna (Interfaces dos Módulos)
A comunicação entre os módulos é feita por chamadas de função diretas (importações).

modulo_1_auth.py
Função: autenticar(id_usuario: str, senha: str) -> bool

Descrição: Verifica se a combinação de id_usuario e senha existe no usuarios.json.

Retorno: True se for válido, False caso contrário.

modulo_2_logica.py
Função: verificar_permissao(id_usuario: str) -> (bool, str)

Descrição: Verifica as regras de acesso (existência, horário) para o id_usuario fornecido.

Retorno: Uma tupla (status, mensagem). Ex: (True, "Acesso Concedido") ou (False, "Acesso Negado: Fora do horário").

Efeito Colateral: Chama modulo_3_logs.registrar_log() com o resultado da verificação.

modulo_3_logs.py
Função: registrar_log(evento: dict)

Descrição: Recebe um dicionário evento contendo os detalhes da tentativa de acesso e o escreve no acessos.log.

Formato do Evento: {"id_usuario": str, "status": bool, "mensagem": str}

Efeito Colateral: Chama verificar_alertas().

Função: exibir_dashboard_logs()

Descrição: Lê o arquivo acessos.log e imprime seu conteúdo no console.

9. Autores e Divisão de Tarefas
O projeto foi dividido para permitir o desenvolvimento paralelo, com as seguintes responsabilidades:

Aluno 1 (Nome do Aluno):

Módulo: Módulo 1: Autenticação e Gestão de Identidade

Componentes: modulo_1_auth.py, usuarios.json

Aluno 2 (Nome do Aluno):

Módulo: Módulo 2: Lógica de Acesso e Permissões

Componentes: modulo_2_logica.py, regras.json

Aluno 3 (Nome do Aluno):

Módulo: Módulo 3: Monitoramento, Logs e Alertas

Componentes: modulo_3_logs.py, acessos.log (definição)

