<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Badge" />
  </a>
  <a href="https://flask.palletsprojects.com/en/2.3.x/">
    <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask Badge" />
  </a>
  <a href="https://getbootstrap.com/">
    <img src="https://img.shields.io/badge/-Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white" alt="Bootstrap Badge" />
  </a>
  <a href="https://fontawesome.com/">
    <img src="https://img.shields.io/badge/-FontAwesome-339AF0?style=flat-square&logo=font-awesome&logoColor=white" alt="FontAwesome Badge" />
  </a>
  <a href="https://jquery.com/">
    <img src="https://img.shields.io/badge/-jQuery-0769AD?style=flat-square&logo=jquery&logoColor=white" alt="jQuery Badge" />
  </a>
    <a href="https://openai.com/">
    <img src="https://img.shields.io/badge/-OpenAI-000000?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Badge" />
  </a>
  <a href="https://openai.com/chatgpt">
    <img src="https://img.shields.io/badge/-ChatGPT-0D96F2?style=flat-square&logo=openai&logoColor=white" alt="ChatGPT Badge" />
  </a>
  <a href="https://github.com/dolanmiu/docx">
    <img src="https://img.shields.io/badge/-docx.js-000000?style=flat-square&logo=docx&logoColor=white" alt="docx.js Badge" />
  </a>
  <a href="https://github.com/eligrey/FileSaver.js">
    <img src="https://img.shields.io/badge/-FileSaver.js-FFD400?style=flat-square&logo=file-saver&logoColor=white" alt="FileSaver.js Badge" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">
    <img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5 Badge" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">
    <img src="https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3 Badge" />
  </a>
  <a href="https://www.adobe.com/acrobat/pdf-reader.html">
    <img src="https://img.shields.io/badge/-PDF-000000?style=flat-square&logo=pdf&logoColor=white" alt="PDF Badge" />
  </a>
  <a href="https://www.microsoft.com/en-us/microsoft-365/word">
    <img src="https://img.shields.io/badge/-DOCX-000000?style=flat-square&logo=word&logoColor=white" alt="DOCX Badge" />
  </a>
  <a href="https://en.wikipedia.org/wiki/Plain_text">
    <img src="https://img.shields.io/badge/-TXT-000000?style=flat-square&logo=text-file&logoColor=white" alt="TXT Badge" />
  </a>
</p>

