import string, os
import csv
from collections import Counter
 
class WordCounter:
    def __init__(self,filename):
        self.filename = filename
        self.f = open(self.filename,'r+')
        
    def removepunctuation(self) :
        text = self.f.readlines()
        self.f.close()
        exclude = set(string.punctuation)
        op_file_path = str(self.filename)
        if os.path.isfile(op_file_path):
            os.remove(op_file_path) 
        for x in xrange(0,len(text)):
            s = text[x]
            s = s.replace('-', ' ')
            s1 = ''.join(ch for ch in s if ch not in exclude)
            op_file = open(op_file_path, 'a')
            op_file.write(s1)
            op_file.close()
        return op_file_path
            
    def findcount(self):
        word_count = Counter()
        with open(self.filename, 'r') as f:
            for line in f:
                for word in line.split(" "):
                    word_count[word.strip().lower()] += 1
            self.countdict ={}
        for word, count in word_count.iteritems():
            if word != '':
                self.countdict.update({word:count})
            #print "word: {}, count: {}".format(word, count)
        #print self.countdict
 
    def writecountfile(self,csvfilename):
        f = open(csvfilename,'wb')
        writer = csv.writer(open(csvfilename, 'wb'))
        for key, value in self.countdict.items():
            writer.writerow([key, value])
        f.close()
        
read1 = WordCounter('red-headed-league.txt')
read1.removepunctuation()
read1.findcount()
read1.writecountfile('countdict.csv')