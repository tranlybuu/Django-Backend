from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("question/", views.viewListQuestion, name="view_list_question"),
    path("detail/<int:question_id>", views.viewDetailQuestion, name="view_detail_question"),
    path('<int:question_id>', views.vote, name="vote"),
]
