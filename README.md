# RAG en menos de 20 líneas (gratis)

Un RAG (Retrieval-Augmented Generation) real y funcional en Python, usando solo el plan **gratuito** de la API de Gemini. Código del video de [@buildwith.juan](https://www.tiktok.com/@buildwith.juan) en TikTok.

El programa responde preguntas sobre un documento (`restaurante.txt`) y, si la respuesta no está en el documento, dice **"No tengo esa información"** en lugar de inventar.

## Cómo funciona

1. **Carga** el documento.
2. **Divide** el texto en fragmentos (uno por párrafo).
3. **Vectoriza** cada fragmento con `gemini-embedding-001`.
4. **Busca** los 2 fragmentos más parecidos a la pregunta (similitud coseno con numpy).
5. **Genera** la respuesta con Gemini usando **solo** ese contexto.

## Cómo ejecutarlo

1. Crea tu clave gratuita en [Google AI Studio](https://aistudio.google.com/apikey).
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configura la clave y ejecuta:

   ```bash
   # Windows (PowerShell)
   $env:GEMINI_API_KEY="tu_clave"
   # macOS / Linux
   export GEMINI_API_KEY="tu_clave"

   python rag.py
   ```

## Resultado real

```
¿A qué hora cierran?
→ De lunes a sábado a las 10:00 p. m., y los domingos a las 6:00 p. m.

¿Tienen parqueadero?
→ No tengo esa información
```

Para usarlo con tus propios datos, reemplaza `restaurante.txt` por tu documento.

> Nota: los nombres de los modelos y los límites del plan gratuito de Gemini cambian con el tiempo. Si un modelo deja de estar disponible, cambia el nombre en `rag.py`.

## ¿Quieres un RAG o una automatización con IA para tu negocio?

Desarrollo y automatizo procesos con inteligencia artificial.
WhatsApp: **+57 319 714 0770** · TikTok: [@buildwith.juan](https://www.tiktok.com/@buildwith.juan)
