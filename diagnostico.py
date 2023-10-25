from pick import pick
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Diagnóstico'))

instructions = """
Por: Frederico Guilherme, Lara Vitória e Maria Beatriz 
=> O programa tem como objetivo determinar o diagnóstico de uma pessoa baseado em seus sintomas apresentados.
=> Para selecionar os sintomas:
    => Navege entra as opções com as setas do teclado
    => Aperte SPACE quando quiser escolher
    => Quanto tiver terminado de escolher, aperte ENTER

Pressione ENTER para continuar
"""

print(instructions)
input()


possible_diagnosis = ["dengue", "chicungunha", "gripe", "mononucleose infecciosa", "estresse", "amigdalite", "covid19",
                      "rinite alérgica", "sinusite"]

tree = {
    "gripe": {
        "AND": {
            "dor_de_cabeça": True,
            "tosse": True,
            "garganta_inflamada": True
        }
    },
    "mononucleose infecciosa": {
        "AND": {
            "cansaço": True,
            "dor_de_cabeça": True,
        }
    },
    "amigdalite": {
        "AND": {
            "cansaço": True,
            "garganta_inflamada": True,
        }
    },
    "estresse": {
        "AND": {
            "cansaço": True
        }
    },

    # Dor de garganta e tosse apenas possuem Ocasionalmente
    "covid19": {
        "AND": {
            "fadiga": True,
            "dor_de_cabeça": True,
            "dor_no_corpo": True,
            "dor_de_garganta_ocasional": True,
            "tosse_ocasional": True
        }
    },
    "rinite alérgica": {
        "AND": {
            "coriza": True,
            "espirro": True
        }
    },
    "sinusite": {
        "AND": {
            "coriza": True,
            "dor_de_cabeça": True
        }
    },
    "dengue": {
        "AND": {
            "manchas_vermelhas": True,
            "febre": True,
            "dor_no_corpo": True
        }
    },
    "chicungunha": {
        "AND": {
            "febre": True,
            "dor_no_corpo": True,
            "dor_de_cabeça": True
        }
    }
}

def isConsequent(antecedent):
    return antecedent in tree






title = "Selecione os sintomas: "
options = ["cansaço", "coriza", "dor_de_cabeça", "dor_de_garganta",
           "dor_de_garganta_ocasional", "dor_no_corpo", "espirro", "fadiga", "febre", "garganta_inflamada",
           "manchas_vermelhas", "tosse", "tosse_ocasional", "encerrar"]
selected_symptoms = pick(options, title, multiselect=True, min_selection_count=1)
for i in range(0, len(selected_symptoms)):
    selected_symptoms[i] = selected_symptoms[i][0]

# Should search for the diagnosis that match with the symptoms
def find_diagnosis(confirmed_symptons):
    diagnosis_total_match = None
    diagnosis_partial_match = []

    # Se os sintomas são exatamente iguais a lista de sintomas da doença, então é um match total
    for diagnosis in possible_diagnosis:
        diagnosis_symptoms = list(tree[diagnosis]["AND"].keys())
        
        if (set(confirmed_symptons) == set(diagnosis_symptoms)):
            diagnosis_total_match = diagnosis
            return diagnosis_total_match
    
    # Se os sintomas existem em uma lista de sintomas da doença, então é um match parcial
    for diagnosis in possible_diagnosis:
        diagnosis_symptoms = list(tree[diagnosis]["AND"].keys())
        
        if (set(confirmed_symptons).issubset(set(diagnosis_symptoms))):
            diagnosis_partial_match.append(diagnosis)
    
    return diagnosis_partial_match

def why(diagnosis, symptoms):
    antecedents = tree[diagnosis]["AND"]
    reasons = []

    for symptom in symptoms:
        if symptom in antecedents.keys():
            reason = f"{symptom} é um sintoma de {diagnosis}"
            reasons.append(reason)

    explanation = f"O programa mostrou {diagnosis} porque {', '.join(reasons)}."
    return explanation


    
results = find_diagnosis(selected_symptoms)

if isinstance(results, list):
    if len(results) > 0:
        print("Diagnósticos possíveis para os sintomas selecionados:")
        for diagnostic in results:
            print(f"- {diagnostic}")
            why_message = why(diagnostic, selected_symptoms)
            if why_message:
                print(f">>> Por quê? {why_message}")
        exit(0)
    print("Não foi possível encontrar um diagnóstico conclusivo para os sintomas selecionados.")
else:
    print(f"O diagnóstico para os sintomas selecionados é:\n - {results}")
    why_message = why(results, selected_symptoms)
    if why_message:
        print(f">>> Por quê? {why_message}")