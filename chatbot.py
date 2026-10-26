
import random
import re
from typing import Dict, List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from iagenerativa import generar_respuestas


app = FastAPI(
    title="CeniChat - Oferta educativa CENIGRAF",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    history: List[Dict[str, str]] = Field(default_factory=list)


class ChatResponse(BaseModel):
    reply: str


"""
def responder(mensaje: str) -> str:
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            datos = archivo.readlines()
    except FileNotFoundError:
        return "Error: no se encuentra el archivo datos.txt."

    modelo = {}

    for frase in datos:
        palabras = frase.lower().split()

        for i in range(len(palabras) - 1):
            actual = palabras[i]
            siguiente = palabras[i + 1]

            if actual not in modelo:
                modelo[actual] = []

            modelo[actual].append(siguiente)

    texto = mensaje.strip().lower()

    if any(saludo in texto for saludo in ("hola", "buenas", "hey")):
        return (
            "¡Hola! Soy CeniChat, el asistente de CENIGRAF. "
            "¿En qué puedo ayudarte?"
        )

    if "nombre" in texto:
        return (
            "Soy CeniChat, un chatbot básico desarrollado "
            "con Python y FastAPI."
        )

    if any(palabra in texto for palabra in ("adiós", "chao", "hasta luego")):
        return "¡Hasta luego! Gracias por conversar con CeniChat."

    if "ayuda" in texto:
        return (
            "Puedo generar frases a partir de mis datos de aprendizaje. "
            "Prueba con palabras como aprendiz, estudiante, python, "
            "flask, react o mysql."
        )

    palabras_usuario = re.findall(r"\w+", texto)

    palabras_vacias = {
        "que", "qué", "como", "cómo", "es", "el", "la", "los",
        "las", "un", "una", "de", "del", "en", "y", "a",
        "me", "puedes", "dime", "sobre", "por", "favor"
    }

    candidatas = [
        palabra
        for palabra in palabras_usuario
        if palabra in modelo and palabra not in palabras_vacias
    ]

    if not candidatas:
        return (
            "No encuentro una palabra conocida en tu consulta. "
            "Prueba con aprendiz, estudiante, python, flask, react o mysql."
        )

    actual = candidatas[-1]
    frase_generada = [actual]

    for _ in range(7):
        if actual not in modelo:
            break

        siguiente = random.choice(modelo[actual])
        frase_generada.append(siguiente)
        actual = siguiente

    respuesta = " ".join(frase_generada)

    return "Según los patrones de mis datos: " + respuesta
"""


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return HTML


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    respuesta = await generar_respuestas(request.message)

    return ChatResponse(reply=respuesta)


HTML = r"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#17191c">

  <title>CeniChat · Oferta educativa CENIGRAF</title>

  <style>
    :root {
      color-scheme: dark;
      --carbon: #17191c;
      --graphite: #202327;
      --panel: #24272c;
      --surface: #2b2f35;
      --border: #3a3e45;
      --silver: #c4c8ce;
      --white: #f4f5f6;
      --muted: #969ca5;
      --hover: #343940;
    }

    * {
      box-sizing: border-box;
    }

    html {
      min-height: 100%;
      background: var(--carbon);
    }

    body {
      font-family: Inter, "Segoe UI", system-ui, sans-serif;
      max-width: 850px;
      min-height: 100vh;
      margin: 0 auto;
      padding: 54px 24px;
      color: var(--white);
      background:
        radial-gradient(
          ellipse at 50% 0%,
          #353941 0%,
          var(--carbon) 55%
        );
    }

    h1 {
      margin: 0;
      color: var(--white);
      text-align: center;
      font-size: clamp(1.7rem, 4vw, 2.5rem);
      font-weight: 750;
      letter-spacing: -1.2px;
    }

    .description {
      max-width: 550px;
      margin: 14px auto 34px;
      color: var(--muted);
      text-align: center;
      font-size: .98rem;
      line-height: 1.7;
    }

    .panel {
      padding: 26px;
      border: 1px solid var(--border);
      border-radius: 22px;
      background: rgba(32, 35, 39, .94);
      box-shadow:
        0 24px 65px #00000035,
        inset 0 1px 0 #ffffff08;
    }

    .section-title {
      margin: 0 0 16px;
      color: var(--silver);
      font-size: .82rem;
      font-weight: 700;
      letter-spacing: 1.2px;
      text-transform: uppercase;
    }

    #frequent-questions {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
      margin-bottom: 30px;
    }

    button {
      min-height: 44px;
      padding: 12px 17px;
      border: 1px solid #d4d7dc;
      border-radius: 11px;
      background: #d4d7dc;
      color: #17191c;
      cursor: pointer;
      font: inherit;
      font-size: .9rem;
      font-weight: 650;
      transition:
        background .2s ease,
        border-color .2s ease,
        color .2s ease,
        transform .2s ease;
    }

    button:hover:not(:disabled) {
      border-color: #ffffff;
      background: #ffffff;
      transform: translateY(-1px);
    }

    button:active:not(:disabled) {
      transform: scale(.98);
    }

    button:disabled {
      opacity: .5;
      cursor: not-allowed;
    }

    .question-button {
      min-height: 58px;
      border-color: var(--border);
      background: var(--graphite);
      color: var(--silver);
      text-align: left;
      line-height: 1.5;
    }

    .question-button:hover:not(:disabled) {
      border-color: #747b85;
      background: var(--hover);
      color: var(--white);
    }

    .chat-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 14px;
    }

    .chat-header .section-title {
      margin: 0;
    }

    #clear-chat {
      min-height: 36px;
      padding: 8px 12px;
      border-color: var(--border);
      background: transparent;
      color: var(--muted);
      font-size: .82rem;
    }

    #clear-chat:hover:not(:disabled) {
      border-color: #777e88;
      background: var(--hover);
      color: var(--white);
    }

    #chat {
      height: 390px;
      overflow-y: auto;
      overflow-x: hidden;
      padding: 18px;
      margin-bottom: 18px;
      border: 1px solid var(--border);
      border-radius: 15px;
      background: #191b1f;
      overflow-wrap: anywhere;
      scrollbar-color: #50555e #191b1f;
      scrollbar-width: thin;
      scroll-behavior: smooth;
    }

    .message {
      width: fit-content;
      max-width: 88%;
      padding: 12px 15px;
      margin: 12px 0;
      border: 1px solid var(--border);
      border-radius: 14px;
      color: var(--white);
      font-size: .94rem;
      line-height: 1.65;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
    }

    .bot-message {
      margin-right: auto;
      border-bottom-left-radius: 4px;
      background: #292d32;
      color: #e3e5e8;
    }

    .user-message {
      margin-left: auto;
      border-color: #666c75;
      border-bottom-right-radius: 4px;
      background: #41464e;
      color: #ffffff;
    }

    .typing {
      border-style: dashed;
      background: #22252a;
      color: var(--muted);
      font-style: italic;
    }

    form {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 7px;
      border: 1px solid var(--border);
      border-radius: 14px;
      background: #191b1f;
      transition: border-color .2s ease;
    }

    form:focus-within {
      border-color: #858c96;
      box-shadow: 0 0 0 3px #ffffff08;
    }

    input {
      flex: 1;
      min-width: 0;
      padding: 13px 12px;
      border: 0;
      outline: none;
      background: transparent;
      color: var(--white);
      font: inherit;
      font-size: .95rem;
    }

    input::placeholder {
      color: #777e88;
    }

    input:focus {
      outline: none;
    }

    input:disabled {
      opacity: .6;
    }

    form button {
      flex-shrink: 0;
      padding: 12px 20px;
    }

    button:focus-visible {
      outline: 2px solid var(--white);
      outline-offset: 3px;
    }

    @media (max-width: 600px) {
      body {
        padding: 32px 14px;
      }

      .description {
        margin-bottom: 25px;
      }

      .panel {
        padding: 17px;
        border-radius: 17px;
      }

      #frequent-questions {
        grid-template-columns: 1fr;
        gap: 8px;
        margin-bottom: 24px;
      }

      .question-button {
        min-height: 48px;
      }

      #chat {
        height: 55vh;
        min-height: 270px;
        max-height: 480px;
        padding: 12px;
      }

      .message {
        max-width: 94%;
        font-size: .9rem;
      }

      form {
        gap: 5px;
      }

      input {
        padding: 12px 8px;
        font-size: .9rem;
      }

      form button {
        padding: 11px 14px;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      *,
      *::before,
      *::after {
        scroll-behavior: auto !important;
        transition: none !important;
      }
    }
  </style>
