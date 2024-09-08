from flask import Flask, request, jsonify, send_from_directory, render_template
import pdfplumber
from PIL import Image
import os
import openai
from docx import Document
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

# Configurações de diretório para armazenar imagens
UPLOAD_FOLDER = 'static/images'
CERTIFICATE_FOLDER = 'certificates'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CERTIFICATE_FOLDER, exist_ok=True)

# Configure a chave da API OpenAI diretamente
openai.api_key = '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'  # Substitua pela sua chave API real

def extract_text_from_pdf(file):
    text = ""

    # Extração de texto usando pdfplumber
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text
            else:
                # Extração de imagem e OCR (fallback)
                image = page.to_image().original
                text += ocr_from_image(image)

    return text

def ocr_from_image(image):
    from pytesseract import image_to_string
    return image_to_string(image)

def generate_certificate(fields):
    template_path = 'path_to_certificate_template.docx'  # Defina o caminho para o modelo de certificado
    doc = Document(template_path)

    # Mapeie os campos extraídos para os placeholders do documento
    placeholders = {
        "EMPRESA CONTRATANTE": fields.get('company_name', 'N/A'),
        "ENDEREÇO DO CONTRATANTE": fields.get('contract_address', 'N/A'),
        "CNPJ EMPRESA CONTRATANTE": fields.get('cnpj_company', 'N/A'),
        "DATA DE ASSINATURA DO CONTRATO": fields.get('contract_date', 'N/A'),
        "NÚMERO DO PREGÃO ELETRÔNICO": fields.get('auction_number', 'N/A'),
        "NÚMERO DO CONTRATO": fields.get('contract_number', 'N/A'),
        "OBJETIVO SOLICITADO NO CONTRATO": fields.get('objective', 'N/A'),
        "DATA DE INÍCIO DO CONTRATO": fields.get('contract_start', 'N/A'),
        "DATA DE TÉRMINO DO CONTRATO": fields.get('contract_end', 'N/A'),
        "SERVIÇOS PRESTADOS": fields.get('services_provided', 'N/A'),
        "LOCAL DE EXECUÇÃO DOS SERVIÇOS": fields.get('location_of_services', 'N/A'),
        "INFORMAR VOLUMETRIA DOS SERVIÇOS PRESTADOS": fields.get('volumetry', 'N/A'),
        "EQUIPE OPERACIONAL": fields.get('operational_team', 'N/A'),
        "AMBIENTE COMPUTACIONAL": fields.get('computing_environment', 'N/A'),
        "FERRAMENTAS UTILIZADAS": fields.get('tools_used', 'N/A'),
        "TECNOLOGIAS ENVOLVIDAS": fields.get('technologies_involved', 'N/A'),
        "METOLOGIAS": fields.get('methodology', 'N/A'),
        "NÍVEIS DE SERVIÇO (SLA)": fields.get('methodology', 'N/A'),
        "SATISFAÇÃO": fields.get('satisfaction', 'N/A'),
        "Nome": fields.get('signatory_name', 'N/A'),
        "Cargo": fields.get('signatory_role', 'N/A'),
        "E-Mail": fields.get('signatory_email', 'N/A'),
        "Telefone": fields.get('signatory_phone', 'N/A'),
        "LOCAL": fields.get('location', 'N/A'),
        "DATA": fields.get('date', 'N/A')
    }

    # Substituir os placeholders no documento pelo conteúdo real
    for paragraph in doc.paragraphs:
        for placeholder, value in placeholders.items():
            if placeholder in paragraph.text:
                paragraph.text = paragraph.text.replace(placeholder, value)

    # Salve o documento preenchido
    output_path = os.path.join(CERTIFICATE_FOLDER, 'certificado.docx')  # Caminho de saída
    doc.save(output_path)

    return output_path

