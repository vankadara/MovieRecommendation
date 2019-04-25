# MovieRecommendation

In phase 1 of movie recommendation is to develop a search engine using tf-idf and cosine similarity and below are the steps describing the phase 1 implementation.

Am reading the dataset and tokenizing the text in the overview column and removing the stop words in it. Updating the count of each terms in the postings array

          for index in range(self.totalDocument):
            terms = self.tokenize(self.MovieData.loc[index, 'overview'])
            self.length.append(len(terms))          
            unique_terms = set(terms)
            self.dict = self.dict.union(unique_terms)
            for term in unique_terms:          
                self.postings[term][index] = terms.count(term)
                
                
Term Frequency (TF)

Given below are the terms and their frequency on each of the document.

TF for Document


Document	the	unexamined	life	is	not	worth	living
Term Frequency	1	1	1	1	1	1	1


Normalized TF for Document


Document	the	unexamined	life	is	not	worth	living
Normalized TF	0.142857	0.142857	0.142857	0.142857	0.142857	0.142857	0.142857



Given below is the code in python which i used for  normalized TF calculation.

          def termFrequency(term, document):
             normalizeDocument = document.lower().split()
             return normalizeDocument.count(term.lower()) / float(len(normalizeDocument))
 
Inverse Document Frequency (IDF)
The main purpose of doing a search is to find out relevant documents matching the query.

Given below is the python code to calculate IDF


          def inverseDocumentFrequency(term, allDocuments):
                    numDocumentsWithThisTerm = 0
                    for doc in allDocuments:
                    if term.lower() in allDocuments[doc].lower().split():
                              numDocumentsWithThisTerm = numDocumentsWithThisTerm + 1
 
                    if numDocumentsWithThisTerm > 0:
                              return 1.0 + log(float(len(allDocuments)) / numDocumentsWithThisTerm)
                    else:
                              return 1.0

Then i written following piece of code for cosine similarity
                   
           return dot(query_vec,doc_vec)/(norm(query_vec)*norm(doc_vec))
           
and returning the top 3 in the document vector for the android application to display.

# Executing the application :

Clone the whole repository
Extract Example1.zip folder in the Android Application folder
Download and install Android Studio Version 3.3
Download and install Java runtime
Open Android Studio
Import the Example1 extracted folder.
Build the project and run it

# References

https://github.com/jaquine/Cosine-similarity-Tf-Idf-/blob/master/DocumentParser.java

https://stackoverflow.com/questions/27685839/removing-stopwords-from-a-string-in-java

https://github.com/BhaskarTrivedi/QuerySearch_Recommentation_Classification.

