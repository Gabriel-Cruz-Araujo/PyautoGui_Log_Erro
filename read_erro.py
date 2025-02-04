import os
import pyautogui
from enviar_log_email import enviar_email

log_path = os.getenv('LOG_PATH')

def verificar_log(log_path):
    with open(log_path, 'r', encoding='utf-8') as log:
        log_content = log.readlines()
    
    erros = [linha for linha in log_content if 'ERROR' in linha]
    return erros

erros_encontrados = verificar_log(log_path)
if erros_encontrados:
    enviar_email(log_path)
else:
    pyautogui.alert("Nenhum erro encontrado", "Verificação concluída")

