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

## Instalación

*(Instrucciones pendientes de implementación)*
