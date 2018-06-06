import nltk 
from nltk.corpus import wordnet as wn 

def score_generator(sentence1,sentence2):
	token1=nltk.word_tokenize(sentence1)
	token2=nltk.word_tokenize(sentence2)
	score=0.0
	for word1 in token1: 
		for word2 in token2: 
		 	extract1=wn.synsets(word1)
		 	extract2=wn.synsets(word2)
		 	if extract1 and extract2: 
				    try:
		 			res= str(extract1[0].wup_similarity(extract2[0]))
					raise NameError('Error')
				    except NameError:
					if res =='None':
							score=score+0
			    		else: 
							score=score+float(res) 

	return score

file=open('Corpus-Collection/text4.txt','r')
txt=file.read()
txt=txt.split(".")
print len(txt)
costarray=['None'] * len(txt)
costarray[0]='0'
cost=[[0 for x in range(len(txt))]for y in range(len(txt))]
i,j=0,0;
index,maxcost =0,0.0;
tokencounter=0
while tokencounter<int((len(txt)-1)/2):
	while j<len(txt)-1:
		if cost[j][i]== 0 and i!=j: 
			cost[i][j]= score_generator(txt[i],txt[j])
			#print i
			#print j
			#print cost[i][j]
			#print maxcost
			if float(cost[i][j])>=float(maxcost):
				if j not in costarray:				
					maxcost=float(cost[i][j])
					index=int(j) 
					#print index
			else: 
				cost[i][j]=cost[j][i]
		j=int(j)+1
	costarray[index]=index
	tokencounter=tokencounter+1
	i=index 
	j=0
	maxcost=0
i=0
while i <len(txt):
	  if costarray[i]!='None':
			print txt[i]
	  i=i+1

