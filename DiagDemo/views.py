from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


def hello(request):
    return HttpResponse("Hello world")

# decode the question and return the answer
def decode(ask):
    ans = 'I don\'t know.'
    return ans


def diag_form(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            ask = request.GET['q']
            # decode dialog .......
            ans = decode(ask)

            return render_to_response('ans_form.html', locals())
    return render_to_response('diag_form.html', {'error': error})
