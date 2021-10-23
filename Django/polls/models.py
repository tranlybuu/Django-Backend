from django.db import models

# Create your models here.

class Question(models.Model):   # Class câu hỏi
    question_text = models.CharField(max_length=200)    # Câu hỏi
    time_public = models.DateTimeField()                # Ngày giờ

class Choice(models.Model):     # Class câu trả lời
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # Liên với câu hỏi, on_delete là nếu câu hỏi xóa thì câu trả lời cũng xóa
    choice_text = models.CharField(max_length=100)                      # Câu trả lời
    vote = models.IntegerField(default=0)                               # Số lượng trả lời cho từng đáp án, mặc định ban đầu là 0