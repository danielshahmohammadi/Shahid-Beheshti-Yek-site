from django.shortcuts import render
# from django.http import HttpResponse as HR

# 1
def home(request):
    menu = [
        {
            "title":"درباره ما",
            "url_name":"about",
        },
        {
            "title":"گالری تصاویر",
            "url_name":"gallerylist",
        },
        {
            "title":"تماس با ما",
            "url_name":"contanct_use",
        },
        {
            "title":"اخبار",
            "url_name":"newslist",
        },
        {
            "title":"ورود کاربر",
            "url_name":"login",
        },
        {
            "title":"افتخارات مدرسه",
            "url_name":"honnors",
        },
        {
            "title":"کارکنان مدرسه",
            "url_name":"school_staff",
        },
        {
            "title":"وبلاگ",
            "url_name":"weblog",
        },

        {
            "title":"امکانات",
            "url_name":"facilitys",
        }
        
    ]
    return render(request,'pages/index.html',{"menu":menu})

# 2
def about(request):
    return render (request,"pages/about.html")
# درباره ما 

# 3
def gallerylist(request):
    return render (request,'pages/gallerylist.html')
# اخبار 

# 4
def contanct_use (request):
    return render (request ,"pages/contanct_use.html")
# تماس با ما

# 5
def newslist(request):
    return render (request,"pages/newslist.html")
# اخبار

# 6
def login(request):
    return render (request,"pages/login.html")
# ورود کاربر

# 7
def dashboard(request): 
    return render (request,"pages/dashboard.html")
# پنل کاربری

# 8
def studentview (request):
    return render (request ,"pages/studentview.html")
# مشخصات دانش آموز

# 9
def lessons (request):
    return render (request ,"pages/dars_dorehlist.html")
# دروس ارائه شده

# 10
def gheybat_list(request):
    return render (request,"pages/gheybat_list.html")
# غیبت ها و تاخیر ها


# 11
def gradelist (request):
    return render (request ,"pages/gradelist.html")
# نمرات کلاسی

# 12
def wekkly_program (request):
    return render (request ,"pages/programweek.html")
# برنامه هفتگی

# 13
def st_darslist (request):
    return render (request ,"pages/st_darslist..html")
# کارنامه دانش آموز


# 14
def changepwd (request):
    return render (request ,"pages/changepwd.html")
# تفییر رمز عبور

# 15
def honnors (request):
    return render (request ,"pages/honnors.html")
# افتخارات مدرسه


# 16
def school_staff (request):
    return render (request ,"pages/chool_staff.html")
# کارکنان مدرسه

# 17
def facilitys(request):
    return render (request,"pages/facilitys.html")
# امکانات

# 18
def weblog (request):
    return render (request ,"pages/weblog.html")
# وبلاگ

# 19
def pishnahadatlis(request):
    return render (request,"pages/pishnahadatlist.html")
# صندوق پیشنهادات

# 20
def majors(request):
    return render (request,"pages/majors.html")
















# def home(request):
#     return HR ("Page One")

# def Admin(request):
#     return HR ("Admin Panel")

# def Teacher(request):
#     return HR ("Teachers Panel")

# def Student(request):
#     return HR ("Students Panel")

# def Manager(request):
#     return HR ("School's Manager Panel")

# def Grades(request):
#     return HR ("Your grade is :",2+2)

# def Books(request):
#     return HR ("Dini")

# def Call(request):
#     return HR ("Call us : 0243333427")
