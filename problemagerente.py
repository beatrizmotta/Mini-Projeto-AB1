from pick import pick 
from pyfiglet import Figlet


f = Figlet(font='slant')
print(f.renderText('Problema do Gerente'))

instructions = """
Por: Frederico Guilherme, Lara Vitória e Maria Beatriz 
=> O programa irá fazer uma série de perguntas para tentar determinar o risco do cliente não pagar o empréstimo.
=> Para responder as perguntas de múltiplas escolhas:
    => Navege entra as opções com as setas do teclado
    => Aperte ENTER quando quiser escolher
=> Para responder perguntas abertas:
    => Simplesmente digite o valor

Pressione ENTER para continuar
"""

print(instructions)

input()


risks = ["alto", "moderado", "baixo"]
questions = {
    "Qual o histórico de crédito do cliente?": ["bom", "ruim", "desconhecido"],
    "Qual o tamanho da dívida?": ["alta", "baixa"],
    "Possui garantia?": ["nenhuma", "adequada"],
    "Qual a faixa de renda?": 0
}

data = {}

tree = {
    "alto": [
        {
            "historico_credito": "ruim",
            "tamanho_divida": "alta",
            "garantia": "nenhuma",
            "renda": [0, 15]
        },
        {
            "historico_credito": "desconhecido",
            "tamanho_divida": "alta",
            "garantia": "nenhuma",
            "renda": [15, 35]
        },
        {
            "historico_credito": "desconhecido",
            "tamanho_divida": "baixa",
            "garantia": "nenhuma",
            "renda": [0, 15]
        },
        {
            "historico_credito": "ruim",
            "tamanho_divida": "baixa",
            "garantia": "nenhuma",
            "renda": [0, 15]
        },
        {
            "historico_credito": "bom",
            "tamanho_divida": "alta",
            "garantia": "nenhuma",
            "renda": [0, 15]
        },
        {
            "historico_credito": "ruim",
            "tamanho_divida": "alta",
            "garantia": "nenhuma",
            "renda": [15, 35]
        }
    ],
    "moderado": [
        {
            "historico_credito": "desconhecido",
            "tamanho_divida": "baixa",
            "garantia": "nenhuma",
            "renda": [15, 35]
        },
        {
            "historico_credito": "ruim",
            "tamanho_divida": "baixa",
            "garantia": "adequada",
            "renda": [35]
        },
        {
            "historico_credito": "bom",
            "tamanho_divida": "alta",
            "garantia": "nenhuma",
            "renda": [15, 35]
        }
    ],
    "baixo": [
        {
            "historico_credito": "desconhecido",
            "tamanho_divida": "baixa",
            "garantia": "nenhuma",
            "renda": [35]
        },
        {
            "historico_credito": "desconhecido",
            "tamanho_divida": "baixa",
            "garantia": "adequada",
            "renda": [35]
        },
        {
            "historico_credito": "bom",
            "tamanho_divida": "baixa",
            "garantia": "nenhuma",
            "renda": [35]
        },
        {
            "historico_credito": "bom",
            "tamanho_divida": "alta",
            "garantia": "adequada",
            "renda": [35]
        },
        {
            "historico_credito": "bom",
            "tamanho_divida": "alta",
            "garantia": "nenhuma",
            "renda": [35]
        }
    ]
}

def getInformation(data):
    for question in questions:
        if (isinstance(questions[question], list)):
            title = question
            options = questions[question]

            option, index = pick(options, title, indicator='=>', )
        else:
            renda = float(input(question + "\n"))

        if (question == "Qual o histórico de crédito do cliente?"):
            data["historico_credito"] = option
        elif (question == "Qual o tamanho da dívida?"):
            data["tamanho_divida"] = option
        elif (question == "Possui garantia?"):
            data["garantia"] = option
        elif (question == "Qual a faixa de renda?"):
            data["renda"] = renda


def findRisk(data, tree, risks):
    for risk in risks:

        for conditions in tree[risk]:
            match = True
            for item in conditions:
                if (item == "historico_credito" or item == "tamanho_divida" or item == "garantia"):
                    
                    if (conditions[item] != data[item]):
                        match = False
                elif (item == "renda"):
                    if (len(conditions[item]) == 1):
                        if (data[item] < conditions[item][0]):
                            match = False
                    else:   
                        if (data[item] < conditions[item][0] or data[item] > conditions[item][1]):
                            match = False
            if (match):
                explanation = []
                for item in conditions:
                    explanation.append(f"- O {item} do cliente é {data[item]}")
                return [risk, explanation]
            else:
                continue
            

        






getInformation(data=data)
[risk, explanations] = findRisk(data=data, tree=tree, risks=risks)




if (risk in risks):
    print("O risco de conceder empréstimo para o cliente é " + risk)
    print("Por quê?")
    for explanation in explanations:
        print(explanation)
else:
    print("Não foi possível determinar o risco de conceder empréstimo para o cliente baseado nas informações dadas.")
