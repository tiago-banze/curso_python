lista_tarefa = []
lista_apagada = []

while True:
    print('comandos: 0-sair, 1-listar, 2-desfazer, 3-refazer')
    entrada = input('inserir tarefa uma tarefa ou comando: ').lower()
    print()
    
    if entrada in ['listar','1']:
        if lista_tarefa:
            for i , tarefa in enumerate(lista_tarefa):
                print(f'**{i+1} -- {tarefa}')
             
        elif not lista_tarefa:
            print('Não existe nenhuma tarefa para listar!')
            print()

    elif entrada in ['desfazer','2']:
        print()
        if lista_tarefa:
            apagado = lista_tarefa.pop()
            lista_apagada.append(apagado)
            for i , tarefa in enumerate(lista_tarefa):
                print(f'**{i+1} -- {tarefa}')
             
        elif not lista_tarefa:
            print('Não existe nenhuma tarefa para desfazer!')
            print()
                
    elif entrada in ['refazer', '3']:
        if lista_apagada:
            apagado = lista_apagada.pop()
            lista_tarefa.append(apagado)
            for i , tarefa in enumerate(lista_tarefa):
                print(f'**{i+1} -- {tarefa}')
             
        elif not lista_apagada:
           print('Não existe nenhuma tarefa para refazer!')
           print() 
    
    elif entrada in ['0','sair']:
        print('Saindo...')
        break
    
    else:
        lista_tarefa.append(entrada)
        for i , tarefa in enumerate(lista_tarefa):
            print(f'**{i+1} -- {tarefa}') 