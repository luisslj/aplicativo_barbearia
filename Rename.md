aplicativo de barbearia 

com funçoes de agendaento do clinte 
agendamento com o barbeiro marcando o horario 
clinte pode ver so os seus agendamentos 
barbeiro pode ver o seu e dos clientes e de todos os barbeior da narnearia 


💈 Funcionalidades do Aplicativo de Barbearia
🧔 Para o Cliente
- Cadastro e Login
- O cliente cria uma conta com nome, telefone e senha.
- Pode acessar o app para visualizar barbeiros disponíveis e seus horários.
- Agendar Corte
- Escolhe o barbeiro desejado.
- Seleciona data e horário disponíveis (o sistema bloqueia automaticamente horários indisponíveis).
- Confirma o agendamento e recebe uma notificação de sucesso.
- Visualizar Meus Agendamentos
- Lista todos os cortes marcados, com data, hora e nome do barbeiro.
- Permite cancelar ou reagendar se o barbeiro liberar essa opção.
- Notificações
- Recebe alertas de confirmação, lembretes de horário e avisos de cancelamento.

💇‍♂️ Para o Barbeiro
- Login e Perfil Profissional
- O barbeiro acessa sua conta com credenciais próprias.
- Pode editar informações como nome, especialidades e horários de trabalho.
- Agenda do Barbeiro
- Visualiza todos os agendamentos feitos pelos clientes.
- Pode adicionar manualmente novos horários ou clientes.
- Bloquear Horários ou Dias
- Escolhe datas ou intervalos de tempo para folgas, compromissos ou manutenção.
- Define o motivo do bloqueio (ex: “folga”, “reunião”, “viagem”).
- O sistema impede que clientes agendem nesses períodos.
- Gerenciar Bloqueios
- Lista todos os horários bloqueados.
- Permite desbloquear dias ou horários quando desejar.
- Controle de Agendamentos
- Pode reagendar, marcar como concluído ou cancelar cortes.
- Visualiza histórico de clientes atendidos.

⚙️ Funcionalidades Gerais
- Verificação automática de disponibilidade: o sistema cruza os bloqueios do barbeiro com os horários solicitados pelo cliente.
- Interface intuitiva: design escuro com detalhes dourados, transmitindo elegância e profissionalismo.
- Sincronização em tempo real: qualquer alteração feita pelo barbeiro reflete imediatamente na tela do cliente.
- Segurança e autenticação: cada usuário (cliente ou barbeiro) tem permissões específicas.


⚙️ Lógica de Funcionamento
- Login e autenticação
- O sistema identifica se o usuário é cliente ou barbeiro.
- Redireciona para o painel correspondente.
- Agendamento
- O cliente escolhe barbeiro, data e hora.
- O sistema verifica na tabela bloqueios se o horário está livre.
- Se estiver disponível, cria o registro em agendamentos.
- Bloqueio de horários
- O barbeiro define um intervalo de tempo e motivo.
- O sistema insere o registro em bloqueios.
- Durante o agendamento, ess- Durante o agendamento, esses horários são ocultados para clientes.
- Gerenciamento
- O barbeiro pode visualizar todos os agendamentos e bloqueios.
- Pode desbloquear horários ou reagendar cortes.
- O cliente pode cancelar ou reagendar seus próprios horários.
- Notificações
- Envio automático de confirmação, lembrete e cancelamento via e-mail ou pu


🔐 Segurança e Boas Práticas
- Criptografia de senhas com bcrypt.
- Validação de horários para evitar sobreposição.
- Controle de acesso com sessões separadas para cliente e barbeiro.
- Logs de atividade para auditoria.

