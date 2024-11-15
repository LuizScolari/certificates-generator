import csv
import json
import os

def csv_to_json(csv_file_path, json_file_name='validos.json', horas_fixas=30):
    # Extrai o diretório do arquivo CSV
    base_dir = os.path.dirname(csv_file_path)
    # Constrói o caminho completo para o arquivo JSON
    json_file_path = os.path.join(base_dir, json_file_name)

    # Dicionário para armazenar os dados
    data_dict = {}

    # Abrindo o arquivo CSV para leitura
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            matricula = row['matricula']
            data_dict[matricula] = {
                "nome": row['nome'],
                "matricula": matricula,
                "cpf": row['cpf'],
                "horas": horas_fixas
            }

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data_dict, json_file, indent=4, ensure_ascii=False)

# Caminho do arquivo .csv
csv_file = 'dados.csv' 

csv_to_json(csv_file)