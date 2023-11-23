import os
import openai
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.http import models

os.environ['OPENAI_API_KEY']="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"

openai_client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)

client = QdrantClient(
    url="https://c933eae4-bb11-4f3f-9473-a457a5459e70.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key="73Xhsd6ZqlZPaV67Su0lcCGeTPk252zwFKRwY2_Fe7cGQXD7JCrpFQ",
)

prev = [""]*3
search_result = ""
context = ""

def generate_ans(query):
    context = prev[0] + prev[1] + prev[2]
    print("Collecting Embeddings ...", end=" ")
    response = openai_client.embeddings.create(
        input=query,
        model="text-embedding-ada-002"
    )
    embeddings = response.data[0].embedding
    search_result = client.search(
        collection_name="csv_collection",
        query_vector=embeddings,
        limit=5
    )
    print("Generating Answer ...")
    print(query)
    prompt=""
    prompt = "these are the prvious conversation - " + context + "\n Now you will be given a query with potential information (hints) related. If the query is based on previous information you may ignore (hints) and if the question is independent of previous information you may ignore the previous information. The query is as follows -"

    for result in search_result:
        prompt += result.payload['text']
    concatenated_string = " ".join([prompt,query])
    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": concatenated_string}
        ]
    )

    prev[0] = prev[1]
    prev [1] = prev[2]
    prev[2] = str(completion.choices[0].message.content)
    context = prev[0] + prev[1] + prev[2]
    return(completion.choices[0].message.content)

def what_search():
    print(search_result)

def what_prev():
    print(prev)

def what_context():
    print(context)