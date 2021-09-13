# Django-REST-2
API View Concept

Views Concept:
====  =======

1. A view is a python function or python class which takes HttpRequest as input and gives 
    HttpResponse as output.

               takes              gives
     request ---------->>  View ---------->> response


--->> A view is responsible to write the business logics

--->> We use def or class keyword to define django views.

--->> A view will interact with models.py file to manage the database.

--->> A view will interact with templates to manage presentation part.

--->> A view will also interact with urls.py file to give the mappings between urls and         views.



--->>> Generally Django supports   two types of views

1. Function Based Views   

2. Class Based Views      

---->> Function Based Views are created by  def   keyword

---->> Class Based Views    are created by  class keyword


for example,

def Function_Based_View_Name(request):
   ======
   ======
   ======

class Class_Based_View_Name(predefinedViewName):
    ======
    ======
    ======
	

Note :  To execute the views we required to create required urls in urls.py like

urls.py
=======
path('fbv/', views.Function_Based_View_Name),

path('cbv/', views.Class_Based_View_Name.as_view())  




Class Based View:-
=============

--->> in last program we were developing the Function Based Views (FBV) only.

--->> Now we are going to discuss about only Class Based Views (CBV).

--->> Every Class Based View is the Child class of "View" class.

--->> This "View" class present in django.views.generic module.

--->> If you want to create Class Based View then compulsary your class is Child class of
     "View" class.

Sysntax :

       class ClassName(View):
               pass


Differences between FBV & CBV :-
==========     ===   **********
If you are using Function Based Views , then if you want to send the GET request then one type of functionality ligics you have to do  and  if you want to send the POST request then another functionality of logics  you have to do. 


for example ,  

if request.method == "GET" :
	< do this GET activity >
 
elif request.method == POST:
	< do this POST activity >


Here  we have to check which request is comming from partner application or from the browser like GET or POST.

This type of headach is there in Function Based View . But in Class Based View there is no such type of problems.

The CBVs are very cute and easy to developing the code. Class Based Views are providing the "Code-Reusability".

for example,  if we developing the views by using Class Based Views then we  "re-use"  these views into another class also by importing the Class's


In CBV , if request is GET then get() is executed. If request is POST then post() is executed. so here the curresponding method only will be excuted directly.

example;

class ClassName(View):
	def get(self , request):
		<.... do this activity ... >

	def post(self , request):
		<.... do this activity ... >

In Class Based Views, we no need to check which type of method is coming from partner applications.

So most of the people preper the Class Based Views only in real time.In REST API , compulsary we use CBV only.




Django REST Framework  APIView  Concept:
=======   ========     =================

Django REST framework provides an APIView class, which is subclasses of Django's View class.

APIView classes are different from regular View classes in the following ways:

Requests passed to the handler methods will be REST framework's Request instances, not Django's HttpRequest instances.

Handler methods may return REST framework's Response, instead of Django's HttpResponse. 
The view will manage content negotiation and setting the correct renderer on the response.

Any APIException exceptions will be caught and mediated into appropriate responses.

Incoming requests will be authenticated and appropriate permissions  will be run before dispatching the request to the handler method.


Note:
=====
--->> Generally we are doing operations on database like Id based operations and Non_Id       based operations.
 
--->> To performing NonID and Id based operations on database then we are going to create       seperate userdefined  view classes using APIView class.

--->> To execute these view classes we are going to create seperate urls.

--->> We are going to use required HTTP methods to perform required operations on       database using apis.

--->> for example,  GET, POST,PUT,DELETE,...

Syntax:

class EmployeeListView(APIView):
    def  get(self,request):
        <do get logics here>

    def  post(self,request):
        <do get logics here>



Q.  How to develop apis to perform CURD operations using APIView  concept ?

Example:
========

step1 : create project name

step2 : create application name

step3 : open settings.py file and goto INSTALLED_APPS section  add our "application name"           and  "rest_framework" applications.


INSTALLED_APPS = [
    '-------------',
    '-------------',
    '-------------',
    '-------------',    
   
    'APIView_App.apps.ApiviewAppConfig',
   
    'rest_framework',

]


--->> Goto  DATABASES  section and configure the database details like beloow

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER' : 'username',
        'PASSWORD' : 'password',
    }
}


step4 : create required database name  using mysql prompt

mysql> create database  nth_rest9amdb_apiview;

step5 : open models and create required models here

step6 : create serializers.py file inside our application name and create required         serializers code here.

step7 : open views.py and create reqired APIViews .

step8 : open urls.py and create reqired api urls for execute reqired APIViews.

step9 : execute makemigrations , migrate, createsuperuser and runserver commands.

step10 : Now execute the usrls from the browser and perform all operations.


