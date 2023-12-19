from PIL import Image, ImageDraw, ImageFont
import yagmail
from config import pass_gmail
import os

class GeradorCertificado:
    @classmethod
    def enviar_email_com_certificado(cls, nome, cpf, horas, email): 
            
            # Gerar um certificado com o nome, cpf e horas
            imagem_certificado = cls.criar_certificado(nome, cpf, horas)

            # Enviar email personalizado
            cls.enviar_email(nome, email, imagem_certificado)


    @staticmethod
    def criar_certificado(nome, cpf, horas):
        # Abrir a imagem de modelo
        imagem = Image.open('certificado.png')
        
        texto1 = f'''Certificamos que {nome}, portador(a) do CPF {cpf},'''
        texto2 = f'''participou da SECCOM 2023 entre os dias 6 de novembro a 10 de novembro,'''
        texto3 = f'''totalizando {horas} horas de atividades.'''        
        
        draw = ImageDraw.Draw(imagem)
        fonte = ImageFont.truetype('arial.ttf', 35)

        # Centralizando o textos
        largura_texto1, _ = draw.textsize(texto1, font=fonte)
        largura_imagem, _ = imagem.size
        ponto_inicio_texto1 = (largura_imagem - largura_texto1) / 2

        # Centralizando o texto2
        largura_texto2, _ = draw.textsize(texto2, font=fonte)
        ponto_inicio_texto2 = (largura_imagem - largura_texto2) / 2
        
        # Centralizando o texto3
        largura_texto3, _ = draw.textsize(texto3, font=fonte)
        ponto_inicio_texto3 = (largura_imagem - largura_texto3) / 2

        # Definindo a cor da fonte como preto (0, 0, 0) e a posição dos textos 
        draw.text((ponto_inicio_texto1, 710), texto1, font=fonte, fill=(0, 0, 0), align='center')
        draw.text((ponto_inicio_texto2, 750), texto2, font=fonte, fill=(0, 0, 0), align='center')
        draw.text((ponto_inicio_texto3, 790), texto3, font=fonte, fill=(0, 0, 0), align='center')

        imagem_certificado = f'{nome}_Certificado.png'
        imagem.save(imagem_certificado)
        return imagem_certificado


    @staticmethod
    def enviar_email(nome, email, imagem_certificado):
        # Inicializar o Yagmail SMTP
        usuario = yagmail.SMTP(user='seu_user@gmail.com', password=pass_gmail) # Insira o email remetente 
        
        assunto = 'Certificado de Participação - SECCOM'
        conteudo = f'Olá {nome},\n\nAqui está o seu certificado de participação da SECCOM 2023. \n\nAtenciosamente,\nOrganização da SECCOM'

        # Anexar a imagem do certificado
        usuario.send(
            to=email,
            subject=assunto,
            contents=conteudo,
            attachments=imagem_certificado
        )

        print(f'Email enviado para {email} com sucesso!')
        os.remove(imagem_certificado) # Remove a imagem do diretório após enviar o email
        print(f"Certificado '{imagem_certificado}' excluído com sucesso.")
