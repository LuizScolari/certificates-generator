import csv
import unicodedata
import gerador_certificado
# ----------------- Dicionário com título da atividade e a quantidade de horas
# ----------------- Editar conforme as atividades requeridas
# ----------------- É necessário remover as vírgulas dos nomes das atividades nos arquivos .csv
# ----------------- O nome da atividade aqui deve ser idêntico ao nome da atividade nos arquivos .csv
palestras = {
    # Segunda
    'Palestra - Geração aleatória de objetos combinatórios para algoritmos criptográficos (Gustavo Zambonin)': 1,
    'Palestra - Desafios do gerenciamento de identidade digital pelo usuário: Do uso inadequado de senhas à identidade digital descentralizada (Shirlei Chaves)': 1,
    'Palestra - Sigilo sob uma perspectiva prioritariamente computacional (Wellington Silvano)': 1,
    'Cerimônia de Abertura': 1,
    'Palestra - PowerBI para profissionais de TI (Brian Henkels)': 1,
    'Hackathon Flutter (Cainã Rinaldi Esteche e Renan Igor)': 5,
    'KDE Neon & KDE Plasma: venha para o KDE e ganhe experiência profissional em TI (Mario Araujo Xavier)': 1,

    # Terça
    'Palestra - Passado, Presente e Futuro do Trabalho com Dados (Pâmela Nunes)': 1,
    'Palestra - Oportunidades em Blockchain: Inovação e a Importância da Segurança (Pedro Veiga e Claudio Gerolimetto)': 1,
    'Palestra - ADES: Assinador Digital com Certificados de Uso Único do LabSEC (Eduardo Perottoni)': 1,
    'Painel Segurança (Dra. Carla Merkle Westphall, Dra. Thaís Bardini Idalino e Dr. Jean E. Martina)': 2,
    'Palestra - FOSSHUB e o desafio de implantar ferramentas livres no mercado corporativo (Mario Araujo Xavier)': 1,

    # Quarta
    'Palestra - Geocodificação em Python: Uma análise para os números de casas desocupadas em Florianópolis (Ale)': 1,
    'Maratona de Programação': 1,
    'Palestra - Segurança ofensiva: Hackeie sistemas e seja pago por isso (Roberto Rodrigues Filho e Derick Andrighetti)': 1,
    'Palestra - Genesis: Segurança na Cloud by Design usando Infrastructure as Code (Luciano Borguetti Faustino)': 1,
    'Palestra - Criptografia da Troca de Chaves: Clássica à Pós-Quântica (Matheus de Oliveira Saldanha)': 3.5,

    # Quinta
    'Palestra - Entre Bits e Clocks: Desvendando o Projetos de Circuitos Integrados (Rafael Oliveira)': 1,
    'Palestra - Como entender vulnerabilidades: Do compilador a ReDoS + Live Hacking (Samuel Cardoso)': 1,
    'Minicurso de LaTeX (Gustavo)': 1,
    'Palestra - Assinatura digital tolerante a modificações (Anthony Kamers)': 1,
    'Palestra - Tratamento de Dados JSON em Banco de Dados (Ronaldo dos Santos Mello)': 1.5,
    'Palestra - Projetos Pessoais: De Hobby a Carreira Internacional (Mateus Cechetto)': 1,
    'Palestra - FOSSHUB e o desafio de implantar ferramentas livres no mercado corporativo (Mario Araujo Xavier)': 1,

    # Sexta
    'Palestra - Proteção de dados no processo de desenvolvimento (Miliane Fantonelli)': 1,
    'Dedos e Grafos: Vencendo com Matemática - Um guia para dominar Jogos de Estratégia (Cainã Rinaldi Esteche)': 1,
    'Clean code ainda é Clean? (Gustavo)': 1,
    'Trabalho Remoto em Empresas de Tecnologia (Ricardo Goes e Bruno Muniz)': 1,
    'Hackathon Flutter - Premiação (Cainã Rinaldi Esteche e Renan Igor)': 1,
}


def remover_acentos(texto):
    # Normaliza a string para a forma 'NFD' e remove os caracteres de combinação
    return ''.join(
        char for char in unicodedata.normalize('NFD', texto)
        if unicodedata.category(char) != 'Mn'
    )


def encontrar_strings(string_grande, lista_strings_menores):
    # Filtra as strings menores encontradas na string grande
    strings_encontradas = [
        substring for substring in lista_strings_menores if substring in string_grande]

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
                validos[matricula]['palestras'] += encontrar_strings(
                    string_grande, lista_strings_menores)


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
    gerador_certificado.enviar_email_com_certificado(
        validos[participante]['nome'], validos[participante]['cpf'], validos[participante]['horas'], validos[participante]['email'])
