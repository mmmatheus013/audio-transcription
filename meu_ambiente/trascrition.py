import whisper

# Carregar modelo
model = whisper.load_model("medium")

# Transcrever com parâmetros
resultado = model.transcribe(
    "restituicao_valeria.mp3",
    language="pt",
    verbose=True
)

# Salvar resultado em um arquivo
with open("restituicao_valeria.txt", "w", encoding="utf-8") as f:
    f.write(resultado["text"])

print("Transcrição concluída!")
