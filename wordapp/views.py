from django.shortcuts import render
import re 

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):

    full_text=request.GET['fulltext']
    word_lis=re.split('[?!.]',full_text)
        
        
    word_list=full_text.split()
    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            word_dictionarty[word] +=1
        else:
            word_dictionary[word]=1
    dicts = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)
    word_dictionary = dict(dicts)
            
    return render(request,'count.html',{"fulltext":full_text,'total':len(word_list),'dictionary':word_dictionary.items(),'word_lis':word_lis})

    