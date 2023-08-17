from django.shortcuts import render,redirect

# Create your views here.
from .models import Contact
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home(request):
    return render(request,"home.html")

@login_required
def addcontact(request):
   try:   
        Name=request.POST['name']
        nme=Contact.objects.filter(Name=Name)
        if nme.exists():
         return render(request,"home.html",{"msg":"contact already exists"})
        else:
         Name=request.POST['name']
         Phoneno=request.POST['mobno']
         contactlist=Contact(Name=Name,phoneno=Phoneno)
         contactlist.save()
         return render(request,"home.html",{"msg":"contact added"})
   except Exception as e:
     print(e)
     return render(request,"home.html",{"msg":"contact not added"})
   
def display(request):
   contactdtls=Contact.objects.all()
   return render(request,"home.html",{"cnt":contactdtls})

@login_required
def dltcontact(request):
   Name=request.POST['oldname']
   contactdtls=Contact.objects.filter(Name=Name)
   if contactdtls.exists():
    contactdtls.delete()
    return render(request,"home.html",{"msg2":"the specified contact deleted!!"})
   else:
    return render(request,"home.html",{"msg2":"there is no such contact!!"})
   
@login_required
def search(request):
    Nme=request.POST['sname'] 
    contactdtls=Contact.objects.filter(Name=Nme)
    if contactdtls.exists():
        return render(request,"home.html",{"cnts":contactdtls})
    else:
        return render(request,"home.html",{"msg6":"there is no such contact!!"})


# def updatecontact(request):
#    try:
#       oldname=request.POST["oldname"]
#       newname=request.POST["newname"]
     
      
#       cnt=Contact.objects.filter(Name=oldname)
     
      
#       if cnt.exists():
#        cnt.update(Name=newname)
#        return render(request,"home.html",{'msg1':"updated"})
      
#       elif cnt==newname:
#          return render(request,"home.html",{"msg1":"contact already exists"})
#       else:
#          return render(request,"home.html",{'msg1':"no records found"})
      
#    except Exception as e:
#       print(e)
#       return render(request,"home.html",{'msg1':"not updated"})
# 
# 
@login_required
def updatecontact(request):
 
 
  oldname=request.POST['oldname']
  newname=request.POST['newname']
  contactList=Contact.objects.filter(Name=oldname)
  if contactList.exists():
         for i in contactList:
            if newname in i.Name:
	                return render(request,"home.html",{"msg1":"contact not exists"})
            # elif newname in i.Name:
            #   contactList.update(Name=newname)
            #   return render(request,"home.html",{'msg1':"updated"})
         
        
    
@login_required   
def updatecontactno(request):
 
 
  oldname=request.POST['oldname']
  Newno=request.POST['newno']
  contactList=Contact.objects.filter(Name=oldname)
  if contactList.exists():
       contactList.update(phoneno=Newno)
       return render(request,"home.html",{'msg4':"updated"})
   
  else:
     return render(request,"home.html",{"msg4":"there is no such contact"})  
	      
       
    #  elif oldname!=i.Name:
    #    return render(request,"home.html",{"msg1":"no records found"})
     


# @login_required
# def home(request):
#     return render(request,"home.html")

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"Invalid login"})
    
def logout_view(request):
    logout(request)
    return redirect('login')

def resethome(request):
   return render(request,'resetpassword.html')

def resetpassword(request):
     responseDic={}
     uname=request.POST['username']
     newpwd=request.POST['password']
 
     try:
       
        user=User.objects.get(username=uname)
        if user is not None:
             user.set_password(newpwd)
             user.save()
             responseDic['errmsg']="password set successfully"
             return render(request,"resetpassword.html",responseDic)
    
     except Exception as e:
          print(e)
          responseDic['errmsg']="password reset failed.."
          return render(request,"resetpassword.html",responseDic)
     
     
          
  







	


  
   


