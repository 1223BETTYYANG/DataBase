from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
#from django.shortcuts import render
from django.db import connection

# Create your views here.
def index(request):
    art_music_list = BooksInfo.books.get_art_music()[0:3]
    science_engineering_list = BooksInfo.books.get_science_engineering()[0:3]
    biology_medicine_list = BooksInfo.books.get_biology_medicine()[0:3]
    financial_business_list = BooksInfo.books.get_financial_business()[0:3]
    literature_social_list = BooksInfo.books.get_literature_social()[0:3]
    other_list = BooksInfo.books.get_other()[0:3]
    context = {'art_music_list':art_music_list, 'science_engineering_list':science_engineering_list, 'biology_medicine_list':biology_medicine_list, 'financial_business_list':financial_business_list, 'literature_social_list':literature_social_list, 'other_list':other_list}
    return render(request,'books/index.html',context)

def art_music_list(request):
    art_music_list = BooksInfo.books.get_art_music()
    context = {'art_music_list':art_music_list}
    return render(request, 'books/art_music_list.html', context)

def science_engineering_list(request):
    science_engineering_list = BooksInfo.books.get_science_engineering()
    context = {'science_engineering_list':science_engineering_list}
    return render(request, 'books/science_engineering_list.html', context)

def biology_medicine_list(request):
    biology_medicine_list = BooksInfo.books.get_biology_medicine()
    context = {'biology_medicine_list':biology_medicine_list}
    return render(request, 'books/biology_medicine_list.html', context)

def financial_business_list(request):
    financial_business_list = BooksInfo.books.get_financial_business()
    context = {'financial_business_list': financial_business_list}
    return render(request, 'books/financial_business_list.html', context)

def literature_social_list(request):
    literature_social_list = BooksInfo.books.get_literature_social()
    context = {'literature_social_list': literature_social_list}
    return render(request, 'books/literature_social_list.html', context)

def other_list(request):
    other_list = BooksInfo.books.get_other()
    context = {'other_list':other_list}
    return render(request, 'books/other_list.html', context)

def release_books(request):
    username = request.session.get('username')
    if username == None:
        context = {'error_msg': '请先登录'}
        return render(request, 'user/login.html', context)
    else:
        context = {}
        return render(request, 'books/release_books.html', context)

def release(request):
    post = request.POST
    title = post.get('title')
    type = post.get('type')
    price = post.get('price')
    address = post.get('address')
    picture = request.FILES['picture']
    fname = '%s/books/%s' % (settings.MEDIA_ROOT, picture.name)
    with open(fname, 'wb') as pic:
        for c in picture.chunks():
            pic.write(c)
    description = post.get('description')
    user_id = request.session.get('user_id')
    user = UserInfo.objects.filter(id=user_id)[0]
    BooksInfo.books.create_book(title,type,'books/'+picture.name,price,address,description,user)
    return redirect('/')

def books_details(request):
    title = request.GET['title']
    book = BooksInfo.books.get_title(title)[0]
    context = {'book':book}
    return render(request, 'books/books_details.html', context)

def after_search(request):
    search_title = request.GET['search_title']
    books = BooksInfo.books.filter(title__contains=search_title)
    print(books)
    count = BooksInfo.books.filter(title__contains=search_title).count()
    print(count)
    context = {'books':books, 'search_title':search_title, 'count':count}
    return render(request, 'books/after_search.html', context)

def book_expensive(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM book_expensive")
        rows = cursor.fetchall()
    return render(request, 'books/book_expensive.html', {'rows': rows})





def UpdateBookPrice(book_id, new_price):
    with connection.cursor() as cursor:
        cursor.callproc('UpdateBookPrice', [book_id, new_price])



