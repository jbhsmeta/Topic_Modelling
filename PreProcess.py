from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re

#Tokenize
def Tokenize(string_txt):
    mystring_tokens=word_tokenize(string_txt)
    return mystring_tokens

#Remove Punctuations
def rem_punct(string_txt):
    mystring_tokens=Tokenize(string_txt)
    str_tokens=[char for char in mystring_tokens if char not in string.punctuation]
    return " ".join(str_tokens)

# Remove digits
def rem_digits(string_txt):
    proc_txt=re.sub(r'\d[a-zA-Z0-9\.\/\-\@]+|[a-zA-Z0-9\.\/\-\@]+\d|\d',' ',string_txt) # Digits replaced with space
    return proc_txt
    
# Remove web address and mail address
def rem_weblnk_mail(string_txt):
    proc_txt=re.sub(r'(https?:\/\/)?(www\.)?[a-zA-Z0-9\.\/\-\@]\[a-z]+|[a-zA-Z0-9\.\/\-\@]+(.com)\s+|(.com)$',' ',string_txt) # Web_links and mails replaced with space
    return proc_txt                

#Remove all the special characters
def sp_char(string_txt):
    proc_txt = re.sub(r'\W',' ',string_txt)
    return proc_txt

#Removing all single characters appearing at the start
def sngle_char_strt(string_txt):
    proc_txt = re.sub(r'^\s+[a-z]\s+',' ',string_txt)
    return proc_txt
    
# Remove all single characters    
def sngle_char(string_txt):
    proc_txt = re.sub(r'\s+[a-z]\s+|\s+[a-z]{2,2}\s+',' ',string_txt)  #|\s+[a-z]{2,}\s+
    return proc_txt

#Substitute multiple spaces with a single space
def rem_mul_spc(string_txt):
    proc_txt = re.sub(r'\s+',' ',string_txt, flags=re.I)
    return proc_txt

#Remove stopwords
def RemoveStopWords(string_txt):
    mystring_tokens=Tokenize(string_txt) 
    stopwords_english = list(set(stopwords.words('english')))
    add_stp_wrds=['http','html','attn','tel']
    stopwords_english.extend(add_stp_wrds)
    post_stopwords=[word for word in mystring_tokens if word.lower() not in stopwords_english]
    return " ".join(post_stopwords)

# Lemmatize String
def Lemmatize(string_txt):
    word_lem=WordNetLemmatizer()
    post_stopword_string = RemoveStopWords(string_txt)
    post_stopword_tokens=Tokenize(post_stopword_string)
    lemm_lst=[ word_lem.lemmatize(word) for word in post_stopword_tokens]
    return " ".join(lemm_lst)

# Convert string to lower case
def to_lower(string_txt):
    str_tokens=Tokenize(string_txt)
    str_tokens=[char.lower() for char in str_tokens]
    return " ".join(str_tokens)

#Substitute blank single quotes with no space
def rem_other(string_txt):
    lst=['``','` `',"''","' '"]
    word_sent=Tokenize(string_txt)
    final_word=[word for word in word_sent if word not in lst]
    return " ".join(final_word)

def preprocess_text(string_txt):
     

    proc_text=string_txt

    #Convert the string to lower case
    proc_text=to_lower(proc_text)

    # Remove weblinks & mail_ids
    proc_text=rem_weblnk_mail(proc_text)

     # Remove digits
    proc_text=rem_digits(proc_text)

    # Remove Stopwords
    proc_text=RemoveStopWords(proc_text)

    #Lemmatize
    proc_text=Lemmatize(proc_text)

    #Remove Special Character
    proc_text=sp_char(proc_text)

    #Remove Single Character
    proc_text=sngle_char(proc_text)

    # Remove all punctiations
    proc_text=rem_punct(proc_text)

    #Remove Single Character at Start
    proc_text=sngle_char_strt(proc_text)

    #Removing single quotes
    proc_text=rem_other(proc_text)

    #Remove Multiple Space
    proc_text=rem_mul_spc(proc_text)

    #Convert the string to lower case
    proc_text=to_lower(proc_text)
         
    return proc_text