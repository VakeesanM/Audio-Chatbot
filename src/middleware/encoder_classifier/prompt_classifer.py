import torch
import torch.nn as nn
import math
from src.middleware.encoder_classifier.positional_encoder import PositionalEncoding


class PromptClassifer(nn.Module):
    def __init__(self, vocab_size, d_model=256, nhead=8, num_layers=4,
                 dim_feedforward=1024, dropout=0.1,
                 max_len=512, pad_idx=0):
        super().__init__()
        self.pad_idx = pad_idx
        self.d_model = d_model

        self.embedding = nn.Embedding(vocab_size, d_model, padding_idx=pad_idx)
        self.pos_encoder = PositionalEncoding(d_model, max_len, dropout)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True,
            norm_first=True,   
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)


        self.head1 = nn.Linear(d_model, 2)


    def forward(self, x):

        padding_mask = (x == self.pad_idx)  

        h = self.embedding(x) * math.sqrt(self.d_model)
        h = self.pos_encoder(h)
        h = self.encoder(h, src_key_padding_mask=padding_mask)  

        mask = (~padding_mask).unsqueeze(-1).float()            # 
        pooled = (h * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1e-9)

        logits = self.head1(pooled)
        return logits   
