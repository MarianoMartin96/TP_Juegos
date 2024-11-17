opcion = 5
while opcion != 0:
    print("🌟" * 13)
    print("✨ BIENVENIDOS A 4 EN 1 ✨")
    print("🌟" * 13)
    print("🎮 1 - TA-TE-TI")
    print("💎 2 - Buscamina")
    print("🐍 3 - Snake")
    print("❓ 4 - Juego de preguntas")
    print("🚪 0 - Salir")
    
    try:
        opcion = int(input("👉 Ingrese el número del juego que desees jugar o 0 para dejar de jugar: "))
        
        if opcion == 1:
            print("🎉 Iniciando TA-TE-TI...")
            from tateti import iniciar_juego
        elif opcion == 2:
            print("🎉 Iniciando Buscamina...")
            from Buscamina import iniciar_juego
        elif opcion == 3:
            print("🎉 Iniciando Snake...")
        elif opcion == 4:
            print("🎉 Iniciando Juego de palabras...")
            from JuegoDePalabras import iniciar_juego
        elif opcion == 0:
            print("👋 ¡Gracias por jugar! Hasta la próxima.")
        else:
            print("❌ Opción no válida. Por favor, elige un número del 0 al 4.")
    except ValueError:
        print("⚠️ Entrada no válida. Por favor, ingresa un número.")
