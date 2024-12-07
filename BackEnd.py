from unstructured.partition.pdf import partition_pdf
from unstructured.partition.text import partition_text
import whisper
import os

def extract_text_from_file(file_path, file_type):
    if file_type == 'pdf':
        elements = partition_pdf(filename=file_path, strategy="fast")
    elif file_type == 'txt':
        elements = partition_text(filename=file_path)
    else:
        raise ValueError("Tipo de arquivo não suportado.")
    
    text = "\n".join([element.text for element in elements if element.text])
    return text

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result['text']

def create_chunks(text, chunk_size=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append({
            'text': chunk,
            'metadata': {
                'length': len(chunk),
                'start_word': i,
                'end_word': min(i + chunk_size, len(words))
            }
        })
    return chunks

def process_file(file_path, file_type):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Arquivo não encontrado.")
    
    if file_type in ['pdf', 'txt']:
        text = extract_text_from_file(file_path, file_type)
    elif file_type == 'mp3':
        text = transcribe_audio(file_path)
    else:
        raise ValueError(f"Tipo de arquivo '{file_type}' não suportado.")
    
    chunks = create_chunks(text)
    return chunks
