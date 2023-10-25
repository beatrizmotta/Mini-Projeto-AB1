from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Qual o Animal?'))

instructions = """
Por: Frederico Guilherme, Lara Vitória e Maria Beatriz 
=> O programa tem como objetivo tentar determinar em que animal o usuário está pensando baseado em suas respostas.
=> Para cada pergunta o usuário deve responder com s (sim) ou n (não)

Pressione ENTER para continuar
"""

print(instructions)
input()


possible_animals = ["leopardo", "girafa", "zebra", "avestruz",
                    "pinguim", "albatroz", "galinha", "flamingo", "morcego"]

tree = {
    "é_mamífero": {
        "AND": {
            "tem_pelo": True,
            "dá_leite": True,
        }
    },
    "é_ave": {
        "OR": [
            {"tem_penas": True},
            {
                "AND": {
                    "voa": True,
                    "bota_ovos": True,
                }
            }
        ]
    },
    "é_carnívoro": {
        "OR": [
            {
                "AND": {
                    "é_mamífero": True,
                    "come_carne": True,
                }
            },
            {
                "AND": {
                    "é_mamífero": True,
                    "tem_dentes_pontiagudos": True,
                    "tem_garras": True,
                    "tem_olhos_frontais": True
                }
            }
        ]
    },
    "é_ungulado": {
        "OR": [
            {
                "AND": {
                    "é_mamífero": True,
                    "tem_casco": True
                }
            },
            {
                "AND": {
                    "é_mamífero": True,
                    "rumina": True,
                    "tem_dedos_pares": True
                }
            }
        ]
    },
    "é_bom_voador": {
        "voa": True 
    },
    "tem_penas_densas": {
        "tem_penas": True
    },
    "girafa": {
        "AND": {
            "é_ungulado": True,
            "tem_pernas_longas": True,
            "tem_pescoço_comprido": True,
            "é_de_cor_amarelo_tostado": True,
            "tem_manchas_escuras": True
        }
    },
    "leopardo": {
        "AND": {
            "é_carnívoro": True,
            "é_de_cor_amarelo_tostado": True,
            "tem_manchas_escuras": True
        }
    },
    "zebra": {
        "AND": {
            "é_ungulado": True,
            "é_de_cor_branca": True,
            "tem_listras_pretas": True
        }
    },
    "avestruz": {
        "AND": {
            "é_ave": True,
            "não_voa": True,
            "tem_pernas_longas": True,
            "tem_pescoço_comprido": True,
            "é_preto_e_branco": True
        }
    },
    "pinguim": {
        "AND": {
            "é_ave": True,
            "não_voa": True,
            "nada": True,
            "é_preto_e_branco": True
        }
    },
    "albatroz": {
        "AND": {
            "é_ave": True,
            "é_bom_voador": True
        }
    },
    "galinha": {
        "AND": {
            "é_ave": True,
            "tem_corpo_arredondado": True,
            "tem_penas_densas": True,
            "não_voa": True,
            "é_doméstico": True
        }
    },
    "flamingo": {
        "AND": {
            "é_ave": True,
            "tem_pernas_longas": True,
            "tem_pescoço_comprido": True,
            "tem_cauda_curta": True,
            "é_de_cor_rosa": True
        }
    },
    "morcego": {
        "AND": {
            "é_mamífero": True,
            "voa": True,
            "não_é_ave": True
        }
    },
}

facts = {}

def isConsequent(antecedent):
    return antecedent in tree
def ask_question(antecedent):
    truth = input("O animal " + antecedent + "? (s/n)\n>>> ")
    truth = True if truth == "s" else False
    facts[antecedent] = truth

def find(node, name):
    if "AND" in node:
        antecedents = node["AND"]
        truths = []
        for antecedent in antecedents:
            if isConsequent(antecedent):
                find(tree[antecedent], antecedent)
            else:
                if (name in facts):
                    break
                if antecedent not in facts:
                    ask_question(antecedent)
                    truths.append(facts[antecedent])

        for antecedent in antecedents:
            if antecedent in facts:
                if antecedents[antecedent] == facts[antecedent]:
                    facts[name] = True

    elif "OR" in node:
        conditions = node["OR"]
        for condition in conditions:
            find(condition, name)

def why(animal):
    antecedents = tree[animal]["AND"]
    similarities = []
    reasons = []

    for antecedent in antecedents:
        if antecedent in facts:
            similarities.append(facts[antecedent] == antecedents[antecedent])
            value = "verdadeiro" if facts[antecedent] else "falso"
            reason = f"{antecedent} é {value}"
            reasons.append(reason)

    if all(similarities):
        return f"O programa acha que você está pensando em {animal} porque {', '.join(reasons)}."

for animal in possible_animals:
    antecedents = tree[animal]["AND"]
    find(tree[animal], animal)

print("Animais possíveis: ")
reduced_possible_animals = []
for animal in possible_animals:
    antecedents = tree[animal]["AND"]
    similarities = []
    for antecedent in antecedents:
        if antecedent in facts:
            similarities.append(facts[antecedent] == antecedents[antecedent])


    if len(similarities) > 0 and all(similarities):
        reduced_possible_animals.append(animal)
        
if (len(reduced_possible_animals) > 0):
    for animal in reduced_possible_animals:
        print(f"- {animal}")
        why_message = why(animal)
        if why_message:
            print(f"  Por quê? {why_message}")
else:
    print("Não consegui determinar em qual animal você está pensando!")