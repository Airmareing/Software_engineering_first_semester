## Проект по программной инженерии  

### Состав команды
- Руссу Вячеслав РИМ-130908
- Исмедлаев Игорь РИМ-130906
- Мухаметгалиев Артём РИМ-130906

### Решаемая задача
Cоздать приложения для транскрибации аудио и видео файлов в текст.  

### Выбранная модель
Whisper от OpenAI https://github.com/openai/whisper.

### Для запуска проектра потребуется
1. Python > 3.8, но < 3.12 (если запускать на версии 3.12, то Whisper не будет работать)
2. openai-whisper
3. ffmpeg-python; так же необходимо скачать и распаковать ffmpeg (https://ffmpeg.org/download.html), а затем добавить в PATH (https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)
4. streamlit
5. FastAPI
6. python-multipart
7. uvicorn
