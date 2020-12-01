from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import datetime
from pytz import timezone

def index(request):
	fmt = "%Y-%m-%d %H:%M %p"
	now_time = datetime.now(timezone('US/Eastern'))
	context = {
		"time": now_time.strftime(fmt)
	}
	return render(request,'index.html', context)

def time_display(request):
	return HttpResponseRedirect("/")
