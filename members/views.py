from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Item, News
from datetime import date
import datetime
from .forms import add_form
import locale

locale.setlocale(locale.LC_ALL, "id_ID")

def index_page(request):
    template = loader.get_template('index.html')
    context = {
        'message': "Welcome to the Members Index Page!",
        'items': Item.objects.all().values,
        'items_today': Item.objects.raw("SELECT * FROM members_item WHERE date = '" + date.today().strftime("%Y-%m-%d") + "'" ),
        'date': date.today().strftime("%d %b %Y"),
        'date_yesterday': (date.today() - datetime.timedelta(days=1)).strftime("%d %b %Y"),
        'news': News.objects.all().values
    }
    # return render(request, 'members/index.html', context)
    return HttpResponse(template.render(context, request))

@login_required
def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = {
        'items': Item.objects.all().values,
        'dates': Item.objects.values('id', 'date').filter(name='test')
    }
    return HttpResponse(template.render(context, request))

@login_required
def add(request):
  template = loader.get_template('add.html')
  context = {
     'form': add_form()
  }
  return HttpResponse(template.render(context, request))

@login_required
def addrecord(request):
   if request.method == 'POST':
      form = add_form(request.POST)
      if form.is_valid():
        date_string = date.today().strftime("%Y-%m-%d")
        name = request.POST['name']
        price = request.POST['price']
        price_unit = request.POST['price_unit']
        stock = request.POST['stock']
        stock_unit = request.POST['stock_unit']
        if Item.objects.raw("SELECT * FROM members_item WHERE name = '" + name + "' AND date = '" + (date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "'" ):
            yesterday_price = Item.objects.raw("SELECT id, price FROM members_item WHERE name = '" + name + "' AND date = '" + (date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "'" )
            item = Item(date=str(date_string), name=name, price=price, price_unit=price_unit, stock=stock, stock_unit=stock_unit, yesterday_price=yesterday_price.price)
        else:
            item = Item(date=str(date_string), name=name, price=price, price_unit=price_unit, stock=stock, stock_unit=stock_unit)
        item.save()
        if not Item.objects.raw("SELECT * FROM members_item WHERE name = 'test' AND date = '" + date.today().strftime("%Y-%m-%d") + "'" ):
           Item(date=str(date_string), name="test", price=0, stock=0).save()
           print("saved ")
        return HttpResponseRedirect(reverse('dashboard') + '?message=Data+berhasil+ditambahkan.')

@login_required
def update(request, id):
    template = loader.get_template('update.html')
    context = {
        'form': add_form(),
        'item': Item.objects.get(id=id)
    }
    if Item.objects.raw("SELECT * FROM members_item WHERE id = '" + str(id) + "' AND date = '" + date.today().strftime("%Y-%m-%d") + "'" ):
        context['up_to_date'] = True
    else: context['up_to_date'] = False
    return HttpResponse(template.render(context, request))
  
@login_required
def updaterecord(request, id):
    if request.method == 'POST':
        form = add_form(request.POST)
        if form.is_valid():
            date_string = date.today().strftime("%Y-%m-%d")
            item = Item.objects.get(id=id)
            item.date = date_string
            name = request.POST['name']
            item.name =  name
            item.price = request.POST['price']
            item.price_unit = request.POST['price_unit']
            item.stock = request.POST['stock']
            item.stock_unit = request.POST['stock_unit']
            if Item.objects.raw("SELECT * FROM members_item WHERE name = '" + name + "' AND date = '" + (date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "'" ):
                yesterday_price = Item.objects.raw("SELECT id, price FROM members_item WHERE name = '" + name + "' AND date = '" + (date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "'" )
                for p in yesterday_price:
                    item.yesterday_price = p.price
            item.save()
            if not Item.objects.raw("SELECT * FROM members_item WHERE name = 'test' AND date = '" + date.today().strftime("%Y-%m-%d") + "'" ):
                Item(date=str(date_string), name="test", price=0, stock=0).save()
            print("saved ")
        else:
            print('form invalid')
        return HttpResponseRedirect(reverse('dashboard') + '?message=Data+berhasil+diperbarui.+')

@login_required
def delete(request, id):
  item = Item.objects.get(id=id)
  item.delete()
  return HttpResponseRedirect(reverse('dashboard') + '?message=Data+berhasil+dihapus+')
      

# Item(date=(date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"), name="test", price=0, stock=0).save()