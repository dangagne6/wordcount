from django.http import HttpResponse
from django.shortcuts import render
import operator


def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    word_list = fulltext.split(" ")

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            #Increase
            word_dictionary[word] +=1

        else:
            #Add to dictionary
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items())

    return render(request, 'count.html',{'fulltext': fulltext, 'count': len(word_list), 'sorted_words': sorted_words})