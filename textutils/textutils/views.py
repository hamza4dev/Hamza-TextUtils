from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ex1(request):
    s='''<h2> Navigation Bar <br> </h2>
    <a href= "https://play.google.com/" > Apps </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a>'''
    return HttpResponse(s)

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    #Check Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')


    # Check if removepunc checkbox is on
    if removepunc == "on":
        # Remove punctuation from djtext
        punctuation = '''!()-[]{};:'\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    # Check if fullcaps checkbox is on
    if fullcaps == "on":
        analyzed =""
        # Convert djtext to uppercase
        for char in djtext:
          analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if newlineremover =="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="/r":
              analyzed = analyzed + char
            params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
            djtext=analyzed

        #return render(request, 'analyze.html', params)


    if extraspaceremover =="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index]=="" and djtext[index +1]=="":
                pass
            else:
               analyzed = analyzed + char
            params = {'purpose': 'Remove line space', 'analyzed_text': analyzed}
            djtext = analyzed
        #return render(request, 'analyze.html', params)


    if charcounter == "on":
        analyzed =""

        for char in djtext:
          analyzed = len(djtext)
        params = {'purpose': 'Count the Character', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)


    return render (request, 'analyze.html', params)



# def capfirst(request):
#     return HttpResponse ("captitalization first")
# def newlineremove(request):
#     return HttpResponse ( "new line remove")
# def spaceremove(request):
#     return HttpResponse ("space remove")
# def charcount(request):
#     return HttpResponse ("character count")
