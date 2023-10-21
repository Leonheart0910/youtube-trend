from django.shortcuts import render

from django.shortcuts import render, HttpResponse
import random
topics = [
    {'id' : 1, 'title':'mogolia', 'body':'mongolsex'},
    {'id' : 2, 'title':'Korea', 'body':'kimchi sex'},
    {'id' : 3, 'title':'japnan', 'body':'mother fucking sex'}
]
def HTMLTemplate():
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
        <html>
            <head>

            </head>
            <body>
                <h1>유튜브 트렌드</h1>
                <ol>
                    {ol}
                </ol>
            </body>
        </html>
        '''
def index(request):
    return HttpResponse(HTMLTemplate())

def create(request):
    return HttpResponse("creat")

def read(request, id):
    return HttpResponse("read" + id)
