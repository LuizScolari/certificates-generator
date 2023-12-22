from PIL import Image, ImageDraw, ImageFont
import yagmail
from config import pass_gmail, user_gmail
import os

class GeradorCertificado:
    @classmethod
    def enviar_email_com_certificado(cls, nome, cpf, horas, email): 
            
            cpf_formatado = cls.formatar_cpf(cpf)
            # Gerar um certificado com o nome, cpf e horas
            imagem_certificado = cls.criar_certificado(nome, cpf_formatado, horas)

            # Enviar email personalizado
            cls.enviar_email(nome, email, imagem_certificado)


    @staticmethod
    def formatar_cpf(cpf):
        cpf = ''.join(x for x in cpf if x.isdigit()).zfill(11)
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        

    @staticmethod
    def criar_certificado(nome, cpf, horas):
        # Abrir a imagem de modelo
        imagem = Image.open('assets/certificado.png')
        
        texto1 = f'''Certificamos que {nome}, portador(a) do CPF {cpf},'''
        texto2 = f'''participou da SECCOM 2023 entre os dias 6 de novembro a 10 de novembro,'''
        texto3 = f'''totalizando {horas} horas de atividades.'''        
        
        draw = ImageDraw.Draw(imagem)
        fonte = ImageFont.truetype('assets/arial.ttf', 35)

        # Centralizando os textos horizontalmente
        largura_texto1, _ = draw.textsize(texto1, font=fonte)
        largura_imagem, _ = imagem.size
        ponto_inicio_texto1 = (largura_imagem - largura_texto1) / 2

        largura_texto2, _ = draw.textsize(texto2, font=fonte)
        ponto_inicio_texto2 = (largura_imagem - largura_texto2) / 2
        
        largura_texto3, _ = draw.textsize(texto3, font=fonte)
        ponto_inicio_texto3 = (largura_imagem - largura_texto3) / 2

        # Definindo a cor da fonte como preto (0, 0, 0) e a altura dos textos 
        draw.text((ponto_inicio_texto1, 710), texto1, font=fonte, fill=(0, 0, 0), align='center')
        draw.text((ponto_inicio_texto2, 750), texto2, font=fonte, fill=(0, 0, 0), align='center')
        draw.text((ponto_inicio_texto3, 790), texto3, font=fonte, fill=(0, 0, 0), align='center')

        imagem_certificado = f'{nome}_Certificado.png'
        imagem.save(imagem_certificado)
        return imagem_certificado


    @staticmethod
    def enviar_email(nome, email, imagem_certificado):
        # Inicializar o Yagmail SMTP
        usuario = yagmail.SMTP(user=user_gmail, password=pass_gmail) 
        
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
