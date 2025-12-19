import os

import chromadb
from chromadb.utils import embedding_functions

from anthropic import Anthropic

os.environ["TOKENIZERS_PARALLELISM"] = "false"

DATA_PATH = "data/archive/*"
CHROMA_PATH = "car_review_embeddings"
EMBEDDING_FUNC_NAME = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME = "car_reviews"

client = chromadb.PersistentClient(CHROMA_PATH)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_FUNC_NAME
)

collection = client.get_collection(
    name=COLLECTION_NAME, embedding_function=embedding_func
)

context = """
 You are a customer success employee at a large
  car dealership. Use the following car reviews
  to answer questions: {}
 """

question = """
 What's the key to great customer satisfaction
  based on detailed positive reviews?
 """

good_reviews = collection.query(
    query_texts=[question],
    n_results=10,
    include=["documents"],
    where={"Rating": {"$gte": 3}},
)

reviews_str = ",".join(good_reviews["documents"][0])
print("Good reviews: ")
print(reviews_str)
print("###########################################")

client = Anthropic()
model = "claude-sonnet-4-5"

good_reviews_analysis = client.messages.create(
    model=model,
    system=context.format(reviews_str),
    max_tokens=1024,
    messages=[
       {"role": "user", "content": question} 
    ]
)

print(f"Claude generated summary with {model} of good reviews: ")
print(good_reviews_analysis.content[0].text)
print("###########################################")

context = """
          You are a customer success employee at a large car dealership.
          Use the following car reivews to answer questions: {}
          """
question = """
            Which of these poor reviews has the worst implications about
            our dealership? Explain why.
            """

poor_reviews = collection.query(
    query_texts=[question],
    n_results=5,
    include=["documents"],
    where={"Rating": {"$lte": 3}},
)

reviews_str = ",".join(poor_reviews["documents"][0])

print("Worst reviews: ")
print(poor_reviews["documents"][0][0])
print("###########################################")

poor_review_analysis = client.messages.create(
    model=model,
    system=context.format(reviews_str),
    max_tokens=1024,
    messages=[
       {"role": "user", "content": question} 
    ]
)

print(f"Claude generated summary with {model} of the single worst review: ")
print(poor_review_analysis.content[0].text)
print("###########################################")
