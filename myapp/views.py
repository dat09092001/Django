from django.shortcuts import redirect,render,get_object_or_404
from .models import sinhvien,khoa,school,comment
from .form import sinhvienFrom,sinhvienForm1,formlogin,commentsfrom
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url="login")
def home(request):
    if 'q' in request.GET:
        nametk=request.GET['q']
        sv=sinhvien.objects.filter(tensv__icontains=nametk)
        if len(sv)==0:
            sv=sinhvien.objects.all()

    else:
        sv=sinhvien.objects.all()
    k=khoa.objects.all()
    t=school.objects.all()
    male=sinhvien.objects.filter(gender__icontains="m")
    female=sinhvien.objects.filter(gender__icontains='f')
    if request.method=="POST":
        form1=commentsfrom(request.POST)
        if form1.is_valid():
            comment.objects.create(user=request.user,text=request.POST["text"]).save()
            return redirect("/")
            
            
    else:
        form1=commentsfrom()
    list_comment=comment.objects.all()
    print(list_comment)
    context={'sv':sv,"male":male,'female':female,"k":k,'t':t,"cm":list_comment,"form1":form1}
    return render(request,"home.html",context)
@login_required(login_url="login")
def viewsv(request,sinhvien_id):
    viewsinhvien=sinhvien.objects.get(id=sinhvien_id)
    return render(request,"view.html",{'viewsv':viewsinhvien})
def deletesv(request,id):
    delete=sinhvien.objects.get(id=id)
    delete.delete()
    return redirect('home')
def addsinhvien(request):
    
    # mak=request.POST["mak"]
    # tenk=request.POST["tenk"]
    # print(mak,tenk)
    # khoa1=khoa.objects.create(mak=mak,tenk=tenk)
    # if khoa1.save():
    #     return redirect("home")
    mak="1"
    tenk="1"
    if request.method=="POST":
       form=sinhvienFrom(request.POST)
       if form.is_valid():
           mak=request.POST['mak']
           tenk=request.POST['tenk']
           print(mak,tenk)
           khoa.objects.create(mak=mak,tenk=tenk).save()
           return redirect("home")
    else:
        form=sinhvienFrom()
    # tenk=request.POST["tenk"]
    # print(mak,tenk)
    # khoa1=khoa.objects.create(mak=mak,tenk=tenk)
    # if khoa1.save():
    #     return redirect("home")
 

    return render(request,"addsv.html",{"form":form,"mak":[mak,tenk]})
def editsv(request,sinhvien_id):
    viewsinhvien=sinhvien.objects.get(id=sinhvien_id)
    khoa1=khoa.objects.all()
    school1=school.objects.all()
    print(khoa1,school1)
    print(viewsinhvien)
    if request.method=="POST":
        masv=request.POST["masv"]
        tensv=request.POST["masv"]
        s=request.POST.get("school")
        k=request.POST.get("khoa")
        lop=request.POST['lop']
        image=request.FILES["image"]
        gender=request.POST.get("gender")
        viewsinhvien.image=image
        viewsinhvien.gender=gender
        viewsinhvien.save()
        return redirect("home")
    return render(request,"edit.html",{'viewsv':viewsinhvien,"khoa1":khoa1,"school1":school1})
def dangki(request):
    if request.method=="POST":
       formdangki=UserCreationForm(request.POST)
       username=request.POST.get("username")
       password=request.POST.get("password")
       if formdangki.is_valid():
           user=formdangki.save()
          
           login(request,user)
           return redirect("home")
    else:
        formdangki=UserCreationForm()
    return render(request,"dangki.html",{"form":formdangki})
def login1(request):
    if request.method=="POST":
        form=formlogin(request.POST)
        username=request.POST.get("username")
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            form.add_error(None,"sai")
    else:
       form=formlogin()
    return render(request,"dangnhap.html",{"form":form})
def logout1(request):
    logout(request)
    return redirect("home")
from django.core.paginator import Paginator
from django.shortcuts import render

def my_view(request):
    items_per_page = 1
    data = khoa.objects.all()
    paginator = Paginator(data, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request,"pain.html",context)
def product(request,pk):
    sv=school.objects.get(pk=pk)
    sv1=sinhvien.objects.filter(school=sv)

    return render(request,"sinhvien.html",{"sv":sv,"sv1":sv1})
def commenta(request,id):
    list_commenet=get_object_or_404(comment,id=id)
    if request.methoad=="POST":
        form=commentsfrom(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            comment.save()
            return redirect("home")

            
                 