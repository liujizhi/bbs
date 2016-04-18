from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from models import BBS,Category,BBS_user
from django.contrib import auth
from django_comments.models import Comment
from django.contrib.auth.models import User
import hashlib
# Create your views here.

def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    if user is not None: 
        auth.login(request,user)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})
    

def logout_view(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/'>Re-login</a>" % user)


def Login(request):
    return render_to_response('login.html')
def register(request):

    if request.method=='GET':
        return render_to_response('register.html')
    elif request.method=='POST':
        username=request.POST['username']
        # password= hashlib.sha1(request.POST['password']).hexdigest()  
        password=request.POST['password']
        # print '==>',password
        user=User.objects.create_user(username=username,password=password)
        user.save()
        return HttpResponseRedirect('/login/')






# def index(request):
# 	bbs_list=BBS.objects.all()
#     # bbs_categories=Category.objects.all()
#     return render_to_response('index.html',{
#                                             'bbs_list':bbs_list,
#                                             'user':request.user,
#                                            })

def index(request):
    bbs_list=BBS.objects.all()
    bbs_categories=Category.objects.all()
    return render_to_response('index.html',{'bbs_list':bbs_list,'user':request.user,'bbs_categories':bbs_categories,'cate_id':0})


def category(request,cate_id):
    bbs_list=BBS.objects.filter(category_id=cate_id)
    bbs_categories=Category.objects.all()
    return render_to_response('index.html',{'bbs_list':bbs_list,'user':request.user,'bbs_categories':bbs_categories,'cate_id':int(cate_id)})


def bbs_detail(request,bbs_id):
	bbs=BBS.objects.get(id=bbs_id)
	return render_to_response('bbs_detail.html',{'bbs_obj':bbs,'user':request.user})



def sub_comment(request):
	bbs_id=request.POST['bbs_id']
	
	comment=request.POST['comment_content']
	Comment.objects.create(
        content_type_id=10,
        object_pk=bbs_id,
        site_id=1,
        user=request.user,
        comment=comment
		)
	return HttpResponseRedirect('/detail/%s' % bbs_id)
def bbs_pub(request):
    return render_to_response('bbs_pub.html',{'user':request.user})
def bbs_sub(request): 
    content=request.POST.get('content')
    author=BBS_user.objects.get(user=request.user)
    BBS.objects.create(
    title='TEXT TITLE',
    summary='HAHA',
    content=content,
    author=author,
    view_count=1,
    ranking=1,
        )
    return HttpResponse('yes.')
