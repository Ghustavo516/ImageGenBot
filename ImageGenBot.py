import telebot
import requests
import io
from PIL import Image

TELEGRAM_API_KEY = "Insert your telegram api bot token here"

API_IMAGEM_URL = "https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image"

headers = {"Authorization": "Insert your API HuggingFace here"}
bot = telebot.TeleBot(TELEGRAM_API_KEY)

# LLM Geradora de imagem
def geradorImagem(payload):
	response = requests.post(API_IMAGEM_URL, headers=headers, json=payload)
	return response.content

# Opcoes de contato
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    prompt = mensagem.text
     
    if "image" in prompt:
        bot.send_message(mensagem.chat.id, "OK, I'm creating your image...")
        image_bytes = geradorImagem({"inputs": prompt,})
        image = Image.open(io.BytesIO(image_bytes)) #Gerar imagem
        bot.send_photo(chat_id=mensagem.chat.id, photo=image)
    
while True:    
    bot.polling()
