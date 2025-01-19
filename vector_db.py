import pinecone
from langchain.embeddings import OpenAIEmbeddings  # You can adjust this to your specific embeddings

# Initialize Pinecone (or your preferred vector DB)
pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")
index_name = "interview-knowledge"
index = pinecone.Index(index_name)

# Use Langchain's embeddings (OpenAIEmbedding can be replaced with your model)
embedding_model = OpenAIEmbeddings()

def embed_and_store_knowledge(question: str, answer: str):
    """Embed interview Q&A and store them in the VectorDB."""
    question_embedding = embedding_model.embed(question)
    answer_embedding = embedding_model.embed(answer)

    # Storing embeddings in Pinecone (or other DB)
    index.upsert([{"id": question, "values": question_embedding}])
    index.upsert([{"id": answer, "values": answer_embedding}])

def query_knowledge(question: str) -> str:
    """Query VectorDB for relevant knowledge."""
    query_embedding = embedding_model.embed(question)
    result = index.query([query_embedding], top_k=1)
    
    # Return the most relevant result
    return result["matches"][0]["metadata"]["answer"]
