# MovieRecommendation

Step 1: Term Frequency (TF)
Term Frequency also known as TF measures the number of times a term (word) occurs in a document. Given below are the terms and their frequency on each of the document.

TF for Document 1

Document1	the	game	of	life	is	a	everlasting	learning
Term Frequency	1	2	2	1	1	1	1	1
TF for Document 2

Document2	the	unexamined	life	is	not	worth	living
Term Frequency	1	1	1	1	1	1	1
TF for Document 3

Document3	never	stop	learning
Term Frequency	1	1	1
In reality each document will be of different size. On a large document the frequency of the terms will be much higher than the smaller ones. Hence we need to normalize the document based on its size. A simple trick is to divide the term frequency by the total number of terms. For example in Document 1 the term game occurs two times. The total number of terms in the document is 10. Hence the normalized term frequency is 2 / 10 = 0.2. Given below are the normalized term frequency for all the documents.

Normalized TF for Document 1

Document1	the	game	of	life	is	a	everlasting	learning
Normalized TF	0.1	0.2	0.2	0.1	0.1	0.1	0.1	0.1
Normalized TF for Document 2

Document2	the	unexamined	life	is	not	worth	living
Normalized TF	0.142857	0.142857	0.142857	0.142857	0.142857	0.142857	0.142857
Normalized TF for Document 3

Document3	never	stop	learning
Normalized TF	0.333333	0.333333	0.333333

Given below is the code in python which i used for  normalized TF calculation.

          def termFrequency(term, document):
             normalizeDocument = document.lower().split()
             return normalizeDocument.count(term.lower()) / float(len(normalizeDocument))
 
