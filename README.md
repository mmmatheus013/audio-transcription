# Whisper Transcription Application

Esta aplicação utiliza o modelo Whisper para transcrever arquivos de áudio em texto.

## Requisitos

- Python 3.12
- Pacote `whisper`

## Instalação

1. Clone o repositório ou copie os arquivos para o seu ambiente de trabalho.
2. Crie um ambiente virtual e ative-o:
    ```sh
    python3 -m venv meu_ambiente
    source meu_ambiente/bin/activate  # Para Linux/MacOS
    meu_ambiente\Scripts\activate  # Para Windows
    ```
3. Instale as dependências:
    ```sh
    pip install whisper
    ```

## Uso

1. Coloque o arquivo  áudiode que deseja transcrever na mesma pasta que o script [trascrition.py](http://_vscodecontentref_/0).
2. Edite o script [trascrition.py](http://_vscodecontentref_/1) para garantir que o nome do arquivo de áudio está correto.
3. Execute o script:
    ```sh
    python trascrition.py
    ```
4. O resultado da transcrição será salvo em um arquivo de texto com o mesmo nome do arquivo de áudio.

## Exemplo

```python
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