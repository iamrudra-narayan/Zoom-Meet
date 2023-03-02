from django.shortcuts import render, redirect
from time import time
from .zoom import createMeeting
from user.models import RecordedCall

# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            meeting = createMeeting() 
            join_url = meeting['join_url']
            password = meeting['password']
            meet_id = meeting['id'] 
            datetime = meeting['start_time']
            duration = meeting['duration']
            #file_name = 'video'
            print(meet_id,  datetime,  duration)
            data = RecordedCall(user = request.user, meeting_id = meet_id, date_time = datetime, duration = duration )
            data.save()

        else:
            return redirect('/myaccount/login/')     
        
    return render(request, 'home.html')