from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "SUA_CHAVE"
endpoint = "SEU_ENDPOINT"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
documents = ["Estou adorando aprender sobre Azure Cognitive Services!"]
response = client.analyze_sentiment(documents=documents)

for doc in response:
    print(f"Sentimento detectado: {doc.sentiment}")
