from browser import document
import browser.aio as aio

from time import time
from datetime import datetime

CHANGE_STATES = {
    "...": ".",
    "..": "...",
    ".": ".."
}

def change_time(total_seconds):
    total_seconds -= 1
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    parts = []

    if days > 0:
        parts.append(f"{days}d")
    if days > 0 or hours > 0:
        parts.append(f"{hours:02}h")
    if days > 0 or hours > 0 or minutes > 0:
        parts.append(f"{minutes:02}m")
    parts.append(f"{seconds:02}s")

    document["time1"].text = " ".join(parts)

    return total_seconds

async def refresh_hour():
    now = datetime.now()
    first_event = datetime(2025, 4, 19, 0, 28)

    diference = first_event - now
    total_seconds = int(diference.total_seconds())

    intervalo = 1
    while total_seconds > 0:  # Only run while there's time left
        start = time()

        total_seconds = change_time(total_seconds)

        elapsed = time() - start
    
        to_sleep = max(0, intervalo - elapsed)
        await aio.sleep(to_sleep)
    
    # When timer reaches zero
    document.getElementById("part1").style.display = "none"
    document.body.classList.add("show-cake")  # Add class to body to trigger the CSS


async def refresh_things():
    while True:
        await aio.sleep(0.5)
        dots = document["waiting"].text
        document["waiting"].text = CHANGE_STATES[dots]
        

aio.run(refresh_things())
aio.run(refresh_hour())

from browser import document, window

# Estado para controlar si está reproduciendo o pausado
reproduciendo = False

def toggle_audio(event):
    global reproduciendo
    audio = document["musica-fondo"]
    
    if reproduciendo:
        audio.pause()
        document["boton-musica"].text = "♪"
    else:
        audio.loop = True
        promise = audio.play()
        document["boton-musica"].text = "❚❚"
        
        # Manejar errores de reproducción
        if promise:
            def on_error(error):
                print("Error al reproducir audio:", error)
            
            promise.catch(on_error)
    
    reproduciendo = not reproduciendo

# Asignar el evento de clic al botón
document["boton-musica"].bind("click", toggle_audio)

