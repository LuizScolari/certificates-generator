from PIL import Image, ImageDraw, ImageFont
import os

def formatar_cpf(cpf):
    cpf = ''.join(x for x in cpf if x.isdigit()).zfill(11)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def criar_certificado(nome, cpf, horas):
    imagem = Image.open('assets/certificado.png')

    texto1 = f'''Certificamos que {nome}, portador(a) do CPF {cpf},''' 
    texto2 = f'''foi voluntário(a) na SECCOM 2024 entre os dias 21 de novembro a 25 de novembro,'''
    texto3 = f'''totalizando {horas} horas de atividades.'''

    draw = ImageDraw.Draw(imagem)
    fonte = ImageFont.truetype('assets/arial.ttf', 33)

    # Calculando a largura e altura dos textos
    bbox_texto1 = draw.textbbox((0, 0), texto1, font=fonte)
    largura_texto1, altura_texto1 = bbox_texto1[2] - bbox_texto1[0], bbox_texto1[3] - bbox_texto1[1]

    bbox_texto2 = draw.textbbox((0, 0), texto2, font=fonte)
    largura_texto2, altura_texto2 = bbox_texto2[2] - bbox_texto2[0], bbox_texto2[3] - bbox_texto2[1]

    bbox_texto3 = draw.textbbox((0, 0), texto3, font=fonte)
    largura_texto3, altura_texto3 = bbox_texto3[2] - bbox_texto3[0], bbox_texto3[3] - bbox_texto3[1]

    # Calculando a posição centralizada dos textos
    largura_imagem, altura_imagem = imagem.size
    espaco_total = altura_imagem - (altura_texto1 + altura_texto2 + altura_texto3)
    
    # Aumenta o espaço entre os textos e posiciona os textos de maneira mais centralizada
    espaco_vazio = espaco_total // 2.5

    ponto_inicio_texto1 = (largura_imagem - largura_texto1) / 2
    ponto_inicio_texto2 = (largura_imagem - largura_texto2) / 2
    ponto_inicio_texto3 = (largura_imagem - largura_texto3) / 2

    # Definindo a cor da fonte e posicionando os textos
    draw.text((ponto_inicio_texto1, espaco_vazio), texto1, font=fonte, fill=(0, 0, 0), align='center')
    draw.text((ponto_inicio_texto2, espaco_vazio + altura_texto1 + 20), texto2, font=fonte, fill=(0, 0, 0), align='center')
    draw.text((ponto_inicio_texto3, espaco_vazio + altura_texto1 + altura_texto2 + 40), texto3, font=fonte, fill=(0, 0, 0), align='center')

    # Define o caminho e nome do arquivo
    caminho_diretorio = 'certificados_gerados'  # Diretório onde os certificados serão salvos
    imagem_certificado = os.path.join(caminho_diretorio, f'{nome}_Certificado.png')

    # Salva o certificado no local especificado
    imagem.save(imagem_certificado)