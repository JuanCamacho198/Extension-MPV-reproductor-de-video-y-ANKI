# Sistema de Selección y Gestión de Subtítulos para Aprendizaje de Idiomas (MPV + Anki)

Este proyecto es una integración entre el reproductor de video **MPV** y **Anki** que permite seleccionar palabras o frases específicas de los subtítulos mientras ves un video, traducirlas automáticamente y almacenarlas como tarjetas de estudio.

## Funcionalidad Principal

1.  **Reproducción**: Ver videos con doble subtítulo en MPV.
2.  **Captura**: Al presionar una tecla (ej. `Ctrl+S`), se pausa el video y se captura el subtítulo actual.
3.  **Selección**: Una interfaz externa se abre permitiendo seleccionar con el mouse la palabra o frase exacta a estudiar.
4.  **Traducción y Guardado**: La selección se traduce (vía OpenAI/DeepL) y se envía automáticamente a Anki.

## Arquitectura

El sistema consta de tres módulos principales:

*   **Cliente MPV (Lua)**: Script que corre dentro de MPV, captura el texto y gatilla el proceso.
*   **Backend (Python/FastAPI)**: Servidor local que orquesta la comunicación, maneja las traducciones y conecta con AnkiConnect.
*   **Frontend (React)**: Interfaz gráfica moderna para realizar la selección de texto y confirmar la creación de la tarjeta.

## Requisitos Previos

*   MPV Player
*   Anki con el plugin AnkiConnect instalado
*   Python 3.10+
*   Node.js (para el desarrollo del frontend)

## Instalación y Ejecución

### 1. Backend (Servidor)
1.  Navega a la carpeta `backend`:
    ```bash
    cd backend
    ```
2.  Crea y activa el entorno virtual:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate
    ```
3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4.  Ejecuta el servidor:
    ```bash
    uvicorn main:app --reload --port 8000
    ```

### 2. Frontend (Interfaz)
1.  Navega a la carpeta `frontend`:
    ```bash
    cd frontend
    ```
2.  Instala las dependencias:
    ```bash
    npm install
    ```
3.  Ejecuta el servidor de desarrollo:
    ```bash
    npm run dev
    ```
    Abre `http://localhost:5173` en tu navegador.

### 3. MPV (Reproductor)
1.  Abre MPV cargando el script Lua:
    ```bash
    mpv --script="ruta/a/mpv-script/mpv-anki-bridge.lua" tu_video.mkv
    ```
    O copia el archivo `.lua` a tu carpeta de scripts de MPV (`%APPDATA%\mpv\scripts\`).

## Uso
1.  Reproduce un video en MPV.
2.  Cuando veas una frase interesante, presiona `Ctrl+S`.
3.  El video se pausará y el subtítulo aparecerá en la interfaz web.
4.  Selecciona la palabra/frase con el mouse.
5.  Haz clic en "Translate" y luego en "Save to Anki".
