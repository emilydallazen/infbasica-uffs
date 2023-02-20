def resumo():
    mensagem = "Claude Elwood  Shannon (30 de abril de 1916 — 24 de fevereiro de 2001) foi um matemático, engenheiro eletrônico e criptógrafo estadunidense, conhecido como o pai da teoria da informação."
    return mensagem


def doutorado():
    mensagem = "Claude Shannon nasceu nos USA em 1916. Formou-se em Matemática e Engenharia Elétrica na Universidade de Michigan, e fez seu mestrado e doutorado no MIT."
    return mensagem


def contribuicoes():
    mensagem = "Shannon propôs pela primeira vez numa tese em 1937 o uso da lógica booleana - mostrando como circuitos podem efetuar operações lógicas - e em 1948 publicou sua Teoria da Informação, que busca otimizar as linhas de comunicação - ao transmitir a informação da maneira mais eficiente e minimizar as distorções existentes. Ele mostrou que toda informação numérica pode ser reduzida numa medida elementar, designada pelo termo bit. Outras contribuições foram a entropia, uma medida do grau de incerteza existente num canal de informação. Ela indica a informação mínima que deve ser mantida para transmitir dados sem perda (por exemplo, no caso de compressão de dados). E além disso, conceituou a Medição da taxa máxima de transmissão, que avalia a quantidade de informação máxima que pode ser transmitida sem perdas dentro de uma determinada largura de banda na presença de ruído."
    return mensagem


def artigos():
    mensagem = "Principais artigos publicados por Claude Shannon:\nA Mathematical Theory of Communication \nPrevisão e Entropia de Impresso Inglês \nCommunication Theory of Secrecy Systems."
    return mensagem


def citacoes():
    mensagem = "Citações famosas de Claude Shannon: \n „Thus we may have knowledge of the past but cannot control it; we may control the future but have no knowledge of it.“ \n „A few first rate research papers are preferable to a large number that are poorly conceived or half-finished. The latter are no credit to their writers and a waste of time to their readers.“"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Claude Shannon.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
            """
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
