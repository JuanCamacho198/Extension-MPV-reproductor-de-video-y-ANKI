# Sistema de Selección y Gestión de Subtítulos para Aprendizaje de Idiomas (MPV + Anki)

Este proyecto es una integración entre el reproductor de video **MPV** y **Anki** que permite seleccionar palabras o frases específicas de los subtítulos mientras ves un video, traducirlas automáticamente y almacenarlas como tarjetas de estudio.

## Funcionalidad Principal

1.  **Reproducción**: Ver videos en MPV.
2.  **Captura**: Al presionar `Ctrl+S`, se pausa el video y se captura el subtítulo actual.
3.  **Selección**: Una interfaz web moderna (React) muestra el subtítulo y permite seleccionar con el mouse la palabra exacta a estudiar.
4.  **Traducción Inteligente**:
    *   Intenta usar **OpenAI (GPT-4o-mini)** para traducciones contextuales.
    *   Si falla (o no hay cuota), usa automáticamente **Google Translate** como respaldo gratuito.
5.  **Integración con Anki**: Guarda la tarjeta directamente en tu mazo configurado (ej. "PALABRAS") sin salir del flujo.

## Requisitos Previos

*   **MPV Player**: Reproductor de video.
*   **Anki**: Con el complemento **AnkiConnect** instalado (código `2055492159`).
*   **Python 3.10+**: Para el backend.
*   **Node.js**: Para el frontend.

## Instalación Inicial

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/JuanCamacho198/Extension-MPV-reproductor-de-video-y-ANKI.git
    cd Extension-MPV-reproductor-de-video-y-ANKI
    ```

2.  **Configurar Backend**:
    ```powershell
    cd backend
    python -m venv venv
    .\venv\Scripts\Activate
    pip install -r requirements.txt
    pip install deep-translator # Para respaldo gratuito
    ```
    *   Crea un archivo `.env` en `backend/` con tu API Key de OpenAI (opcional) y configuración de Anki:
        ```env
        OPENAI_API_KEY=sk-...
        ANKI_DECK=PALABRAS
        ANKI_MODEL=Basic
        ```

3.  **Configurar Frontend**:
    ```powershell
    cd frontend
    npm install
    ```

4.  **Instalar Script de MPV**:
    *   El script `mpv-anki-bridge.lua` debe estar en `%APPDATA%\mpv\scripts\`.
    *   (Si usaste el asistente, esto ya se hizo automáticamente).

---

## Guía de Uso Diario

Para usar tu sistema de aprendizaje cada vez que quieras estudiar, sigue estos 3 sencillos pasos:

### 1. Abre Anki
Asegúrate de que la aplicación de escritorio de Anki esté abierta y ejecutándose en segundo plano.

### 2. Inicia el Sistema
Hemos creado un script automático para facilitar esto. Ve a la carpeta del proyecto y ejecuta:

```powershell
.\start_app.ps1
```

*   Esto abrirá dos ventanas de terminal (Backend y Frontend).
*   Abrirá automáticamente tu navegador en `http://localhost:5173`.

### 3. Abre tu Video en MPV
Abre cualquier archivo de video con MPV. El script se cargará automáticamente.

### ¡A Estudiar!
1.  Mira tu video tranquilamente.
2.  Cuando veas una palabra o frase que quieras aprender, presiona **`Ctrl+S`**.
3.  El video se pausará automáticamente.
4.  Ve a la ventana del navegador abierta.
5.  **Selecciona con el mouse** la palabra o frase específica.
6.  Haz clic en **"Traducir"** (verás la traducción limpia).
7.  Haz clic en **"Guardar en Anki"**.
8.  ¡Listo! La tarjeta se ha guardado en tu mazo "PALABRAS". Vuelve al video y continúa.

## Solución de Problemas

*   **Error de OpenAI (429)**: El sistema cambiará automáticamente a Google Translate. No requiere acción.
*   **No conecta con Anki**: Asegúrate de que Anki está abierto y tienes AnkiConnect instalado.
*   **No captura el subtítulo**: Asegúrate de que el video tiene subtítulos activos en MPV.
