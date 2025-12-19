import os
import argparse

import chromadb
from chromadb.utils import embedding_functions

# Optional model SDKs — import only if available to keep the script import-safe
try:
    from openai import OpenAI
    _has_openai = True
except Exception:
    OpenAI = None
    _has_openai = False

try:
    from google import genai
    from google.genai import types as genai_types
    _has_gemini = True
except Exception:
    genai = None
    genai_types = None
    _has_gemini = False

try:
    from anthropic import Anthropic
    _has_claude = True
except Exception:
    Anthropic = None
    _has_claude = False


# Configuration
DATA_PATH = "data/archive/*"
CHROMA_PATH = "car_review_embeddings"
EMBEDDING_FUNC_NAME = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME = "car_reviews"


def get_collection():
    client = chromadb.PersistentClient(CHROMA_PATH)
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_FUNC_NAME
    )

    collection = client.get_collection(
        name=COLLECTION_NAME, embedding_function=embedding_func
    )
    return collection


def query_good_reviews(collection, question, n_results=10):
    return collection.query(
        query_texts=[question],
        n_results=n_results,
        include=["documents"],
        where={"Rating": {"$gte": 3}},
    )


def query_poor_reviews(collection, question, n_results=5):
    return collection.query(
        query_texts=[question],
        n_results=n_results,
        include=["documents"],
        where={"Rating": {"$lte": 3}},
    )


def analyze_with_openai(reviews_str, question, model="gpt-3.5-turbo"):
    if not _has_openai:
        raise RuntimeError("OpenAI SDK not available. Install the official OpenAI Python SDK.")
    client = OpenAI()
    context = """
 You are a customer success employee at a large
  car dealership. Use the following car reviews
  to answer questions: {}
 """

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": context.format(reviews_str)},
            {"role": "user", "content": question},
        ],
        temperature=0,
        n=1,
    )
    return resp.choices[0].message.content


def analyze_with_gemini(reviews_str, question, model="gemini-2.5-flash"):
    if not _has_gemini:
        raise RuntimeError("Gemini (google-genai) SDK not available. Install google-genai.")
    client = genai.Client()
    context = """
 You are a customer success employee at a large
  car dealership. Use the following car reviews
  to answer questions: {}
 """

    resp = client.models.generate_content(
        model=model,
        contents=context.format(reviews_str),
        config=genai_types.GenerateContentConfig(
            system_instruction=question,
            temperature=0,
        ),
    )
    # gemini's response text is available on .text
    return getattr(resp, "text", None) or str(resp)


def analyze_with_claude(reviews_str, question, model="claude-sonnet-4-5"):
    if not _has_claude:
        raise RuntimeError("Anthropic SDK not available. Install the anthropic package.")
    client = Anthropic()
    context = """
 You are a customer success employee at a large
  car dealership. Use the following car reviews
  to answer questions: {}
 """

    resp = client.messages.create(
        model=model,
        system=context.format(reviews_str),
        max_tokens=1024,
        messages=[{"role": "user", "content": question}],
    )
    # Anthropic SDK returns content in resp.content[...] structure in older clients
    # Try a couple of common access patterns
    if hasattr(resp, "content"):
        try:
            return resp.content[0].text
        except Exception:
            return str(resp.content)
    return str(resp)


def run(provider: str):
    collection = get_collection()

    # Positive reviews question
    pos_question = "What's the key to great customer satisfaction based on detailed positive reviews?"
    good_reviews = query_good_reviews(collection, pos_question, n_results=10)
    reviews_str = ",".join(good_reviews["documents"][0])

    print("Good reviews (excerpt):")
    print(reviews_str[:1000])
    print("###########################################")

    # Negative reviews question
    poor_question = (
        "Which of these poor reviews has the worst implications about our dealership? Explain why."
    )
    poor = query_poor_reviews(collection, poor_question, n_results=5)
    poor_reviews_str = ",".join(poor["documents"][0])

    print("Worst review (excerpt):")
    print(poor["documents"][0][0][:1000])
    print("###########################################")

    if provider == "openai":
        summary = analyze_with_openai(reviews_str, pos_question)
        worst = analyze_with_openai(poor_reviews_str, poor_question)
    elif provider == "gemini":
        summary = analyze_with_gemini(reviews_str, pos_question)
        worst = analyze_with_gemini(poor_reviews_str, poor_question)
    elif provider == "claude":
        summary = analyze_with_claude(reviews_str, pos_question)
        worst = analyze_with_claude(poor_reviews_str, poor_question)
    else:
        raise ValueError("Unknown provider: choose one of openai|gemini|claude")

    print(f"{provider} generated summary of good reviews:\n")
    print(summary)
    print("###########################################")
    print(f"{provider} generated analysis of worst review:\n")
    print(worst)


def main():
    parser = argparse.ArgumentParser(description="Unified car review context analyzer")
    parser.add_argument("provider", choices=["openai", "gemini", "claude"], help="Which provider to use")
    args = parser.parse_args()
    run(args.provider)


if __name__ == "__main__":
    main()
