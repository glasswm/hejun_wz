# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render, render_to_response


# Create your views here.
from infor.models import StudentForm


def index(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(u'添加成功')
            # Do something.
    else:
        form = StudentForm()
    return render(request, "index.html", {
        "form": form,
    })