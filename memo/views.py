from django.shortcuts import render
from django.views.generic import ListView, DetailView
from memo.models import Memo


class MemoList(ListView):
    model = Memo

class MemoDetail(DetailView):
    model = Memo


