from django.conf.urls import url

from . import views

app_name = 'questApp'
urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # Список всех вопросов
    url(r'^questions/$', views.questions, name='questions'),
    # Страница с ответами на вопрос
    url(r'^questions/(?P<question_id>[0-9]+)$', views.answers, name='answers'),
    # Страница для добавления нового вопроса
    url(r'^new_question/$', views.new_question, name='new_question'),
    # Страница для добавления нового ответа
    url(r'^new_answer/(?P<question_id>[0-9]+)/$', views.new_answer, name='new_answer'),
    # Страница для редактирования поста
    url(r'^edit_answer/(?P<answer_id>[0-9]+)/$', views.edit_answer, name='edit_answer'),
    # Страница для редактирования вопроса
    url(r'^edit_question/(?P<question_id>[0-9]+)/$', views.edit_question, name='edit_question')

]
