from django.shortcuts import render,redirect
from Category_App.models import News_Category
from date_time import today

# Create your views here.

# Add Category
def category_add(request):

    if (request.method == 'POST'):
        cat_title = request.POST.get('cat_title')
        cat_creater = request.POST.get('cat_creater')
        cat_summary = request.POST.get('cat_summary')
        added_date = request.POST.get('added_date')

        if cat_title == "" or cat_creater == "" or cat_summary == "":
            error="All Fields Are Required..."
            return render(request, 'back/error.html',{'error':error})

        try:
            #to Varify by calling that title to check if it exist then it len should be more than 0
             
            if len(News_Category.objects.filter(Title=cat_title)) != 0:
                error="This Category is already exist.."
                return render(request, 'back/error.html',{'error':error})

            else:
                category_data = News_Category(Title = cat_title , Created_By = cat_creater , 
                                              Added_date = added_date , Short_Text = cat_summary,
                                              Views = "10")         
                category_data.save()
                return redirect('category_list')
        
        except:
            error="Please Retry"
            return render(request, 'back/error.html',{'error':error})

    Added_date = today()
    return render(request, 'back/category/category_add.html',{'date':Added_date})


# Category list
def category_list(request):
    news_cat = News_Category.objects.all()
    return render(request, 'back/category/category_list.html',{'news_cat':news_cat})


def category_delete(request,pk):

    try:
        b = News_Category.objects.get(pk=pk)
        b.delete()

    except:
        error="Something Wrong"
        return render(request, 'back/error.html',{'error':error})

    return redirect('category_list')