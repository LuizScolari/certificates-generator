# Gerador de Certificados SECCOM - Organização

![logo seccom](assets/seccom2.png)
Este repositório contém um programa em Python para gerar certificados de participação para eventos, como a SECCOM (Semana Acadêmica da Computação). O programa lê dados de arquivos Json e gera um certificado no formato PNG.

## Pré-requisitos
Para utilizar este programa, você precisa ter o Python instalado em sua máquina. Além disso, são necessárias algumas bibliotecas específicas, listadas no arquivo `requirements.txt`.

## Instalação
Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:

   ```sh
   pip install -r requirements.txt

   ```


## Estrutura dos Arquivos
`gerador_certificado.py`: Módulo principal que contém a lógica para a geração dos certificados.

`main.py`: Script para processar os dados dos organizadores e chamar o gerador de certificados.

Arquivos `.json`: Devem incluir os dados do formulário da organização em formato json, como mostrado no `validos_exemplo.json`.

No diretório `assets` há um exemplo de certificado para testes, substitua-o pelo template real do certificado.



## Uso
1. Preparação dos dados:
    * Garanta que todos os arquivos necessários estejam no diretório do projeto e o arquivo `validos.json` esteja na formatação correta.
    * Certifique-se de que o template do certificado (certificado.png) esteja no diretório `assets`.
    
2. Ajuste o código para suas necessidades:
   * No arquivo `gerador_certificado.py`, ajuste a altura dos textos conforme o template usado.

5. Execução:
    * Execute o script `main.py` para processar os dados e gerar os certificados:

    ```sh
    python3 main.py

    ```