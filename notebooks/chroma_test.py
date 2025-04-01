import marimo

__generated_with = "0.11.31"
app = marimo.App(width="medium")


@app.cell
def _():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    return api_key, load_dotenv, os


@app.cell
def _():
    from shared.db_handler import ChromaDBHandler
    client = ChromaDBHandler.get_client()
    return ChromaDBHandler, client


@app.cell
def _(client):
    try:
        client.delete_collection(name="my_collection")
    except ValueError:
        print("Not Found")
    return


@app.cell
def _(ChromaDBHandler, api_key, client):

    collection = client.create_collection(
        name="my_collection",
        embedding_function=ChromaDBHandler.get_embedding_function(key=api_key))
    collection.add(
        documents=[
            "This is a document about pineapple",
            "This is a document about oranges"
        ],
        ids=["id1", "id2"]
    )
    return (collection,)


@app.cell
def _(collection):
    from pprint import pprint
    results = collection.query(
        query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
        n_results=1 # how many results to return
    )
    pprint(results)
    return pprint, results


@app.cell
def _(ChromaDBHandler, api_key, pprint):
    oa_ef = ChromaDBHandler.get_embedding_function(key=api_key)
    query_embs = oa_ef(["This is a query document about hawaii"])
    pprint(query_embs)
    return oa_ef, query_embs


@app.cell
def _(collection, pprint, query_embs):
    em_results = collection.query(query_embeddings=query_embs, n_results=1)
    pprint(em_results)
    return (em_results,)


if __name__ == "__main__":
    app.run()
