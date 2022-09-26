"""News_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home_App import views as hv
from News_App import views as nv
from Category_App import views as cv
from Sub_Category_App import views as scv
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    # Home Page
    path('',hv.home,name='home'),
    path('contact/',hv.contact,name='contact'),
    path('about/',hv.about,name='about'),

    # Category Page
    #path('category/', hv.category),

    # News Page
    path('news/?P<word>.*/',nv.news_detail,name='News_detail'),

    # error Page
    path('error/',hv.error,name='error'),

    # Authentication
    path('login/',hv.login,name='login'),
    #path('logout/',hv.log_out,name='logout'),
   

    # Admin Start 
    path('panel/', hv.panel,name='panel'),

    path('panel/news/list/',nv.news_list,name='news_list'),
    path('panel/news/add/',nv.news_add,name='news_add'),
    path('panel/news/edit/?P<pk>d+/',nv.news_edit,name='news_edit'),
    path('panel/news/del/?P<pk>d+/',nv.news_delete,name='news_delete'),

    #Category Section
    path('panel/category/list/',cv.category_list,name='category_list'),
    path('panel/category/add/',cv.category_add,name='category_add'),
    path('panel/category/del/?P<pk>d+/',cv.category_delete,name='category_delete'),

    #Sub Category Section
    path('panel/subcategory/list/',scv.subcat_list,name='subcat_list'),
    path('panel/subcategory/add/',scv.subcat_add,name='subcat_add'),
    path('panel/subcategory/del/?P<pk>d+/',scv.subcat_delete,name='subcat_delete'),

   # Admin End


]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


