
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

df = pd.read_csv('movies_metadata.csv')


# In[3]:

df.head()


# In[4]:

df['overview'].describe()


# In[5]:

df['overview'] = df['overview'].fillna("")


# In[6]:

df['overview'].describe()


# In[7]:

df['tagline'].describe()


# In[8]:

df['tagline'] = df['tagline'].fillna("")


# In[9]:

df['tagline'].describe()


# In[10]:

df['tagline']


# In[11]:

df['genres']


# In[12]:

def extract_genres(data):
    genres_list = []
    for row in data:
        genres_list.append(row['name'])
    return genres_list


# In[13]:

from ast import literal_eval
df['genres'] = df['genres'].apply(literal_eval)


# In[14]:

df['genres'] = df['genres'].apply(extract_genres)


# In[15]:

df['genres']


# In[16]:

def text_dump(data):
    return data['original_title'] + ' ' + data['overview'] + ' '  + data['tagline'] + ' ' .join(data['genres'])
df['unprocesses_text_col'] = df.apply(text_dump, axis=1)
df['unprocesses_text_col'][23455]


# In[19]:

from nltk.corpus import stopwords
import re
df.unprocesses_text_col = df.unprocesses_text_col.apply(lambda x: x.lower())
df['unprocesses_text_col'][23455]


# In[21]:

df['unprocesses_text_col'] = df['unprocesses_text_col'].str.replace('[^\w\s]','')
df['unprocesses_text_col'][23455]


# In[45]:

cachedStopWords = stopwords.words("english")

def removeStopWords(text):
        text = ' '.join([word for word in text.split() if word not in cachedStopWords])
        return text

df['processed_text_col'] = df['unprocesses_text_col'].apply(removeStopWords)
df['processed_text_col'][23455]


# In[46]:

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
stemmer = SnowballStemmer('english')

def stemmerk(text):
    words = word_tokenize(text)
    return ' '.join([stemmer.stem(w) for w in words])
df['processed_text_col'] = df['processed_text_col'].apply(stemmerk)
df['processed_text_col'][23455]


# In[ ]:

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer()
count_matrix = count.fit_transform(df['processed_text_col'])


# In[52]:

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()
train_tfidf = tfidf_transformer.fit_transform(count_matrix)


# In[154]:

import re
def movieList(entry):
    entry = entry.lower()
    entry = re.sub(r'[^\w\s]','',entry)
    entry = removeStopWords(entry)
    entry = stemmerk(entry)
    entry_count_matrix = count.transform([entry])
    entry_tf_idf = tfidf_transformer.transform(entry_count_matrix)
    similarity_score = cosine_similarity(entry_tf_idf, train_tfidf)
    sorted_indexes = np.argsort(similarity_score).tolist()
    return df[['original_title', 'overview']].iloc[sorted_indexes[0][-10:]]


# In[160]:

movies = movieList("batman")
movies


# In[170]:

import json


# In[165]:

mList = []
for movie in movies:
    movieDict = {
        'Title': movie[0],
        'Overview': movie['overview']}
    mList.append(movieDict)
return json.dumps(mList)


# In[ ]:

movie_name = []
movie_description = []
retrive_data = {}
for result_index in range(5):
    movie_name.append(self.MovieData.loc[self.sorted_similarity[result_index],'title'])
    movie_description.append(self.MovieData.loc[self.sorted_similarity[result_index],'overview'])
    retrive_data.update({"Movie":movie_name})
    retrive_data.update({"Description": movie_description})
    return  retrive_data

