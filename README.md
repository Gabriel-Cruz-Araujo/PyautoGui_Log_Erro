# **RPA - Log Error Checker**

Este projeto é uma **automação simples** desenvolvida para verificar erros em arquivos de log, destacar as linhas com erros em vermelho no terminal, e enviar um e-mail com o arquivo de log anexado. O script foi feito usando **Python**, e pode ser integrado com ferramentas de automação como **PyAutoGUI**.

## **Características**

- Verifica arquivos de log em busca de linhas contendo a palavra "ERROR".
- Destaca erros em **vermelho** no terminal para facilitar a leitura.
- Envia um e-mail com o arquivo de log anexado, caso erros sejam encontrados.
- Utiliza a biblioteca **PyAutoGUI** para alertar o usuário quando nenhum erro for encontrado.

## **Pré-requisitos**

Antes de rodar o projeto, você precisa garantir que as seguintes bibliotecas estão instaladas:

- **PyAutoGUI**: para exibir uma mensagem de alerta.
- **smtplib**: para enviar e-mails com o arquivo de log.
- **os**: para trabalhar com caminhos de arquivos e verificar sua existência.

Para instalar as dependências do **Projeto**, execute:

```bash```
pip install -r requirements.txt

## **Importante**
- **.ENV**: crie um arquivo de configuração de variaveis de ambiente chamado de .env
