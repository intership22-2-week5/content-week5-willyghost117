from email import message
from django.http import HttpResponse

from datetime import datetime
import json

def time(request):
    
    return HttpResponse('hi! Current server time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))
    
def sorted_function (request):
    """hi"""
    
    numbers =[int(i)for i in  request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers' : sorted_ints,
        'message' : 'Ingers sorted successfully.'
    }

    import pdb; pdb.set_trace()
    return HttpResponse(json.dumps(data, indent = 4),content_type = "application/json")

def say_hi (request, name, age):
    """Return a greeetin"""
    if age < 12:
        message= 'Sorry {}, your are not allowed here'.format(name)

    else: 
        message= 'Welcome {}, your  session es ok'.format(name)

    return HttpResponse(message)
