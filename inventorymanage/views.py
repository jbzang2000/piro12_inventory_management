from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop, Item
from .forms import ItemForm, ShopForm
from django.urls import reverse


# Create your views here.

def item_list(request):
    queryset = Item.objects.all()
    return render(request, 'inventorymanage/item_list.html', {
        'item_list': queryset
    })

def item_amount_add(request, pk):

    item = Item.objects.get(pk=pk)
    queryset = Item.objects.all()
    print(request.POST)
    if request.method == 'POST':
        item.amount = item.amount + 1
        item.save()  # 저장을 해야 함
        return render(request, 'inventorymanage/item_list.html', {
            'item_list': queryset
        })

def item_amount_sub(request, pk):

    item = Item.objects.get(pk=pk)
    queryset = Item.objects.all()
    print(request.POST)
    if request.method == 'POST':
        item.amount = item.amount - 1
        item.save()  # 저장을 해야 함
        return render(request, 'inventorymanage/item_list.html', {
            'item_list': queryset
        })



def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'inventorymanage/item_detail.html', {
        'item': item
    })


def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'inventorymanage/shop_detail.html', {
        'shop': shop
    })


def shop_list(request):
    queryset = Shop.objects.all()
    return render(request, 'inventorymanage/shop_list.html', {
        'shop_list': queryset
    })


def item_create(request, item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item = form.save()
            return redirect('inventorymanage:item_detail', item.id)
    else:
        form = ItemForm(instance=item)
        return render(request, 'inventorymanage/item_create.html', {
            'form': form,
        })


def shop_create(request, shop=None):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)

        if form.is_valid():
            shop = form.save()
            return redirect('inventorymanage:shop_detail', shop.id)
    else:
        form = ShopForm(instance=shop)
        return render(request, 'inventorymanage/shop_create.html', {
            'form': form,
        })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_create(request, item)


def shop_edit(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return shop_create(request, shop)


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'GET':
        return redirect('inventorymanage:item_detail', item.id)

    if request.method == 'POST':
        item.delete()
        return redirect('inventorymanage:item_list')


def shop_delete(request, pk):
    shop = get_object_or_404(Shop, pk=pk)

    if request.method == 'GET':
        return redirect('inventorymanage:shop_detail', shop.id)

    if request.method == 'POST':
        shop.delete()
        return redirect('inventorymanage:shop_list')
