import requests

text = """Once upon a time, in a small village, there were two chickens named Daisy and Duke.
They were best friends and did everything together, from pecking at seeds to taking dust baths.
One day, while they were out foraging for food, they stumbled upon a magical seed.
 They had heard rumors of such seeds that could grant wishes, but they had never actually seen one before.
Excitedly, they decided to make a wish together. 
Daisy wished for a never-ending supply of corn, while Duke wished for the ability to fly.
To their amazement, their wishes came true! 
Daisy found herself surrounded by heaps of delicious corn, while Duke flapped his wings and soared into the sky.
Overjoyed with their newfound abilities, they spent the entire day enjoying their wishes. 
But as the sun began to set, they realized they had forgotten about the most important thing - 
how to share their newfound wealth and happiness with their fellow chickens.
Feeling guilty, they decided to use their wishes for the good of the whole village. 
Daisy shared her endless corn with the other chickens, while Duke taught them how to fly.
From then on, Daisy and Duke were known as the kindest and most generous chickens in the village, 
and their friendship grew stronger with each passing day. 
And even though their wishes had been granted, 
they realized that true happiness lies in sharing and caring for others."""

payload = {
    'text': text
}

response = requests.post('http://localhost:5000/summarize', json=payload)
data = response.json()

summarized_text = data['summarized_text']
print(summarized_text)
