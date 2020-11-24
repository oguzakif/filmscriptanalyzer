from operator import itemgetter
import matplotlib.pyplot as plt 
import os.path

FILE_NAME1 = ''
FILE_NAME2 = ''

stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 
            'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 
            'such', 'into', 'of', 'most', 'itself', 'other', 'off','is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 
            'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor',
            'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both','ext',
            'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been',
            'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 
            'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just','e',"don't","doesn't",'int',
            'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom','his',"he's","she's",'him',"it's",'the'
            , 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than',"i'm",'is']

punctiations = [',','.','?',':',';','-','!','(',')','/','>','<']
#TAKING INPUT FROM USER
def userinput(FILE_NAME1,FILE_NAME2):
    numofscript = 0
    while(numofscript != 1 and numofscript !=2):
        print('How many files do you want to enter?')
        numofscript = int(input('1 or 2 '))
        if numofscript == 2:
           
            FILE_NAME1 = input('Please enter the first file name with extension.  ')
            while(not(os.path.isfile(FILE_NAME1))):
                FILE_NAME1 = input('File doesnt exist please try again.  ')
                
            FILE_NAME2 = input('Please enter the second file name with extension.  ')
            while(not(os.path.isfile(FILE_NAME2))):
                FILE_NAME2 = input('File doesnt exist please try again.  ')

        elif numofscript ==1:
            FILE_NAME1 = input('Please enter the first file name with extension.  ')
            while(not(os.path.isfile(FILE_NAME1))):
                FILE_NAME1 = input('File doesnt exist please try again.  ')
        else:
            print('Invalid file number please enter file number between 1-2.  ')

    return FILE_NAME1,FILE_NAME2,numofscript
#COUNTING AND SORTING WORDS
def countwords(text,text2):
    freq_list = []
    words_list= []
    words2_list = []
    freq2_list = [] 
    freqtot_list = []
    intersect = set(text).intersection(set(text2))
    intersect = list(intersect)
    #IF THERE IS ONE FILE
    if (text2 ==''):
        for word in text:
            if word not in words_list:
                words_list.append(word)
                freq_list.append(text.count(word))
        #SORT THE LIST ACCORDING TO FIRST INDEX OF ZIPPED LIST
        sorted_list = sorted(zip(words_list, freq_list), key=itemgetter(1), reverse=True)    
        
        for i in range(len(sorted_list)):
            words_list[i] = sorted_list[i][0]
            freq_list[i] = sorted_list[i][1]
        
        return words_list,freq_list
    #IF THERE IS TWO FILE
    else:
        for word in intersect:
            for i in text:
                if word == i and word not in words_list:
                    words_list.append(word)
                    freq_list.append(text.count(word))
                    freqtot_list.append(text.count(word)+text2.count(word))

            for j in text2:
                if word == j and word not in words2_list:
                   words2_list.append(word)
                   freq2_list.append(text2.count(word))
        #SORT THE LIST ACCORDING TO SECOND INDEX OF ZIPPED LIST(FREQTOT)
        sorted_list = sorted(zip(words_list, freq_list,freqtot_list), key=itemgetter(2), reverse=True)  
        for i in range(len(sorted_list)):
            words_list[i] = sorted_list[i][0]
            freq_list[i] = sorted_list[i][1]
        #SORT THE LIST ACCORDING TO SECOND INDEX OF ZIPPED LIST(FREQTOT)
        sorted2_list = sorted(zip(words2_list,freq2_list,freqtot_list),key=itemgetter(2), reverse=True)
        for i in range(len(sorted2_list)):
            words2_list[i] = sorted2_list[i][0]
            freq2_list[i] = sorted2_list[i][1]

        return words_list,freq_list,words2_list,freq2_list
#READING FILE
def readingfile(file1,file2,filenum):
            f1 = open(file1,"r")
            script1 = f1.read()
            script1 = script1.lower()
            f1.close
            if filenum ==2:    
                f2 = open(file2,"r")
                script2 = f2.read()
                script2 = script2.lower()
                f2.close
                return script1,script2

            return script1
        
#CLEANING PUNCTUATIONS
def cleanpunctuations(text,text2):
    for i in range(len(text)):
        for j in range(len(punctiations)):
            if (i>=len(text)):
                break
            elif (text[i] == punctiations[j]): 
               text = text.replace(punctiations[j],'')
    
    text = text.split()
    if not(text2 == ''):
        for i in range(len(text2)):
            for j in range(len(punctiations)):
                if (i>=len(text2)):
                    break
                elif (text2[i] == punctiations[j]): 
                    text2 = text2.replace(punctiations[j],'')
        
        text2=text2.split()
        return text,text2
    
    return text

#CLEANING STOPWORDS
def cleanstopwords(text):
    return [w for w in text if w not in stopwords]
    

def main():
    text2=''
    wordsnum= 20
    axisofbarchart = []
    file1,file2,filenum = userinput(FILE_NAME1,FILE_NAME2)
    decision =''
    #LIMIT OF THE FREQUENCY BOARD
    while(decision != 'y' and decision !='n'):
        decision = (input('Do you want to change your limit(20) of frequency board? y or n '))
        if decision == 'y':
            wordsnum =int(input('How much words do you want to see on the board? '))  
    for i in range(wordsnum):
        axisofbarchart.append(i+1)
    
    #IF THERE IS TWO FILE
    if filenum == 2:
        text,text2 = readingfile(file1,file2,filenum)
        wordswstops,wordswstops2 = cleanpunctuations(text,text2)
        words = cleanstopwords(wordswstops)
        words2 = cleanstopwords(wordswstops2)
        words_list,freq_list,words2_list,freq2_list = countwords(words,words2)
        
        words_list = words_list[0:wordsnum]
        freq_list = freq_list[0:wordsnum]
        words2_list = words2_list[0:wordsnum]
        freq2_list = freq2_list[0:wordsnum]
        freq_tot = []
        for i in range(len(freq_list)):
            freq_tot.append(freq2_list[i]+freq_list[i])
        print ('{:<4} {:<10} {:<10} {:<10} {:<10}'.format('NO','WORD','FREQUENCY1','FREQUENCY2','FREQUENCY TOTAL'))
        for i in range(wordsnum):
            print ('{:<4} {:<10} {:<10} {:<10} {:<10}'.format(i+1,words_list[i],freq_list[i],freq2_list[i],freq_tot[i]))
         
        #PRINTING BARCHART
        #FREQ1
        plt.bar(axisofbarchart,freq_list,align='center')
        plt.xticks(axisofbarchart,words_list)
        plt.show()
        #FREQ2
        plt.bar(axisofbarchart,freq2_list,align='center')
        plt.xticks(axisofbarchart,words2_list)
        plt.show()
        #FREQTOT
        plt.bar(axisofbarchart,freq_tot,align='center')
        plt.xticks(axisofbarchart,words_list)
        plt.show()
        
    #IF THERE IS ONE FILE
    elif filenum == 1:
        text = readingfile(file1,file2,filenum)
        wordswstops = cleanpunctuations(text,text2)
        words = cleanstopwords(wordswstops)
        words_list,freq_list = countwords(words,text2)
        
        words_list = words_list[0:wordsnum]
        freq_list = freq_list[0:wordsnum]
        
        print ('{:<4} {:<10} {:<8}'.format('NO','WORD','FREQUENCY'))
    
        for i in range(wordsnum):
            print ('{:<4} {:<10} {:<8}'.format(i+1,words_list[i],freq_list[i]))

        #PRINTING BARCHART
        plt.bar(axisofbarchart,freq_list,align='center')
        plt.xticks(axisofbarchart,words_list)
        plt.show()
   
main()