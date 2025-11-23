import { useState, useEffect, useCallback } from 'react'

function App() {
  const [subtitle, setSubtitle] = useState('')
  const [selection, setSelection] = useState('')
  const [translation, setTranslation] = useState('')
  const [status, setStatus] = useState('')

  const fetchSubtitle = useCallback(async () => {
    try {
      const res = await fetch('http://localhost:8000/api/current-subtitle')
      const data = await res.json()
      if (data.text) {
        setSubtitle(prev => {
          if (prev !== data.text) {
            setSelection('')
            setTranslation('')
            setStatus('')
            return data.text
          }
          return prev
        })
      }
    } catch (err) {
      console.error('Error fetching subtitle', err)
    }
  }, [])

  useEffect(() => {
    const interval = setInterval(fetchSubtitle, 1000)
    return () => clearInterval(interval)
  }, [fetchSubtitle])

  const handleMouseUp = () => {
    const text = window.getSelection().toString()
    if (text) {
      setSelection(text)
    }
  }

  const handleTranslate = async () => {
    if (!selection) return
    setStatus('Translating...')
    try {
      const res = await fetch('http://localhost:8000/api/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: selection, context: subtitle })
      })
      const data = await res.json()
      setTranslation(data.translation)
      setStatus('Translated')
    } catch (err) {
      console.error(err)
      setStatus('Error translating')
    }
  }

  const handleSaveAnki = async () => {
    if (!selection || !translation) return
    setStatus('Saving to Anki...')
    try {
      const res = await fetch('http://localhost:8000/api/anki/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ front: selection, back: translation, context: subtitle })
      })
      const data = await res.json()
      if (data.status === 'success') {
        setStatus('Saved to Anki!')
      } else {
        setStatus('Error saving')
      }
    } catch (err) {
      console.error(err)
      setStatus('Error saving')
    }
  }

  return (
    <div className='min-h-screen bg-gray-900 text-white p-8 flex flex-col items-center justify-center'>
      <div className='max-w-2xl w-full bg-gray-800 p-6 rounded-lg shadow-xl'>
        <h1 className='text-2xl font-bold mb-4 text-blue-400'>MPV Anki Assistant</h1>
        
        <div 
          className='text-xl mb-6 p-4 bg-gray-700 rounded min-h-[100px] cursor-text border border-gray-600 hover:border-gray-500 transition-colors'
          onMouseUp={handleMouseUp}
        >
          {subtitle || <span className='text-gray-500 italic'>Esperando subtítulo... (Reproduce un video y presiona Ctrl+S)</span>}
        </div>

        {subtitle && !selection && (
          <p className='text-yellow-400 text-center animate-pulse mb-4'>
            👆 Selecciona con el mouse la palabra o frase que quieres aprender
          </p>
        )}

        {selection && (
          <div className='mb-6 p-4 bg-gray-700/50 rounded border border-blue-500/30'>
            <p className='text-sm text-gray-400 mb-2'>Selección:</p>
            <p className='text-lg font-semibold text-blue-300'>{selection}</p>
            
            <div className='flex gap-4 mt-4'>
              <button 
                onClick={handleTranslate}
                className='px-4 py-2 bg-blue-600 hover:bg-blue-500 rounded font-medium transition-colors'
              >
                Traducir
              </button>
            </div>
          </div>
        )}

        {translation && (
          <div className='mb-6 p-4 bg-green-900/30 rounded border border-green-500/30'>
            <p className='text-sm text-gray-400 mb-2'>Traducción:</p>
            <p className='text-lg'>{translation}</p>
            
            <div className='flex gap-4 mt-4'>
              <button 
                onClick={handleSaveAnki}
                className='px-4 py-2 bg-green-600 hover:bg-green-500 rounded font-medium transition-colors'
              >
                Guardar en Anki
              </button>
            </div>
          </div>
        )}

        {status && (
          <p className='text-center text-sm text-gray-400 mt-4'>{status}</p>
        )}
      </div>
    </div>
  )
}

export default App
