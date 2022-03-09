from typing import Any
from bleach import clean
from pykospacing import Spacing
from hanspell import spell_checker
from soynlp.normalizer import repeat_normalize
from konlpy.tag import Okt
import re
import pandas as pd



def text_clean(texts):
    result = []
    for text in texts:  
        #불용어 처리
        text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]','',text)
        
        # 띄어쓰기 수정
        spacing = Spacing()
        text = spacing(text)

        #맞춤법 수정
        temp = spell_checker.check(text)
        text = temp.checked

        #의성어 정규화 
        text = repeat_normalize(text,num_repeats=2)

        result.append(text)
    return result

def make_token(texts):
    #불용어 참고 "https://wikidocs.net/44249"
    stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
    okt = Okt()
    result = []
    for text in texts:
        tokenized_text = okt.morphs(text,stem=True) #토큰화
        stopwords_removed_sentence = [word for word in tokenized_text if not word in stopwords] #불용어 제거
        result.append(stopwords_removed_sentence)

    return result
    
     
    




g


