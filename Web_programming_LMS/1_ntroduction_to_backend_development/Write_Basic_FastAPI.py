import math
def cvss_base_score(V: str):
    metrics_map = {
        "AV": {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2},
        "AC": {"L": 0.77, "H": 0.44},
        "PR": {
            "N": 0.85,
            "L": {"U": 0.62, "C": 0.68},  
            "H": {"U": 0.27, "C": 0.5}
        },
        "UI": {"N": 0.85, "R": 0.62},
        "S": {"U": 1, "C": 1.08},
        "C": {"N": 0, "L": 0.22, "H": 0.56},
        "I": {"N": 0, "L": 0.22, "H": 0.56},
        "A": {"N": 0, "L": 0.22, "H": 0.56},
        "E": {"ND": 1, "H": 1, "F": 0.97, "P": 0.94, "U": 0.91},
        "RL": {"ND": 1, "U": 1, "W": 0.97, "T": 0.96, "O": 0.95},
        "RC": {"ND": 1, "C": 1, "R": 0.96, "U": 0.92},
        "CR": {"ND": 1, "H": 1.5, "M": 1, "L": 0.5},
        "IR": {"ND": 1, "H": 1.5, "M": 1, "L": 0.5},
        "AR": {"ND": 1, "H": 1.5, "M": 1, "L": 0.5}
    }
    params = V.split('/')[1:]
    scope_change = False
    cvss_values = {}
    for param in params:
        key, value = param.split(':')
        cvss_values[key] = metrics_map[key][value]
        if(key == "S" and value == "C"):
            scope_change = True
    ISCBase = 1 - (1 - cvss_values["C"]) * (1 - cvss_values["I"]) * (1 - cvss_values["A"])
    if (scope_change == True):
        impact = 7.52*(ISCBase - 0.029) - 3.25 * (ISCBase - 0.02)**15
        if(isinstance(cvss_values["PR"], dict)):
            cvss_values["PR"] = cvss_values["PR"]["C"]
    else:
        impact = 6.42*ISCBase
        if(isinstance(cvss_values["PR"], dict)):
            cvss_values["PR"] = cvss_values["PR"]["U"]

    exploitability = 8.22 * cvss_values["AV"] * cvss_values["AC"] * cvss_values["PR"] * cvss_values["UI"]
    if impact > 0:
        if cvss_values["S"] == 1: 
            base_score = math.ceil(min(impact + exploitability, 10)*10)/10
        else: 
            base_score = math.ceil(min(1.08 * (impact + exploitability), 10)*10)/10
    else:
        base_score = 0
    return base_score
