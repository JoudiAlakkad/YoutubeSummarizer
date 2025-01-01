import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
import re
from nltk.corpus import stopwords
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
#nltk.download('punkt_tab')
import numpy as np

def summarize(link):
    unique_id = link.split("=")[-1]
    sub = YouTubeTranscriptApi.get_transcript(unique_id)
    subtitle = " ".join([x['text'] for x in sub])
    subtitle = subtitle.replace("\\", "")
    sentences = sent_tokenize(subtitle)
    organized_sent = {k:v for v,k in enumerate(sentences)}
    tf_idf = TfidfVectorizer(min_df=2, 
                                    strip_accents='unicode',
                                    max_features=None,
                                    lowercase = True,
                                    token_pattern=r'w{1,}',
                                    ngram_range=(1, 3), 
                                    use_idf=True,
                                    smooth_idf=True,
                                    sublinear_tf=True,
                                    stop_words = 'english')

    sentence_vectors = tf_idf.fit_transform(sentences)
    sent_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
    N = 3
    top_n_sentences = [sentences[index] for index in np.argsort(sent_scores, axis=0)[::-1][:N]]
    mapped_sentences = [(sentence,organized_sent[sentence]) for sentence in top_n_sentences]
    mapped_sentences = sorted(mapped_sentences, key = lambda x: x[1])
    ordered_sentences = [element[0] for element in mapped_sentences]
    summary = " ".join(ordered_sentences)
    return summary
    