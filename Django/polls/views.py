from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Choice, Question

# Create your views here.
def index(request):
    Name = "Trần Lý Bửu"
    E_device = ["Điện thoại", "Laptop", "Pc", "hello"]
    context = {"name": Name, "device": E_device}
    return render(request, "polls/index.html", context)

def viewListQuestion(request):
    list_question = Question.objects.all()      # get_object_or_404(Question,pk =1)
    context = {"question": list_question}
    return render(request, "polls/listQuestion.html", context)

def viewDetailQuestion(request, question_id):
    q = Question.objects.get(pk=question_id)
    context = {"detail_question": q}
    return render(request, "polls/detailQuestion.html", context)

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
        c.vote = c.vote + 1
        c.save()
    except:
        return HttpResponse("Lỗi")
    return render(request, "polls/result.html", {"question": q})