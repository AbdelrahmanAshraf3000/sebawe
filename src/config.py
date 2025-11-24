class Config:
    MAX_LEN = 200        # Max characters per sentence
    BATCH_SIZE = 64
    EMBED_DIM = 300      # Match FastText dimension
    HIDDEN_DIM = 256     # LSTM Hidden size
    LR = 0.001
    N_EPOCHS = 10
    DEVICE = "cuda"