</head>

<body>
  <h1>CeniChat · Oferta educativa CENIGRAF</h1>

  <p class="description">
    ¡Hola! Soy el asistente de CENIGRAF.
    Pregúntame por nuestra oferta educativa.
  </p>

  <main class="panel">
    <p class="section-title">Preguntas frecuentes</p>

    <div id="frequent-questions">
      <button type="button" class="question-button">
        ¿Qué programas ofrece CENIGRAF?
      </button>

      <button type="button" class="question-button">
        ¿Cuánto duran los programas?
      </button>

      <button type="button" class="question-button">
        ¿Cómo puedo inscribirme?
      </button>

      <button type="button" class="question-button">
        ¿Qué requisitos necesito?
      </button>
    </div>

    <div class="chat-header">
      <p class="section-title">Conversación</p>
      <button type="button" id="clear-chat">Limpiar chat</button>
    </div>

    <div id="chat" aria-live="polite" aria-busy="false">
      <p class="message bot-message">
        CeniChat: ¡Hola! Soy el asistente de CENIGRAF.
        Selecciona una pregunta frecuente o escribe tu consulta.
      </p>
    </div>

    <form id="form">
      <input
        id="message"
        autocomplete="off"
        placeholder="Escribe tu mensaje..."
        maxlength="2000"
        aria-label="Escribe tu mensaje"
      >

      <button type="submit" id="send-button">Enviar</button>
    </form>
  </main>

  <script>
    const chat = document.querySelector('#chat');
    const form = document.querySelector('#form');
    const input = document.querySelector('#message');
    const sendButton = document.querySelector('#send-button');
    const clearButton = document.querySelector('#clear-chat');
    const questionButtons = document.querySelectorAll('.question-button');

    let isSending = false;

    function addMessage(who, text) {
      const p = document.createElement('p');
      p.className = 'message';

      if (who === 'Tú') {
        p.classList.add('user-message');
      } else {
        p.classList.add('bot-message');
      }

      p.textContent = `${who}: ${text}`;
      chat.appendChild(p);
      chat.scrollTop = chat.scrollHeight;
    }

    function showTyping() {
      const p = document.createElement('p');
      p.id = 'typing-indicator';
      p.className = 'message typing';
      p.textContent = 'CeniChat está escribiendo...';

      chat.appendChild(p);
      chat.setAttribute('aria-busy', 'true');
      chat.scrollTop = chat.scrollHeight;
    }

    function hideTyping() {
      const indicator = document.querySelector('#typing-indicator');

      if (indicator) {
        indicator.remove();
      }

      chat.setAttribute('aria-busy', 'false');
    }

    async function sendMessage(text) {
      const message = text.trim();

      if (!message || isSending) {
        return;
      }

      isSending = true;
      input.value = '';
      input.disabled = true;
      sendButton.disabled = true;

      questionButtons.forEach(button => {
        button.disabled = true;
      });

      addMessage('Tú', message);
      showTyping();

      try {
        const response = await fetch('/api/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ message })
        });

        if (!response.ok) {
          throw new Error('No se pudo obtener una respuesta.');
        }

        const data = await response.json();
        addMessage('CeniChat', data.reply);
      } catch (error) {
        addMessage(
          'CeniChat',
          `Error: ${error.message} Comprueba la conexión e inténtalo de nuevo.`
        );
      } finally {
        hideTyping();
        isSending = false;
        input.disabled = false;
        sendButton.disabled = false;

        questionButtons.forEach(button => {
          button.disabled = false;
        });

        input.focus();
      }
    }

    form.addEventListener('submit', function(event) {
      event.preventDefault();

      const message = input.value.trim();

      if (!message) {
        addMessage(
          'CeniChat',
          'Por favor, escribe un mensaje antes de enviarlo.'
        );

        input.focus();
        return;
      }

      sendMessage(message);
    });

    questionButtons.forEach(button => {
      button.addEventListener('click', function() {
        sendMessage(button.textContent);
      });
    });

    clearButton.addEventListener('click', function() {
      if (isSending) {
        alert(
          'Espera a que termine la respuesta antes de limpiar el chat.'
        );
        return;
      }

      const confirmed = confirm(
        '¿Estás seguro de que deseas borrar la conversación visible?'
      );

      if (confirmed) {
        chat.innerHTML = '';

        addMessage(
          'CeniChat',
          '¡Hola! Soy el asistente de CENIGRAF. ' +
          'Selecciona una pregunta frecuente o escribe tu consulta.'
        );
      }
    });
  </script>
</body>
</html>"""
