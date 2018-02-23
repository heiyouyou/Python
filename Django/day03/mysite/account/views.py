from django.shortcuts import render

# Create your views here.

def test(request):
	data = {
		'name':"account is page"
	}
	return render(request,'account/index.html',context=data)

def detail(request,question_id):
	return render(request,'account/detail.html',context={"message":'this is a detail page...',"question_id":question_id})
