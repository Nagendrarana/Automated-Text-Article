from transformers import pipeline

#generator = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")


#prompt = "Python is incredible"

#res = generator( prompt, max_length=100, temperature=0.7)

print(pipeline('sentiment-analysis')('we love you'))
#print(res)