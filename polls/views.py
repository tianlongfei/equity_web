from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.

# version 1
# def index(request):
# 	question_list = Question.objects.order_by('-pub_date')[0:5]
# 	context = {
# 		'question_list': question_list,
# 	}
# 	template = loader.get_template('polls/index.html')

# 	return HttpResponse(template.render(context, request))

# version 2
def index(request):
	try:
		question_list = Question.objects.order_by('-pub_date')[0:5]
	except :
		raise Http404("Question does not exist")

	context = {
		'question_list': question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	context = {
		'question': question
	}
	return render(request, 'polls/detail.html', context)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)



