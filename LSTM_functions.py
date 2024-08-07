import numpy as np
import torch
import torch.nn as nn

is_cuda = torch.cuda.is_available()

if is_cuda:
  device = torch.device("cuda")
  print("GPU is available")
else:
  device = torch.device("cpu")
  print("GPU not available, CPU used")


def process_sequence(text_sequence, word_to_idx):
  res = []
  for w in text_sequence:
    if w in word_to_idx:
      res.append(word_to_idx[w])
    else:
      res.append(1)
  return res


def pad_sequences_manual(sequences, maxlen, padding='pre'):
  padded_sequences = []
  for seq in sequences:
    if padding == 'pre':
      padded_seq = [0] * (maxlen - len(seq)) + seq
    elif padding == 'post':
      padded_seq = seq + [0] * (maxlen - len(seq))
    else:
      raise ValueError("Invalid padding type. Use 'pre' or 'post'.")
    padded_sequences.append(padded_seq)
  return np.array(padded_sequences)


class SentimentLSTM(nn.Module):
  def __init__(self, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, drop_prob=0.5):
    super(SentimentLSTM, self).__init__()
    self.output_size = output_size
    self.n_layers = n_layers
    self.hidden_dim = hidden_dim

    self.embedding = nn.Embedding(vocab_size, embedding_dim)
    self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers, dropout=drop_prob, batch_first=True)
    self.dropout = nn.Dropout(0.2)
    self.fc = nn.Linear(hidden_dim, output_size)  # fully connected
    self.sigmoid = nn.Sigmoid()

  def forward(self, x, hidden):
    batch_size = x.size(0)
    x = x.long()  # cast to long tensor
    embeds = self.embedding(x)
    lstm_out, hidden = self.lstm(embeds, hidden)
    lstm_out = lstm_out.contiguous().view(-1, self.hidden_dim)

    out = self.dropout(lstm_out)
    out = self.fc(out)
    out = self.sigmoid(out)

    out = out.view(batch_size, -1)
    out = out[:, -1]
    return out, hidden

  def init_hidden(self, batch_size):
    weight = next(self.parameters()).data
    hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to(device),
              weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to(device))
    return hidden