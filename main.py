import gerador_certificado
import json

# ----------------- Dicionário com título da atividade e a quantidade de horas
# ----------------- Editar conforme as atividades requeridas
# ----------------- É necessário remover as vírgulas dos nomes das atividades nos arquivos .csv
# ----------------- O nome da atividade aqui deve ser idêntico ao nome da atividade nos arquivos .csv

with open('validos.json', 'r') as json_file:
    validos = json.load(json_file)

# Classe que gera e envia os certificados por email
for participante in validos:
    gerador_certificado.enviar_email_com_certificado(
        validos[participante]['nome'], validos[participante]['cpf'], validos[participante]['horas'], validos[participante]['email'])
