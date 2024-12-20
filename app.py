import nltk
import streamlit as st
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
ps= PorterStemmer()
def Transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title("Email/SMS Classifier")
input_box = st.text_area("Enter Message")
if st.button('predict'):

    transformed_msg = Transform_text(input_box)
    vector_input = tfidf.transform([transformed_msg])
    result = model.predict(vector_input)[0]

    if result == 1 :
        st.header("spam")
    else:
        st.header("not spam")
