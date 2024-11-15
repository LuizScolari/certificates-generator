from PIL import Image, ImageDraw, ImageFont

def formatar_cpf(cpf):
    cpf = ''.join(x for x in cpf if x.isdigit()).zfill(11)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def criar_certificado(nome, cpf, horas):
    imagem = Image.open('assets/certificado.png')

    texto1 = f'''Certificamos que {nome}, portador(a) do CPF {cpf},'''
    texto2 = f'''foi voluntário(a) na SECCOM 2024 entre os dias 21 de novembro a 25 de novembro,'''
    texto3 = f'''totalizando {horas} horas de atividades.'''

    draw = ImageDraw.Draw(imagem)
    fonte = ImageFont.truetype('assets/arial.ttf', 35)

    # Calculando a largura dos textos com textbbox
    bbox_texto1 = draw.textbbox((0, 0), texto1, font=fonte)
    largura_texto1 = bbox_texto1[2] - bbox_texto1[0]

    bbox_texto2 = draw.textbbox((0, 0), texto2, font=fonte)
    largura_texto2 = bbox_texto2[2] - bbox_texto2[0]

    bbox_texto3 = draw.textbbox((0, 0), texto3, font=fonte)
    largura_texto3 = bbox_texto3[2] - bbox_texto3[0]

    # Calculando a posição inicial dos textos para centralizá-los
    largura_imagem, _ = imagem.size
    ponto_inicio_texto1 = (largura_imagem - largura_texto1) / 2
    ponto_inicio_texto2 = (largura_imagem - largura_texto2) / 2
    ponto_inicio_texto3 = (largura_imagem - largura_texto3) / 2

    # Definindo a cor da fonte como preto (0, 0, 0) e a altura dos textos
    draw.text((ponto_inicio_texto1, 710), texto1,
              font=fonte, fill=(0, 0, 0), align='center')
    draw.text((ponto_inicio_texto2, 750), texto2,
              font=fonte, fill=(0, 0, 0), align='center')
    draw.text((ponto_inicio_texto3, 790), texto3,
              font=fonte, fill=(0, 0, 0), align='center')

    imagem_certificado = f'{nome}_Certificado.png'
    imagem.save(imagem_certificado)
    return imagem_certificado
