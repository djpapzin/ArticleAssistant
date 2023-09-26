from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import SeleniumURLLoader
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate

# Get URLs from the user
input_urls = input("Please enter the URLs separated by commas: ")
urls = [url.strip() for url in input_urls.split(',')]

# Use the selenium scraper to load the documents
loader = SeleniumURLLoader(urls=urls)
docs_not_splitted = loader.load()

# Split the documents into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
docs = text_splitter.split_documents(docs_not_splitted)

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Create Deep Lake dataset
my_activeloop_org_id = "djpapzin"
my_activeloop_dataset_name = "langchain_course_customer_support"
dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)

# Add documents to the Deep Lake dataset
db.add_documents(docs)

# Define the chatbot prompt template
system_message_template = """You are an exceptional customer support chatbot that gently answer questions.
You know the following context information.
{chunks_formatted}
Answer to the following question from a customer. Use only information from the previous context information. Do not invent stuff.
Question: {query}
Answer:"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_message_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

# Initialize the OpenAI chat model
chat = ChatOpenAI(temperature=0)

# Continuous chat loop
while True:
    # Get the user's question
    query = input("\nEnter your question (or type 'exit' to end): ")
    
    # Check if the user wants to exit
    if query.lower() in ['exit', 'quit', 'close', 'bye']:
        print("Goodbye!")
        break

    # Retrieve relevant chunks
    docs = db.similarity_search(query)
    retrieved_chunks = [doc.page_content for doc in docs]

    # Format the prompt
    chunks_formatted = "\n\n".join(retrieved_chunks)
    prompt_formatted = chat_prompt.format_prompt(chunks_formatted=chunks_formatted, query=query).to_messages()

    # Generate the answer
    answer = chat(prompt_formatted)
    print("\nAnswer:", answer.content)
