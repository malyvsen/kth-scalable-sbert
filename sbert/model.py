from pathlib import Path
from sentence_transformers import SentenceTransformer
import torch


def run_model(text: str) -> torch.Tensor:
    return model.encode([text])[0]


model = SentenceTransformer(
    Path(__file__).parent.parent
    / "checkpoints/classification_output/v4_training_nli_roberta-base"
)
