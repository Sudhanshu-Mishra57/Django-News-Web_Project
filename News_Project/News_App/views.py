from contextlib import redirect_stderr
from distutils.log import error
from fileinput import filename
import imp
from sre_constants import SUCCESS
from tkinter import image_names
from django.shortcuts import render,redirect
from News_App.models import News
from Category_App.models import News_Category
from Sub_Category_App.models import Sub_Category
from Category_App.models import Category
from django.core.files.storage import FileSystemStorage
from date_time import today




# Frontend strat
def news_detail(request,word):
    news = News.objects.filter(Title=word)
    return render(request, 'front/News/news_details.html',{'news':news})
# Frontend end

# Backend Start

# News Add
def news_add(request):
    
    if request.method == 'POST':
        title = request.POST.get('newstitle')
        author = request.POST.get('newsauthor')
        cat = request.POST.get('newscat')
        subcat = request.POST.get('subcat')
        summary = request.POST.get('newssummary')
        content = request.POST.get('newscontent')
        image = request.POST.get('newsimage')
        date = request.POST.get('newsdate')

        if title == "" or cat == "" or subcat == "" or content == "" or date == "" or summary == "":
            error="All Fields Are Required..."
            return render(request, 'back/error.html',{'error':error})  
    
        try: 
            #for save image and give it a system generated name from prevent duplicate name
            newsimage = request.FILES['newsimage']
            fs = FileSystemStorage()
            image_name = fs.save(image,newsimage)
            url = fs.url(image_name)
            #for check the filetype because the user can only upload an real image
            if str(newsimage.content_type).startswith("image"):
                
                #for checking file size is less than 5mb

                if newsimage.size < 5000000:
                    cat_id = Category.objects.get(Title=cat).pk
                    subcat_id = Sub_Category.objects.get(Title=subcat).pk
                    print('===============')
                    print(cat_id,subcat_id)

                    # for saving the content in the database
                    news_data = News(Title = title , Author = author ,
                                Summary = summary , Content = content , 
                                ImageName = image_name , Image = url ,       
                                Added_date = date , Category = cat , 
                                Sub_Category = subcat , Views = '23' )
                    news_data.save()                    
                    return redirect('news_list')

                else:
                    fs = FileSystemStorage()
                    fs.delete(image_name)

                    error="Your file is bigger than 5mb"
                    return render(request, 'back/error.html',{'error':error})

            else:
                fs = FileSystemStorage()
                fs.delete(image_name)
                error="Please Upload an valid Image"
                return render(request, 'back/error.html',{'error':error})

        except:
            error="Please Upload Image"
            return render(request, 'back/error.html',{'error':error})

    news_cat = News_Category.objects.all()
    sub_cat = Sub_Category.objects.all()
    Added_date = today()
    return render(request, 'back/News/news_add.html',{'date':Added_date,'news_cat':news_cat,'sub_cat':sub_cat})

# News List
def news_list(request):
    news_list = News.objects.all()
    return render(request, 'back/News/news_list.html',{'news_list':news_list})

# News Edit
def news_edit(request,pk):

    if len(News.objects.filter(pk=pk)) == 0:
        error="News Not Found"
        return render(request, 'back/error.html',{'error':error})

    news = News.objects.get(pk=pk)
    cat = News_Category.objects.all()
    sub_cat = Sub_Category.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('newstitle')
        author = request.POST.get('newsauthor')
        cat = request.POST.get('newscat')
        subcat = request.POST.get('subcat')
        summary = request.POST.get('newssummary')
        content = request.POST.get('newscontent')
        image = request.POST.get('newsimage')
        date = request.POST.get('newsdate')

        if title == "" or cat == "" or subcat == "" or content == "" or date == "" or summary == "" or image == "":
            error="All Fields Are Required..."
            return render(request, 'back/error.html',{'error':error})  
    
        try: 
            #for save image and give it a system generated name from prevent duplicate name
            newsimage = request.FILES['newsimage']
            fs = FileSystemStorage()
            image_name = fs.save(image,newsimage)
            url = fs.url(image_name)
            #for check the filetype because the user can only upload an real image
            if str(newsimage.content_type).startswith("image"):
                
                #for checking file size is less than 5mb
                if newsimage.size < 5000000:

                    # for saving the content in the database
                    news_data = News.objects.get(pk=pk)
                    fss = FileSystemStorage()
                    fss.delete(image_name)

    
                    news_data.Title = title  
                    news_data.Image = url    
                    news_data.Category = cat    
                    news_data.Content = content 
                    news_data.Summary = summary
                    news_data.Added_date = date 
                    news_data.ImageName = image_name
                    news_data.Sub_Category = subcat
                    news_data.save() 

                    return redirect('news_list')

                else:
                    fs = FileSystemStorage()
                    fs.delete(image_name)
                    error="Your file is bigger than 5mb"
                    return render(request, 'back/error.html',{'error':error})

            else:
                fs = FileSystemStorage()
                fs.delete(image_name)
                error="Please Upload an valid Image"
                return render(request, 'back/error.html',{'error':error})

        except:
            news_data = News.objects.get(pk=pk)
            news_data.Title = title  
            news_data.Category = cat    
            news_data.Content = content 
            news_data.Summary = summary
            news_data.Added_date = date 
            news_data.Sub_Category = subcat
            news_data.save()                    
            return redirect('news_list')

    return render(request, 'back/news/news_edit.html',{'pk':pk,'news':news,'news_cat':cat,'sub_cat':sub_cat})

#Delete News
def news_delete(request,pk):

    try:
        b = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(b.ImageName)
        b.delete()
        
    except:
        error="Something Wrong"
        return render(request, 'back/error.html',{'error':error})
    return redirect('news_list')
# Backend End