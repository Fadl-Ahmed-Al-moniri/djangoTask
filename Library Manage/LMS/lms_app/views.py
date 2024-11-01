from django.shortcuts import render
from django.shortcuts import redirect

from .models import * 
from .forms import * 
# Create your views here.



def home(request): 
    context= {
        "books":Book.objects.all(),
        "bookcount":Book.objects.all().count(),
        "typecategory":Category.objects.all(),
        "addbookforms":AddBookForm(),
        "addcategoryforms":AddCategoryForm(),
        "bookavailable":Book.objects.exclude(state="available" ).count(),
        "booksold":Book.objects.exclude(state="sold" ).count(),
        "bookrental":Book.objects.exclude(state="rental" ).count(),
        "bookpricerental":Book.objects.all().exclude(state="rental"),
        "bookprice":Book.objects.all().exclude(state="sold")

    }
    bookdata = AddBookForm(request.POST,request.FILES)
    categorydata=AddCategoryForm(request.POST,request.FILES)
    if request.method=="POST":
        if categorydata.is_valid(): 
                    categorydata.save()
                    print("some_success_url")
        if bookdata.is_valid(): 
                    bookdata.save()
                    print("some_success_url")
    else:
        None
    return render(request=request,template_name="pages/index.html",context=context)



def showbooks(request):
    title =None
    search = Book.objects.all()
    if "search_name" in request.GET:
        title = request.GET["search_name"]
        if title :
                search= search.filter(title__icontains= title)
    context= {
        "books":search,
        "bookcount":Book.objects.all().count(),
        "typecategory":Category.objects.all(),
        "addbookforms":AddBookForm(),
        "addcategoryforms":AddCategoryForm(),
    }
    return render(request=request,template_name="pages/books.html",context=context)
def deletebook(request,id ):
    context= {
        "books":Book.objects.all(),
        "bookcount":Book.objects.all().count(),
        "typecategory":Category.objects.all(),
        "addbookforms":AddBookForm(),
        "addcategoryforms":AddCategoryForm(),
    }
    book_id = Book.objects.get(id=id)
    if request.method =="POST":
            book_id.delete()
            return  redirect("/")

        
    return render(request=request,template_name="pages/delete.html",context=context)


def updatebook(request,id):
    book_id = Book.objects.get(id=id)
    if request.method =="POST":
        bookdata= AddBookForm(request.POST,request.FILES,instance=book_id)
        if bookdata.is_valid:
                bookdata.save()
                return redirect(to='/')
    else :  
        context= {
            "addbookforms":AddBookForm(instance=book_id),
        }
    return render(request=request,template_name="pages/update.html",context=context)