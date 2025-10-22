from transformers import pipeline

# pipeline automatycznie pobierze mały model; na GPU ustaw device=0
generator = pipeline("text-generation", model="gpt2")

prompt = "Wprowadzenie do generatywnej sztucznej inteligencji:"
result = generator(prompt, max_length=12, num_return_sequences=1)
print(result[0]['generated_text'])
