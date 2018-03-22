from django.shortcuts import render
import sys
from kgqa.KB_query import query_main

# Create your views here.

def search_post(request):
    ctx = {}
    if request.POST:
        question = request.POST['q']
        ctx['rlt'] = query_main.query_function(question)
        print(ctx['rlt'])
    return render(request, "post.html", ctx)
