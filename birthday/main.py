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

