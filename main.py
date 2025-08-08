from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# Load all text files from the 'planets_data/' directory
loader = DirectoryLoader("planets", glob="*.txt", loader_cls=TextLoader)
documents = loader.load()

# Initialize a free, local embeddings model from Hugging Face.
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create a Chroma vector store from the loaded documents and the new embeddings.
db = Chroma.from_documents(documents, embeddings_model)

# Perform a similarity search on the vector store with a sample query.
query = input()
docs = db.similarity_search(query)

# Print the content of the most similar document.
print(docs[0].page_content)
