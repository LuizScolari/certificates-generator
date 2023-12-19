# Gerador de Certificados SECCOM

Este repositório contém um programa em Python para gerar e enviar certificados de participação para eventos, como a SECCOM (Semana Acadêmica da Computação). O programa lê dados de arquivos CSV, gera um certificado no formato PNG e o envia por e-mail aos participantes.

## Pré-requisitos
Para utilizar este programa, você precisa ter o Python instalado em sua máquina. Além disso, são necessárias algumas bibliotecas específicas, listadas no arquivo `requirements.txt`.

## Instalação
Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:

   ```sh
   pip install -r requirements.txt

   ```


## Estrutura dos Arquivos
`gerador_certificado.py`: Script principal que contém a lógica para a geração e envio dos certificados.

`main.py`: Script para processar os dados dos participantes e chamar o 
gerador de certificados.

`config.py`: Contém configurações, como a senha do e-mail remetente (necessário ajustar com sua própria senha).

Arquivos `.csv`: Devem incluir os dados dos formulários de inscrição e as listas de presença para cada dia do evento.

No diretório `assets` há um exemplo de certificado para testes, substitua-o pelo template real do certificado.



## Uso
1. Preparação dos dados:
    * Garanta que todos os arquivos CSV necessários estejam no diretório do projeto. Isso inclui o arquivo de inscrição (info.csv) e os arquivos de presença para cada dia (segunda.csv, terca.csv, etc.).
    * Certifique-se de que o template do certificado (certificado.png) esteja no diretório `assets`.

2. Configuração do email:
    * Edite o arquivo `config.py` para incluir a senha do seu e-mail (senha de aplicativo do Gmail).
    * Edite o arquivo `gerador_certificado.py` para colocar o seu user (remetente) do gmail.
  
3. Ajuste o código para suas necessidades:
   * No arquivo `main.py`, coloque as palestras/atividades específicas do evento
   * No arquivo `gerador_certificado.py`, ajuste a altura dos textos conforme o template usado.

5. Execução:
    * Execute o script `main.py` para processar os dados e enviar os certificados:

    ```sh
    python3 main.py

    ```
