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
- **.ENV**: crie um arquivo de configuração de variaveis de ambiente chamado de .env, ele serve para configurar as credenciais necessárias para o código como por exemplo email, senha do email e o caminho para os arquivos de log em seu sistema.
- **Configuração do E-mail**
- O script utiliza **SMTP do Gmail** para enviar e-mails. Você precisa de uma conta do Gmail e habilitar o acesso de aplicativos menos seguros ou usar uma senha de aplicativo.
- **Passo 1:** Gere uma senha de aplicativo [aqui](https://myaccount.google.com/apppasswords) se a verificação em duas etapas estiver ativada.  
- **Passo 2:** Defina essa senha na variável `senha` dentro do código ou como variável de ambiente `EMAIL_PASSWORD`.
