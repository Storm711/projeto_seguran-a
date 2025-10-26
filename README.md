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
