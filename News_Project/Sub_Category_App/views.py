from django.shortcuts import render,redirect
from Sub_Category_App.models import Sub_Category
from Category_App.models import News_Category
from date_time import today

# Add Category
def subcat_add(request):

    if (request.method == 'POST'):

        subcat_title = request.POST.get('subcat_title')
        parent_id = request.POST.get('parent_id')
        subcat_creater = request.POST.get('subcat_creater')
        subcat_summary = request.POST.get('subcat_summary')
        date = request.POST.get('subcatdate')

        if subcat_title == "" or subcat_creater == "" or subcat_summary == "" :
            error="All Fields Are Required..."
            return render(request, 'back/error.html',{'error':error})

        try:
            #to Varify by calling that title to check if it exist then it len should be more than 0
            
            if len(Sub_Category.objects.filter(Title=subcat_title)) != 0:
                error="This Sub Category is already exist.."
                return render(request, 'back/error.html',{'error':error})
    
            else:
                catname = News_Category.objects.get(pk=parent_id)
                #parent_id=News_Cat.objects.filter(Title=parentcat_title)
                Subcat_data = Sub_Category(Title = subcat_title , Parent_Name = catname ,
                                           Parent_Id = parent_id , Created_By = subcat_creater ,
                                           Added_Date = date , Short_Text = subcat_summary ,
                                           Views = '00')         
                Subcat_data.save()
                return redirect('subcat_list')

        except:
            error="Please Retry"
            return render(request, 'back/error.html',{'error':error})
      
    news_cat = News_Category.objects.all()
    Added_date = today()
    return render(request, 'back/Sub_Category/sub_cat_add.html',{'news_cat':news_cat,'date':Added_date})

# Category list
def subcat_list(request):
    '''# login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end;'''
    sub_cat = Sub_Category.objects.all()
    return render(request, 'back/Sub_Category/sub_cat_list.html',{'sub_cat':sub_cat})

def subcat_delete(request,pk):
    '''# login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end'''
    try:
        d = Sub_Category.objects.get(pk=pk)
        d.delete()
    except:
        error="Something Wrong"
        return render(request, 'back/error.html',{'error':error})

    return redirect('subcat_list')