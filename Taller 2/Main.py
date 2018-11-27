
#Se importan los paquetes/librerias
import telepot, time, serial, sys


#Vamos a recuperar desde telegram el nombre del emisor del mensaje y otros...
def principal(msj):
    tipoDeMensaje, tipoDeChat, chatID = telepot.glance(msj)
    informacionEmisor = msj['from']
    emisor = informacionEmisor['first_name']

    if (tipoDeMensaje == 'text'):
        comando = msj ['text'] #mensaje que se le envia al bot
        print('Comando recibido: %s' %comando)
        #El bot va a reaccionar cuando le envien Hola
        if 'Hola' in comando:
            bot.sendMessage(chatID, "Hola "+ emisor +"!")
        elif 'Que tal?' in comando:
            bot.sendMessage(chatID, "Pura vida!")
        elif ('/start') in comando:
            bot.sendMessage(chatID, "Hola " + emisor +
                            ", mi nombre es CRUTN-SC soy un bot y esta es mi lista de acciones\n" +
                            "/GON --> Enciende el led verde.\n" +
                            "/GOFF --> Apaga el led verde.\n" +
                            "/YON --> Enciende el led amarillo.\n" +
                            "/YOFF --> Apaga el led amarillo.\n" +
                            "/RON --> Enciende el led rojo.\n" +
                            "/ROFF --> Apaga el led rojo.\n" +
                            "/AON --> Enciende todos los leds.\n" +
                            "/AOFF --> Apaga todos los leds.\n")
        elif ('/GON' in comando):

            bot.sendMessage(chatID, "led verde encendido")
        elif ('/GOFF' in comando):
            ser.write(b'g')
            bot.sendMessage(chatID, "led verde apagado")
        elif ('/YON' in comando):
            ser.write(b'Y')
            bot.sendMessage(chatID, "led amarillo encendido")
        elif ('/YOFF' in comando):
            ser.write(b'y')
            bot.sendMessage(chatID, "led amarillo apagado")
        elif ('/RON' in comando):

            bot.sendMessage(chatID, "led rojo encendido")
        elif ('/ROFF' in comando):
            ser.write(b'r')
            bot.sendMessage(chatID, "led rojo apagado")
        elif ('/AON' in comando):
            ser.write(b'A')
            bot.sendMessage(chatID, "Todos los leds encendidos")
        elif ('/AOFF' in comando):

            bot.sendMessage(chatID, "Todos los leds apagados")


    if (tipoDeMensaje != 'text'):
        bot.sendMessage(chatID,"No puedo responder a eso " + emisor + " ,solo esta habilitada la opcion de texto.")

#este es el token que nos genera a la hora de crear el bot
bot =  telepot.Bot('742095787:AAFTLwR1oFM4wR0emo08FOzPq4pFamMjVKs')
bot.message_loop(principal)

while 1:
    time.sleep(10)





