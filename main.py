import csv
import unicodedata
from gerador_certificado import GeradorCertificado


# ----------------- Dicionário com título da atividade e a quantidade de horas 
# ----------------- Editar conforme as atividades requeridas
# ----------------- É necessário remover as vírgulas dos nomes das atividades nos arquivos .csv 
# ----------------- O nome da atividade aqui deve ser idêntico ao nome da atividade nos arquivos .csv 

palestras = {
    # Segunda
    'Abertura SECCOM': 1,
    'Palestra - Prevendo o desempenho de Alunos de Cursos Online com Deep Learning e Processamento de Linguagem Natural (Armindo Guerra)': 1,
    'Painel - Perspectivas em IA (profs. Jerusa Marchi Mauro Roisenberg Jonata Tyska)': 2,
    'Hackaton de Segurança': 4.5,
    'Minicurso -  Introdução à Unity Game Engine': 3,
    
    # Terça
    'Palestra - Dados (semi não ...) estruturados: problemas e solução (#sqn) (Profa. Carina Dorneles)': 1,
    'Palestra - Quem você pensa que é? Chris Bumstead CBum? Eu acho que não. Porque a pós-graduação precisa estar no seu radar de formação acadêmica (Profa. Patricia Plentz)': 1,
    'Palestra - Tecnologia FPGA Intel no Mercado Brasileiro (Franciele Nornberg) - Macnica DHW': 1,
    'Palestra - Perspectivas no uso de dados para Agricultura (Luiz Santana) - Leaf Agriculture': 1,
    'Minicurso - Linux: comandos básicos (André Régis)': 3,
    'Minicurso - Programação Linear Inteira (Profs. Álvaro Franco e Rafael de Santiago)': 1.5,

    # Quarta
    'Minicurso - Desenvolvendo um aplicativo mobile com Flutter (Cainã Rinaldi Esteche)': 4,
    'Palestra - Chips: Pilares da Era da Informação (prof. José Luís Güntzel)': 1.5,
    'Maratona de Programação': 2.5,
    'Roda de conversa sobre Computação & IA (PET Computação)': 1.5,
    
    # Quinta
    'Palestra - Introdução a programação de computadores quânticos - (Msc. Evandro Chagas da Rosa)': 1,
    'Progressos e expectativas da computação quântica - Prof. Renato Portugal pesquisador Titular do LNCC/MCTI': 1,
    'Minicurso - Introdução a geração de imagens com IA Gerativa (Prof. Aldo von Wangenheim/Thiago Luz)': 4,
    'Palestra - Persistência Poliglota de Dados: Fundamentos e Oportunidades de Pesquisa  (Prof. Ronaldo Mello)': 1.5,
    'Minicurso - Editor de Texto VIM (André Régis)': 3,
    'Palestra - A IA no Desenvolvimento de Software no Mercado Livre  (Milton Bittencourt) -  Mercado Livre': 1.5,

    # Sexta
    'Palestra - Do Zero ao Hack: Hackeando Jogos de PS1 (Mateus Favarin Costa)': 1,
    'Palestra - Microeletrônica é computação? Sim!!  (Profa. Cristina Meinhardt)': 1,
}


def remover_acentos(texto):
    # Normaliza a string para a forma 'NFD' e remove os caracteres de combinação
    return ''.join(
        char for char in unicodedata.normalize('NFD', texto)
        if unicodedata.category(char) != 'Mn'
    )


def encontrar_strings(string_grande, lista_strings_menores):
    # Filtra as strings menores encontradas na string grande
    strings_encontradas = [substring for substring in lista_strings_menores if substring in string_grande]

    return strings_encontradas


def get_validos():
    validos = {}
    with open('info.csv', 'r') as arquivo:
        reader = csv.reader(arquivo)
        
        for i, linha in enumerate(reader):
            email = linha[1]
            nome = linha[2]
            matricula = linha[3]
            cpf = linha[6].replace('.', '').replace('-', '')[:11]
            # print(f'{nome:<50} | {matricula:10} | {cpf}')

            if len(cpf) == 11 and matricula != '':
                validos[matricula] = {
                    'email': remover_acentos(email),
                    'nome': remover_acentos(nome),
                    'matricula': matricula,
                    'cpf': cpf,
                    'palestras': [],
                    'horas': 0
                }
            
    return validos


validos = get_validos()


for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
    with open(f'{dia}.csv', 'r') as arquivo:
        reader = csv.reader(arquivo)
        for i, linha in enumerate(reader):
            if i == 0:
                continue
            
            matricula = linha[2]
            string_grande = linha[3]
            lista_strings_menores = list(palestras.keys())


            if matricula in validos.keys():
                validos[matricula]['palestras'] += encontrar_strings(string_grande, lista_strings_menores)
    

chaves_a_remover = []

for participante in validos:
    total_horas = 0
    for palestra in validos[participante]['palestras']:
        total_horas += palestras[palestra]
    
    # print(validos[participante]['palestras'])
    validos[participante]['horas'] = total_horas

    if validos[participante]['horas'] == 0:
        chaves_a_remover.append(participante)


for ausente in chaves_a_remover:
    del validos[ausente]


# Classe que gera e envia os certificados por email
for participante in validos:
    GeradorCertificado.enviar_email_com_certificado(validos[participante]['nome'], validos[participante]['cpf'], validos[participante]['horas'], validos[participante]['email'])