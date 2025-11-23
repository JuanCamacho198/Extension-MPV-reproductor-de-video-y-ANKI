Write-Host "Iniciando Backend..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; .\venv\Scripts\Activate; uvicorn main:app --reload --port 8000"

Write-Host "Iniciando Frontend..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"

Write-Host "----------------------------------------------------------------" -ForegroundColor Cyan
Write-Host "Sistema iniciado." -ForegroundColor Cyan
Write-Host "1. Backend: http://localhost:8000" -ForegroundColor Gray
Write-Host "2. Frontend: http://localhost:5173" -ForegroundColor Gray
Write-Host "3. Abre tu video en MPV con el script cargado." -ForegroundColor Gray
Write-Host "----------------------------------------------------------------" -ForegroundColor Cyan