@app.route('/')
def index():
    return render_template('indexFUNCIONA copy.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    if file and file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(file)
        return jsonify({'text': text})

    return jsonify({'error': 'Tipo de arquivo inválido'}), 400

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    document_text = data.get('document_text')

    if not question or not document_text:
        return jsonify({'error': 'Pergunta ou texto do documento ausente'}), 400

    try:
        # Prepare the chat prompt
        prompt = f"""
        Você tem a tarefa de preencher um documento com base nos dados extraídos. O documento contém placeholders que precisam ser substituídos pelos valores correspondentes extraídos.

        Dados Extraídos:
        {document_text}

        Tarefa:
        Identificar e extrair os seguintes campos do texto e formatar a saída da seguinte forma:

        EMPRESA CONTRATANTE: [Placeholder]
        ENDEREÇO DO CONTRATANTE: [Placeholder]
        CNPJ EMPRESA CONTRATANTE: [Placeholder]
        DATA DE ASSINATURA DO CONTRATO: [Placeholder]
        NÚMERO DO PREGÃO ELETRÔNICO: [Placeholder]
        NÚMERO DO CONTRATO: [Placeholder]
        OBJETIVO SOLICITADO NO CONTRATO: [Placeholder]
        DATA DE INÍCIO DO CONTRATO: [Placeholder]
        DATA DE TÉRMINO DO CONTRATO: [Placeholder]
        SERVIÇOS PRESTADOS: [Placeholder]
        LOCAL DE EXECUÇÃO DOS SERVIÇOS: [Placeholder]
        INFORMAR VOLUMETRIA DOS SERVIÇOS PRESTADOS: [Placeholder]
        EQUIPE OPERACIONAL: [Placeholder]
        AMBIENTE COMPUTACIONAL: [Placeholder]
        FERRAMENTAS UTILIZADAS: [Placeholder]
        TECNOLOGIAS ENVOLVIDAS: [Placeholder]
        METOLOGIAS: [Placeholder]
        NÍVEIS DE SERVIÇO (SLA): [Placeholder]
        SATISFAÇÃO: [Placeholder]
        Nome: [Placeholder]
        Cargo: [Placeholder]
        E-Mail: [Placeholder]
        Telefone: [Placeholder]
        LOCAL: [Placeholder]
        DATA: [Placeholder]
        ANO: [Placeholder]

        Por favor, retorne a resposta no formato acima, substituindo [Placeholder] pelos valores extraídos do texto. Cada campo deve estar em uma linha separada.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Ou "gpt-4o-mini", "gpt-4" ou "gpt-3.5-turbo" dependendo da sua escolha
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3000, # original 1500
            temperature=0.7
        )

        extracted_info = response.choices[0].message['content'].strip()

        # Ensure the output is formatted properly with line breaks
        formatted_info = '\n'.join(line.strip() for line in extracted_info.split('\n') if line.strip())

        return jsonify({
            'extracted_info': formatted_info
        })
    except Exception as e:
        return jsonify({'error': f'Error from OpenAI: {str(e)}'}), 500

@app.route('/generate_certificate', methods=['POST'])
def generate_certificate_route():
    data = request.json
    # Campos que serão preenchidos
    fields = {
        'company_name': data.get('company_name'),
        'contract_address': data.get('contract_address'),
        'cnpj_company': data.get('cnpj_company'),
        'contract_date': data.get('contract_date'),
        'auction_number': data.get('auction_number'),
        'contract number': data.get('contract_number'),
        'objective': data.get('objective'),
        'contract_start': data.get('contract_start'),
        'contract_end': data.get('contract_end'),
        'services_provided': data.get('services_provided'),
        'location_of_services': data.get('location_of_services'),
        'volumetry': data.get('volumetry'),
        'operational_team': data.get('operational_team'),
        'computing_environment': data.get('computing_environment'),
        'tools_used': data.get('tools_used'),
        'technologies_involved': data.get('technologies_involved'),
        'methodology': data.get('methodology'),
        'service_level_agreements_(SLA)': data.get('service_level_agreements_(SLA)'),
        'satisfaction': data.get('satisfaction'),
        'signatory_name': data.get('signatory_name'),
        'signatory_role': data.get('signatory_role'),
        'signatory_email': data.get('signatory_email'),
        'signatory_phone': data.get('signatory_phone'),
        'location': data.get('location'),
        'date': data.get('date'),
        'year': data.get('year')
    }

    try:
        certificate_path = generate_certificate(fields)
        return jsonify({'message': 'Certificate generated successfully', 'certificate_path': certificate_path})
    except Exception as e:
        return jsonify({'error': f'Error generating certificate: {e}'}), 500

@app.route('/certificates/<filename>')
def serve_certificate(filename):
    return send_from_directory(CERTIFICATE_FOLDER, filename)

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
