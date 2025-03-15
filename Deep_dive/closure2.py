# Configurador de notificações personalizadas

def criar_notificacao(tipo_evento):
    def enviar_mensagem(email):
        print(f"Enviando e-mail sobre {tipo_evento} para {email}")
    return enviar_mensagem

# Criando funções específicas para cada tipo de evento
notificacao_pagamento = criar_notificacao("Pagamento Confirmado")
notificacao_entrega = criar_notificacao("Entrega Realizada")

# Usando as funções
notificacao_pagamento("cliente@tiago.com")
print()
notificacao_entrega("cliente@samora.com")