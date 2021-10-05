from basilica import Connection

API_KEY = "8dbd4037-f1a2-40e3-01ab-1f877bfad9b5"
sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]

connection = Connection(API_KEY)
print("CONNECTION", type(connection))
embeddings = list(connection.embed_sentences(sentences))
print(embeddings)

embedding = connection.embed_sentence("Hello World!!!", model = "twitter")
print(type(embedding))
print(type(embedding[0]))
print(len(embedding))

