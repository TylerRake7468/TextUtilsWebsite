#i have created this file.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, "index.html")

def analyzer(request):
	djtext = request.POST.get('text', 'default')
	analyze_type1 = request.POST.get('action_punc','off')
	analyze_type2 = request.POST.get('action_full_cap','off')
	analyze_type3 = request.POST.get('action_new_line_remove','off')

	if analyze_type1=="on":
		analyzed_text = ""
		punc_list = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
		for char in djtext:
			if char not in punc_list:
				analyzed_text = analyzed_text + char
		params = {'purpose':'Punctuation', 'analyzed_text': analyzed_text}
		djtext = analyzed_text
		# return render(request, "analyze.html", params)
	if analyze_type2=="on":
		analyzed_text = ""
		for char in djtext:
			analyzed_text = analyzed_text + char.upper()
		params = {'purpose':'Uppercase convert', 'analyzed_text': analyzed_text}
		djtext = analyzed_text
		# return render(request, "analyze.html", params)
	if analyze_type3=="on":
		analyzed_text = ""
		for char in djtext:
			if char != "\n" and char !="\r":
				analyzed_text = analyzed_text + char
		params = {'purpose':'New Line remover', 'analyzed_text': analyzed_text}
		# return render(request, "analyze.html", params)

	if analyze_type1!="on" and analyze_type2!="on" and analyze_type3!="on":
		return HttpResponse("Please select checkbox. Error")
	else:
		return render(request, "analyze.html",params)

def about(request):
	return render(request, "about.html")

