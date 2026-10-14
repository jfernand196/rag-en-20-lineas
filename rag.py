import numpy as np
from google import genai

client = genai.Client()  # usa la variable de entorno GEMINI_API_KEY

# 1. Cargar el documento
texto = open("restaurante.txt", encoding="utf-8").read()

# 2. Dividir en fragmentos (uno por párrafo)
fragmentos = [p.strip() for p in texto.split("\n\n") if p.strip()]

# 3. Convertir cada fragmento en un vector
def vectorizar(textos):
    r = client.models.embed_content(model="gemini-embedding-001", contents=textos)
    v = np.array([e.values for e in r.embeddings])
    return v / np.linalg.norm(v, axis=1, keepdims=True)

vectores = vectorizar(fragmentos)

def preguntar(pregunta, k=2):
    # 4. Buscar los fragmentos más parecidos
    q = vectorizar([pregunta])[0]
    mejores = np.argsort(vectores @ q)[::-1][:k]
    contexto = "\n".join(fragmentos[i] for i in mejores)
    # 5. Generar la respuesta solo con ese contexto
    prompt = (f"Responde SOLO con este contexto. Si no está, di 'No tengo esa información'.\n"
              f"Contexto:\n{contexto}\n\nPregunta: {pregunta}")
    return client.models.generate_content(model="gemini-3.5-flash-lite", contents=prompt).text

print(preguntar("¿A qué hora cierran?"))
print(preguntar("¿Tienen parqueadero?"))
