from summa import summarizer
file=open('text4.txt','r')
text=file.read()
print summarizer.summarize(text,ratio=0.5)
