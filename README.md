# MovieRecommendation

#Search
------------------------

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


#Classification:
---------------------------------------

For implementing the classification i used naive bayes algorithm. Naive Bayes model is easy to build and particularly useful for very large data sets. Along with simplicity, Naive Bayes is known to outperform even highly sophisticated classification methods.

Bayes theorem provides a way of calculating posterior probability P(c|x) from P(c), P(x) and P(x|c). 

                    P(c/x) = (P(x/c) * p(c) ) / p(x)

P(c|x) is the posterior probability of class (c, target) given predictor (x, attributes).
P(c) is the prior probability of class.
P(x|c) is the likelihood which is the probability of predictor given class.
P(x) is the prior probability of predictor.

TO read the movie dataset file i used following code 
                    
                    data = pd.read_csv("../input/movie_metadata.csv")
                   
To split the movie dataset into training and test i used below code

                    def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]
          
 For calculating the class probabilities
 
                    def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.iteritems():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities
          
And after calculating class probabilities for the code, i used top 1 result to show the genre, the given query belongs to.

#Challenges:
	
The challenging part in building the classifier is to knowing the algorithm and implementing the algorithm and especially in stage of calculating the class probablities and computing the class to which the query belongs to. But i used the materials given by professor and those were very helpful and handy while designing the entire project.



# Executing the application :

Download .apk file.
Install the .apk file in your mobile.
After successful installation, search for the application with name ServerConnection.
Provide admin as both username and password.

# References

https://github.com/jaquine/Cosine-similarity-Tf-Idf-/blob/master/DocumentParser.java

https://stackoverflow.com/questions/27685839/removing-stopwords-from-a-string-in-java

https://github.com/BhaskarTrivedi/QuerySearch_Recommentation_Classification.

https://machinelearningmastery.com/


# Brochure & Video

You can find project brochure and video on my homepage under posts section

