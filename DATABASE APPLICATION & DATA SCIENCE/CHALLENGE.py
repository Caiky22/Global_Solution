print('Cadastro inicial\n')

doador = []
solicitante = []

while True:
    cadastro = str(input('Deseja se cadastrar?')).lower()
    if cadastro == 'sim':
        print('\nDigite 1 para: Doador')
        print('Digite 2 para: Solicitante')
        tipo_cadastro = str(input('\nQual o seu tipo de cadastro? '))
        if tipo_cadastro == '1':
            cadastro_doador = {
                'nome': str(input('Nome completo: ')),
                'CPF': int(input('CPF: ')),
                'Estado': str(input('UF do doador: ')),
                'Municipio': str(input('Municipio do doador: ')),
                'Endereco': str(input('Endereco do doador: ')),
                'Telefone': int(input('Telefone para contato: '))
            }
            print('\n-------------------')
            print('Cadastro finalizado')
            print('-------------------')
            doador.append(cadastro_doador)
            for chave, valor in cadastro_doador.items():
                print(f'\n{chave} : {valor}')
        elif tipo_cadastro == '2':
            cadastro_solicitante = {
                'nome': str(input('Nome da ONG ou Solicitante: ')),
                'CNPJ': str(input('CNPJ da organizacao: ')),
                'Estado': str(input('UF do solicitante: ')),
                'Municipio': str(input('Municipio do solicitante: ')),
                'Telefone': int(input('Telefone para contato: '))
            }
            print('\n-------------------')
            print('Cadastro finalizado')
            print('-------------------')
            solicitante.append(cadastro_solicitante)
            for chave, valor in cadastro_solicitante.items():
                print(f'\n{chave} : {valor}')
        else:
            print('Cadastro feito')
    else:
        print('Sem cadastro')
        break
