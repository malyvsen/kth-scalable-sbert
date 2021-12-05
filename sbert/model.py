import torch
from transformers import BertTokenizer, BertModel


def run_model(text: str) -> torch.Tensor:
    return (
        model(**tokenizer(text, return_tensors="pt"))
        .last_hidden_state[0]
        .mean(0)
        .detach()
        .numpy()
    )


model = BertModel.from_pretrained("bert-base-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
