import requests
import time

print("\n\npp grow sender")
print("by Junior Schueller\n\n")

token = input("Insira seu Token (para o Discord autorizar a mensagem): ")

channel_id = input("\nInsira o ID do Canal: ")

sends = 0

print("\nEnviando...\n")


url = "https://discord.com/api/v9/channels/" + channel_id + "/messages"

payload = {
    "content": "pp grow"
}

header = {
    "authorization": token
}

def sendppgrow(snds):
    if(snds == 150):
        print("Aguardando 30 segundos...\n\n")
        time.sleep(30)
        snds = 0
        return sendppgrow(0)
    else:
        print("Aguardando 10 segundos...\n")
        time.sleep(10)
        r = requests.post(url, headers=header, data=payload)
        sends = snds + 1
        print(f"{snds + 1} mensagens enviadas...\n")
        print("Mensagem enviada!\n")
        return sendppgrow(sends)

sendppgrow(sends)
