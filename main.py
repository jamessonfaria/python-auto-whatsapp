from util import whatsapp
import time

# definir os contatos e mensagem
contatos = ['+558199799872', '+558171142643', '+558199799872', '+558199799872', '+558199799872', '+558199799872', '+558199799872', ]
mensagem = 'Olá tudo bem ? ### Mensagem Automática ###'
imagem = "/Users/jamesson/Documents/3x4.png"

navegador = whatsapp.abrir_navegador()

# buscar os contatos
for contato in contatos:
  #  try:
        time.sleep(5)
        whatsapp.buscar_contato(contato, navegador)
        whatsapp.enviar_mensagem(mensagem, navegador)
       # whatsapp.enviar_anexo(imagem, navegador)
#    except:

 #   finally:
