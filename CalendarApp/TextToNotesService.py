# import torch
from transformers import AutoTokenizer, AutoModelWithLMHead


def summarize_text(text):

    # initializing tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained('t5-base')
    model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=True)

    # text tokenizing
    inputs = tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=512, truncation=True)

    # running tokens through the model
    outputs = model.generate(inputs, max_length=512, min_length=50, num_beams=2)

    # decoding our outputs
    summary = tokenizer.decode(outputs[0])

    return summary

