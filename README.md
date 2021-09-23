**Introduction:**
Topic modelling is recognizing the words from the topics present in the document or the corpus of data. This is useful because extracting the words from a document takes more time and is much more complex than extracting them from topics present in the document.
The aim of this project was to identify the relationships between the entities across the given json files which contain the news articles in it and come up with a solution to provide the named entity recognition.
**About this Data:**
In the real live project, the xml files were taken as source. But for now, the xml files been converted to JSON files. A total of 2000 JSON files been provided within the dataset folder.

**Problem Statement**
Topic modelling is recognizing the words from the topics present in the document or the corpus of data. This is useful because extracting the words from a document takes more time and is much more complex than extracting them from topics present in the document. For example, there are 1000 documents and 500 words in each document. So to process this it requires 500\*1000 = 500000 threads. So when you divide the document containing certain topics then if there are 5 topics present in it, the processing is just 5*500 words = 2500 threads.

In this project we do the following
    1. Preprocess the data to remove stopwords, punctuations, mails, single caharacters etc
    2. Lemmatize the text
    3. Vectorize to create TF-IDF vectors
    4. Finally create topic models using LDA form Gensim