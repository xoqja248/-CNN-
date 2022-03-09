import pandas as pd
import preprocessing as pp 
from gensim.models import Word2Vec

def make_word2vec(train):
    train['document'] = pp.text_clean(train['document']) ## 데이터 정제
    train = train.dropna(how = "any") ## 결측 데이터 제거

    tokenized_data = pp.make_token(train['document'])## text tokenzied

    model = Word2Vec(sentences = tokenized_data, window = 5, min_count = 5, workers = 4, sg = 0) ## sg : cbow

    return model

sample = pd.read_csv("./data/ratings_train.txt",sep='\t')
sample = sample.iloc[0:1000]

model = make_word2vec(sample)
model_result = model.wv.most_similar("재미")
print(model_result)



