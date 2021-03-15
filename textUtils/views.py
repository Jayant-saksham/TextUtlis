# I have created this file - Jayant

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'jayant', 'place': 'mars'}
    return render(request, "index.html", params)


def analyze(request):
    djtext = request.GET.get('text', 'null')
    removePunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    numberremover = request.GET.get('numberremover', 'off')
    punctuations = '''!@#$%^&*~`()_'}{[]"><+/*-.,?/|\₹'''
    numbers = '''0123456789'''
    if removePunc == 'on':
        analyzedText = ""
        for i in djtext:
            if i not in punctuations:
                analyzedText += i
        djtext = analyzedText

    if fullcaps == 'on':
        analyzedText = ""
        for i in djtext:
            analyzedText += i.upper()
        djtext = analyzedText

    
    if newlineremover == 'on':
        analyzedText = ""
        for i in djtext:
            if i!='\n':
                analyzedText +=i
        djtext = analyzedText

    
    if extraspaceremover == 'on':
        analyzedText = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == ' 'and djtext[i+1] == ' '):
                analyzedText += char 
        
        djtext = analyzedText
    
    if numberremover == 'on':
        analyzedText = ""
        for i in djtext:
            if i not in numbers:
                analyzedText += i
        djtext = analyzedText
    

    if removePunc!='on' and newlineremover!='on' and extraspaceremover!='on' and fullcaps!='on' and numberremover!='on':
        return HttpResponse("Error")    

    myDictionary = {
            'purpose': "Remove punctuation",
            'analyzed_text': analyzedText,
    }
    return render(request, 'analyze.html', myDictionary)


