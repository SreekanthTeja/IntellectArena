from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import pandas as pd
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST' and request.is_ajax():
        form = SignUpForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("error")

    form = SignUpForm()
    return render(request, 'auth/register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return HttpResponse(f'<h3 class="center">Welcome {user.username}</h3>')

        return HttpResponse("error")
    form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, " You have succesfully logged out")
    return redirect('signin')


def store_date(request):
    df = pd.read_csv('out1 django.csv')
    date = df["date"]
    if StoreDateColumn.objects.all():
        return HttpResponse('Already had this specific data in database')
    else:
        print(True)
        list_date = [StoreDateColumn(date=i) for i in date]
        sd = StoreDateColumn.objects.bulk_create(list_date)
    return HttpResponse("Successfully uploaded")


class AppointmentView(generics.CreateAPIView):
    serializer_class = AppointmentSerializers
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(participent=self.request.user)
