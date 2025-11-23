local utils = require 'mp.utils'
local msg = require 'mp.msg'

-- Configuración
local backend_url = "http://localhost:8000/api/capture"

-- Función para capturar el subtítulo
function capture_subtitle()
    local sub_text = mp.get_property("sub-text")
    
    if not sub_text or sub_text == "" then
        mp.osd_message("No hay subtítulo para capturar", 2)
        return
    end

    -- Pausar el video
    mp.set_property("pause", "yes")
    mp.osd_message("Capturando...", 1)

    -- Preparar datos JSON
    local data = {
        text = sub_text,
        timestamp = mp.get_property("time-pos"),
        filename = mp.get_property("filename")
    }
    
    local json_data = utils.format_json(data)

    -- Enviar al backend usando curl
    local args = {
        "curl",
        "-X", "POST",
        "-H", "Content-Type: application/json",
        "-d", json_data,
        backend_url
    }

    msg.info("Enviando subtítulo: " .. sub_text)

    mp.command_native_async({
        name = "subprocess",
        args = args,
        capture_stdout = true,
        capture_stderr = true
    }, function(success, result, error)
        if success and result.status == 0 then
            msg.info("Subtítulo enviado correctamente")
            -- Aquí podríamos abrir el navegador automáticamente si lo deseamos
            -- mp.commandv("run", "cmd", "/c", "start", "http://localhost:5173")
        else
            msg.error("Error enviando subtítulo")
            if result and result.stderr then
                msg.error(result.stderr)
            end
            mp.osd_message("Error conectando al backend", 3)
        end
    end)
end

-- Asignar tecla (Ctrl+s)
mp.add_key_binding("ctrl+s", "capture-subtitle", capture_subtitle)

msg.info("MPV Anki Bridge cargado")
