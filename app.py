from langchain.document_loaders import PyPDFLoader # Probar PyPDF2?
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

pdf_path = "./proyecto.pdf"
loader = PyPDFLoader(pdf_path)

pages = loader.load_and_split()
text = ""

for page in pages:
    text += page.page_content

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=24,
    length_function=len,
    add_start_index=True,
)

texts = text_splitter.create_documents([text])
print(texts[0])
print(texts[1])
print(texts[2])

embeddings_model = OpenAIEmbeddings() # Probar con el modelo free del pibe del video de 1h
embeddings = embeddings_model.embed_documents(texts)

print("Number of documents embedded", len(embeddings))
print("dimension of each embedding", len(embeddings[0]))

# Usamos textract para 

# # Load the PDF and split it into chunks
# chunks = langchain.split_pdf(pdf_path)

# # Embed the chunks
# embedded_chunks = []
# for chunk in chunks:
#     embedded_chunk = langchain.embed_text(chunk)
#     embedded_chunks.append(embedded_chunk)

# # Create a QA Document model
# qa_model = langchain.create_qa_model(embedded_chunks)
