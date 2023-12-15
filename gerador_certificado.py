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
        
        texto = f'''Certificamos que {nome}, portador(a) do CPF {cpf}, 
                participou da SECCOM 2023 entre os dias 6 de novembro a 10 de novembro,
                totalizando {horas} horas.'''

        draw = ImageDraw.Draw(imagem)

        fonte = ImageFont.truetype('calibrib.ttf', 40)

        # Definindo a cor da fonte como preto (0, 0, 0)
        draw.text((310, 710), texto, font=fonte, fill=(0, 0, 0), align='center')

        imagem_certificado = f'{nome}_Certificado.png'
        imagem.save(imagem_certificado) # usar para testes
        return imagem_certificado



    @staticmethod
    def enviar_email(nome, email, imagem_certificado):
        # Inicializar o Yagmail SMTP
        usuario = yagmail.SMTP(user='seu_user@gmail.com', password=pass_gmail)
        
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
        os.remove(imagem_certificado)
        print(f"Certificado '{imagem_certificado}' excluído com sucesso.")