![image](https://github.com/user-attachments/assets/45e15f7a-b7e0-4ac8-8f44-7c6c908bbc75)

## 📜 Descrição
HeloDocs é um sistema web que permite o upload de documentos ```.pdf```, ```.docx```, ```.txt```, realiza a extração de informações e oferece funcionalidades para fazer perguntas sobre o conteúdo extraído. Além disso, o sistema permite a formatação do resultado e a geração de certificados em formato DOCX com base nas informações extraídas dos documentos.

## 🔗 Utilização de APIs da OpenAI

O sistema utiliza a API da OpenAI para responder perguntas e questionamentos feitos pelos usuários. Os modelos utilizados incluem:
- **GPT-4:** Um dos modelos mais avançados disponíveis.
- **GPT-4o-mini:** Versão otimizada do GPT-4.
- **GPT-3.5-turbo:** Modelo anterior, mas ainda muito eficaz.

As perguntas e questionamentos feitos pelos usuários são respondidos pela IA, proporcionando respostas precisas e contextuais baseadas no conteúdo dos documentos.

## ⚙️ Funcionalidades

- 📁 Upload de Documentos: Permite ao usuário fazer upload de arquivos PDF.
- 🔍 Extração de Informações: Processa o documento e extrai informações relevantes.
- ❓ Perguntas sobre o Documento: Permite ao usuário fazer perguntas sobre o conteúdo do documento.
- 👁️ Visualização e Formatação: Exibe e formata as respostas em uma área designada.
- 📝 Geração de Certificado: Gera um certificado em formato DOCX com base nas informações extraídas.
- 🖨️ Impressão de Certificado: Oferece uma opção para imprimir o certificado diretamente da interface web.

## 🛠️ Tecnologias Utilizadas
### Front-End
- **HTML5:** Estrutura básica do conteúdo da página.
- **CSS3:** Estilização da página. Utiliza Bootstrap e FontAwesome para componentes e ícones.
- **JavaScript:** Interatividade e manipulação dinâmica da página. Utiliza jQuery para manipulação do DOM e AJAX para comunicação assíncrona.
- **docx.js:** Biblioteca para criação e manipulação de documentos DOCX.
- **FileSaver.js:** Biblioteca para salvar arquivos no cliente.

### Back-End:

- **Python:** Linguagem utilizada para implementar a lógica do servidor.
- **Flask:** Framework web para criar e gerenciar as rotas e a lógica do servidor.

## 📦 Dependências

### Front-End
- **Bootstrap 3.4.1:** Framework CSS para design responsivo e componentes de interface.
- **FontAwesome 4.7.0:** Biblioteca de ícones vetoriais.
- **Roboto:** Fonte utilizada para estilização do texto.
- **jQuery 3.5.1:** Biblioteca JavaScript para manipulação do DOM e AJAX.
- **docx.js:** Biblioteca para criar e manipular documentos DOCX.
- **FileSaver.js:** Biblioteca para salvar arquivos gerados no cliente.

### Back-End
- **Flask:** Framework para desenvolvimento web em Python.

## 📁 Estrutura do Projeto

- ```index.html``` Página principal que fornece a interface do usuário para fazer upload de documentos, fazer perguntas e gerar certificados.
- ```app.py``` Script Python que configura e executa o servidor Flask, gerencia rotas e processa o upload e as perguntas.
- 
## 📝 Configuração do Tesseract OCR
Para o sistema HeloDocs realizar a extração de texto de documentos PDF usando OCR (Reconhecimento Óptico de Caracteres), é necessário ter o Tesseract OCR instalado em sua máquina. O Tesseract é uma ferramenta de código aberto para OCR, e o pytesseract é uma biblioteca Python que age como uma interface entre o Tesseract e o Python.

### Passos para Instalar e Configurar o Tesseract OCR

**Instalar o Tesseract OCR:**

- Faça o download do instalador do Tesseract OCR a partir do repositório oficial ou de uma fonte confiável.
- Execute o instalador e siga as instruções na tela para concluir a instalação.
- Durante a instalação, anote o diretório onde o Tesseract OCR é instalado. Por padrão, ele é instalado em ```C:\Program Files\Tesseract-OCR\tesseract.exe``` no Windows.
- Configurar o Caminho no Código:

Após a instalação, você precisa configurar o caminho para o executável do Tesseract OCR em seu código Python. Isso é feito para que o pytesseract possa encontrar e usar o Tesseract OCR corretamente.

Adicione o seguinte código no início do seu script Python para definir o caminho do Tesseract OCR:

```
# Configure o caminho para o executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## 🚀 Instruções de Configuração

### Requisitos

- Python 3.x
- Pip (gerenciador de pacotes Python)
- Instalação do Back-End

## Instalação do Back-End

1. Clone o repositório:

```
git clone https://github.com/seu_usuario/helodocs.git
cd helodocs
```

2. Crie um ambiente virtual:

```
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

3. Instale as dependências:

```
pip install flask
```

4. Execute o servidor Flask:

```
python app.py
```

## 🏠 Uso
Acesse o sistema no navegador, geralmente disponível em ```http://localhost:5000.```
Faça o upload de um documento PDF.
Após o upload, utilize o formulário para fazer perguntas sobre o documento.
Visualize as respostas e formate-as conforme necessário.
Gere e baixe o certificado DOCX ou imprima diretamente a partir da interface.

## 💻 Exemplo de ```app.py```

```
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Lógica para processar o upload do arquivo
    return jsonify({"text": "Texto extraído do documento"})

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    document_text = data.get('document_text')
    # Lógica para responder à pergunta
    return jsonify({"extracted_info": "Informação extraída", "certificate_path": "/path/to/certificate"})

if __name__ == '__main__':
    app.run(debug=True)
```
## Autor: [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/levilucena/)](https://www.linkedin.com/in/levilucena/)

