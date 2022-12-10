def get_type_request(response: dict):
    tipo = [i['type']['name'].capitalize() for i in response]
    return tipo

def get_abilities_request(response: dict):
    habilidades = [i['ability']['name'].capitalize() for i in response]
    return habilidades

def get_weight_request(response: dict):
    peso = [response]
    return peso

def get_stats_request(response: dict):
    estadisticas = [f"{i['stat']['name'].capitalize()} = {i['base_stat']}" for i in response]
    return estadisticas