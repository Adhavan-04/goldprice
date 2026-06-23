from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from .models import GoldPrice
# Create your views here.
def index(request):
    return render(request,"index.html")


def register(request):
    if request.method=="POST":
        first=request.POST['fname']
        last=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        psw=request.POST['psw']
        psw1=request.POST['psw1']
        if psw==psw1:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exists")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(first_name=first,
                last_name=last,email=email,username=uname,password=psw)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return render(request,"register.html")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST['uname']
        psw=request.POST['psw']
        user=auth.authenticate(username=username,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('data')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    return render(request,"login.html")

def data(request):
    if request.method=="POST":
        spx=float(request.POST['spx'])
        uso=float(request.POST['uso'])
        slv=float(request.POST['slv'])
        eur=float(request.POST['eur'])
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sqlalchemy import create_engine
        from sqlalchemy.engine import URL
        #import pypyodbc as odbc

        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestRegressor
        from sklearn import metrics
        gold_data = pd.read_csv("static/gld_price_data.csv")
        print(gold_data.head())
        print(gold_data.tail())
        print(gold_data.shape)
        print(gold_data.info())
        print(gold_data.isnull().sum())
        print(gold_data.describe())
        sns.distplot(gold_data['GLD'],color='green')
        plt.show()
        X= gold_data.drop(['Date','GLD'],axis=1)
        Y= gold_data['GLD']
        regressor = RandomForestRegressor(n_estimators=100)
        regressor.fit(X,Y)
        import numpy as np
        data=np.array([[spx,uso,slv,eur]],dtype=object)
        pred_price=regressor.predict(data)
        print(pred_price)
        gold=GoldPrice.objects.create(SPX=spx,USO=uso,
        SLV=slv,EUR_USD=eur,GOLD=pred_price)
        gold.save()
        return render(request,"predict.html",{"spx":spx,"uso":uso,"slv":slv,
        "eur":eur,"price":pred_price})
    return render(request,"data.html")

def predict(request):
    return render(request,"predict.html")

def logout(request):
    auth.logout(request)
    return redirect('/')