import streamlit as st
from BackEnd import process_file
import os

def main():
    st.title("Processador de Arquivos")
    st.write("Carregue um arquivo para processá-lo. Suportamos arquivos PDF, TXT e MP3.")
    
    # Upload de arquivo
    uploaded_file = st.file_uploader("Envie seu arquivo aqui", type=["pdf", "txt", "mp3"])
    
    if uploaded_file is not None:
        # Determinando o tipo de arquivo
        file_extension = uploaded_file.name.split(".")[-1].lower()
        file_path = os.path.join(os.getcwd(), uploaded_file.name)

        # Salvando o arquivo localmente
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        
        st.write(f"Arquivo carregado: {uploaded_file.name}")
        st.write(f"Tipo de arquivo: {file_extension}")

        # Processando o arquivo
        try:
            st.write("Processando o arquivo...")
            process_file(file_path, file_extension)
            st.success("Arquivo processado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")
        finally:
            # Remover arquivo local após processamento
            if os.path.exists(file_path):
                os.remove(file_path)

if __name__ == "__main__":
    main()
