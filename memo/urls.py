from django.urls import path
from memo.views import MemoList, MemoDetail


app_name = 'memo'
urlpatterns =[
    path('', MemoList.as_view(), name='index'),
    path('<int:pk>/memo',MemoDetail.as_view(), name='detail'),
]