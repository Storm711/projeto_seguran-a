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
