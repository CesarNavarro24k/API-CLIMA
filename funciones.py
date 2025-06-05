def get_weather(city: str) -> str:
    base_url = f"https://wttr.in/{city}?format=%C+%t"  # URL de solicitud con formato (descripción y temperatura)
    response = requests.get(base_url)  # Realizar una solicitud GET a la API
    if response.status_code == 200:  # Si la solicitud es exitosa (código 200)
        return response.text.strip()  # Retornar la respuesta en texto sin espacios extra
    else:
        return "No se pudo obtener la información del clima. Por favor, inténtalo más tarde."  # Retornar el mensaje de error

# Función para la síntesis de voz
# Recordar colocar import  pyttsx3
engine = pyttsx3.init()
def speak(text: str):
    engine.say(text)  # Pasar el texto para la síntesis
    engine.runAndWait()  # Ejecutar la síntesis de voz y esperar a que termine

# Comando para obtener el clima
@bot.command()
async def weather(ctx, *, city: str):
    weather_info = get_weather(city)  # Obtener los datos del clima para la ciudad especificada
    await ctx.send(f"Clima en {city}: {weather_info}")  # Enviar la información del clima al canal de Discord
    speak(weather_info)  # Vocalizar la información obtenida
