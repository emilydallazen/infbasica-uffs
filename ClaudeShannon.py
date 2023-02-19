def resumo():
    mensagem = " Claude Elwood Shannon (1916-2001) foi um matemático e engenheiro elétrico norte-americano que é considerado o pai da teoria da informação. Ele desenvolveu um conjunto de teorias e técnicas que formaram a base da comunicação de dados moderna, incluindo a codificação de canal, a compressão de dados e a teoria da criptografia. \n Shannon começou a trabalhar na teoria da informação na década de 1940, enquanto trabalhava na Bell Labs. Ele publicou um artigo seminal em 1948, intitulado `A Mathematical Theory of Communication`, que estabeleceu a teoria da informação como um campo de estudo. Neste artigo, Shannon introduziu o conceito de entropia como medida da quantidade de informação em uma mensagem. \n Além de suas contribuições à teoria da informação, Shannon também fez importantes avanços em outras áreas da matemática e engenharia, incluindo a teoria dos circuitos booleanos, a criptografia e a codificação de fonte. \n Shannon recebeu muitas honras ao longo de sua carreira, incluindo a Medalha Nacional de Ciência em 1966 e o Prêmio Kyoto em Tecnologia Avançada em 1985. Sua influência na ciência da computação e nas telecomunicações ainda é sentida hoje, e sua obra continua a inspirar e informar a pesquisa em comunicação de dados e teoria da informação."
    return mensagem


def doutorado():
    mensagem = "O doutorado de Claude Elwood Shannon, concluído em 1940, foi intitulado \"Uma Análise Simbólica das Máquinas de Comutação\" e foi fundamental para a teoria da lógica digital e da computação moderna. A tese de Shannon mostrou que os circuitos elétricos podiam ser analisados utilizando técnicas de lógica simbólica e álgebra booleana, permitindo que circuitos complexos fossem simplificados e projetados com mais eficiência. Shannon também propôs o conceito de chaveamento binário, que foi essencial para a criação de sistemas digitais e abriu o caminho para o desenvolvimento de computadores modernos."
    return mensagem


def contribuicoes():
    mensagem = "Shannon propôs pela primeira vez numa tese em 1937 o uso da lógica booleana - mostrando como circuitos podem efetuar operações lógicas - e em 1948 publicou sua Teoria da Informação, que busca otimizar as linhas de comunicação - ao transmitir a informação da maneira mais eficiente e minimizar as distorções existentes. Ele mostrou que toda informação numérica pode ser reduzida numa medida elementar, designada pelo termo bit. Outras contribuições foram a entropia, uma medida do grau de incerteza existente num canal de informação. Ela indica a informação mínima que deve ser mantida para transmitir dados sem perda (por exemplo, no caso de compressão de dados). E além disso, conceituou a Medição da taxa máxima de transmissão, que avalia a quantidade de informação máxima que pode ser transmitida sem perdas dentro de uma determinada largura de banda na presença de ruído."
    return mensagem


def artigos():
    mensagem = "Claude Elwood Shannon publicou vários artigos importantes em sua carreira, incluindo: \n\n`A Symbolic Analysis of Relay and Switching Circuits` (1938) - Este artigo introduziu a ideia de usar álgebra booleana para analisar circuitos elétricos e estabeleceu as bases para o projeto de circuitos digitais modernos. \n`A Mathematical Theory of Communication` (1948) - Este artigo é considerado um marco na teoria da informação, estabelecendo a noção de entropia como uma medida da informação contida em uma mensagem e lançando as bases para a teoria da compressão de dados e a codificação de canal. \n `Prediction and Entropy of Printed English` (1951) - Este artigo aplica os princípios da teoria da informação à linguagem escrita, fornecendo uma análise quantitativa da estrutura do inglês escrito. \n`Communication Theory of Secrecy Systems` (1949) - Neste artigo, Shannon estabeleceu os fundamentos da criptografia moderna, apresentando o conceito de teoria da informação aplicada à segurança de sistemas de comunicação. \n`The Bandwagon` (1955) - Este artigo é um exemplo de trabalho de Shannon em teoria de jogos, onde ele discute a ideia de seguir a multidão em tomadas de decisão. \n\nAlém desses, Shannon publicou muitos outros artigos em uma variedade de tópicos, incluindo redes de comutação, aprendizado de máquina e computação quântica."
    return mensagem


def citacoes():
    mensagem = "Claude Elwood Shannon é conhecido por suas contribuições fundamentais em diversos campos, e algumas de suas citações mais famosas incluem:\n\n\"A informação é a resolução da incerteza.\" - Esta é uma das definições mais famosas de Shannon de informação, que estabelece que a informação é uma medida da redução da incerteza.\n\"A teoria da informação é a lógica do possível em comunicação.\" - Shannon descreveu a teoria da informação como a lógica subjacente à comunicação, e ela é amplamente utilizada em engenharia de comunicações.\n\"A matemática é a ferramenta de todas as ciências.\" - Shannon reconheceu a importância da matemática em todas as áreas da ciência e acreditava que era uma ferramenta essencial para avançar o conhecimento."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Claude Elwood Shannon.\n")

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
