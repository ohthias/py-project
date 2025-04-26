import json
with open('./data.json','r', encoding='utf-8') as file:
    data = json.load(file)

def get_data_by_name(name):
    for i in range(len(data)):
        if data[i]['name'] == name:
            return data[i]
    return None

nomeUsuario = input("Digite o nome do usuário: ")
if get_data_by_name(nomeUsuario) is not None:
    print("Usuário encontrado:", get_data_by_name(nomeUsuario))
else:
    print("Usuário não encontrado.")
