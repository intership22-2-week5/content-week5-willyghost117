"""Posts views"""
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
# Create your views here.

posts = [
    {
    'title' : 'Mont blac',
    'user' :{
        'name':'Yesica Cortés',
        'picture' : 'https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U'
            } ,
    'timestamp':datetime.now().strftime('%b %dth, %Y -%H:%M hrs'),
    'photo': 'https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U'
    },
    {
    'title' : 'Mount',
    'user' :{
        'name':'Yulissa Cortés',
        'picture' : 'https://i.picsum.photos/id/866/200/300.jpg?hmac=rcadCENKh4rD6MAp6V_ma-AyWv641M4iiOpe1RyFHeI'
            } ,
    'timestamp':datetime.now().strftime('%b %dth, %Y -%H:%M hrs'),
    'photo': 'https://i.picsum.photos/id/866/200/300.jpg?hmac=rcadCENKh4rD6MAp6V_ma-AyWv641M4iiOpe1RyFHeI'
    },
        {
    'title' : 'Freezer',
    'user' :{
        'name':'Marìa Cortés',
        'picture' : 'https://i.picsum.photos/id/620/200/300.jpg?grayscale&hmac=YeHYQiHXe-_XZSomLBWOju6HQi3QJ2Clm09NyL6YkiY'
            } ,
    'timestamp':datetime.now().strftime('%b %dth, %Y -%H:%M hrs'),
    'photo': 'https://i.picsum.photos/id/620/200/300.jpg?grayscale&hmac=YeHYQiHXe-_XZSomLBWOju6HQi3QJ2Clm09NyL6YkiY'
    }
]

def list_posts(request):

    return render(request, 'feed.html',{'posts':posts})

    #"""
    #content = []
    #for post in posts:
        #content.append("""
        #<p><strong> {name}</strong> </p>
        #<p><small> {user} - <i> {timestamp}</i> </small> </p>
        #<figure> <img src ="{picture}"/> </figure>
        #""".format(**post))
    #return HttpResponse('<br>'.join(content))

