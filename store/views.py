from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from store.models import Product, Vendor, Category, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Address
#from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
#@login_required
def index(request):
   if request.user.is_authenticated:
      categories=Category.objects.all()
      context = {
         'categories':categories
      }
      return render(request, 'store/index.html',context)
   else:
      return render(request,"userauths/sign-in.html")


def shop_view(request):
   if request.user.is_authenticated:
      products = Product.objects.all()
      context = {
      'products': products
      }
      return render(request,'store/shop.html',context)
   else:
      return render(request,"userauths/sign-in.html")

def about_view(request):
   
   return render(request,'store/about.html')

def contact_view(request):
   return render(request,'store/contact.html')

def blog_view(request):
   return render(request, 'store/blog.html')

def services_view(request):
   return render(request, 'store/services.html')

def cart_vieww(request):
   if request.user.is_authenticated:
      return render(request,'store/cart.html')
   else:
      return render(request,"userauths/sign-in.html")

def cart_view(request,pid):
   product=Product.objects.get(pid=pid)
   context = {
        'p': product
    }
   return render(request, 'store/cart.html',context)

def checkout_view(request):
   if request.user.is_authenticated:
      return render(request, 'store/checkout.html')
   else:
      return render(request,"userauths/sign-in.html")

def search_view(request):
   products = Product.objects.all()
   query1 = request.GET.get("q")
   query2 = request.GET.get("choices-single-defaul")
   min_price = request.GET.get("min")
   max_price = request.GET.get("max")
   print(min_price)
   print(max_price)
   print(query1)
   
   

   if query1 !='' and query1 is not None:
      products = products.filter(title__icontains=query1, descreption__icontains=query1)

   if (query2=='Salon'):
      category = Category.objects.get(title='Salon')
      cid = category.cid
      cat = Category.objects.get(cid=cid)
      products = products.filter(category=cat)

   if (query2=='Cuisine'):
      category = Category.objects.get(title='Cuisine')
      cid = category.cid
      cat = Category.objects.get(cid=cid)
      products = products.filter(category=cat)

   if (query2=='Chambre'):
      category = Category.objects.get(title='Chambre')
      cid = category.cid
      cat = Category.objects.get(cid=cid)
      products = products.filter(category=cat)

   if min_price is not None:
        products = products.filter(price__gte=min_price)

   if max_price is not None:
      products = products.filter(price__lte=max_price)

   context ={
      'products': products,
   }
   return render(request,'store/search.html', context)

   
def details_view(request,pid):
   product=Product.objects.get(pid=pid)
   # product= get_object_or_404(Product,pid=pid)
   context = {
        'p': product
    }
   return render(request, 'store/details.html',context)

def add_to_cart(request):
   cart_product={}
   cart_product[str(request.GET[{"id"}])]={
      'title':request.GET[{"title"}],
      'price':request.GET[{"price"}],
   }
   if 'cart_data_obj' in request.session:
      if str(request.GET[{"id"}]) in request.session['cart_data_obj']: 
         cart_data=request.session['cart_data_obj']
         cart_data[str(request.GET[{"id"}])] 
      

from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

def checkout_view(request):   
   return render(request,'store/checkout.html')  
   # host = request.get_host()
   # paypal_dict = {
   #    'business' : settings.PAYPAL_RECEIVER_EMAIL,
   #    'amount':'200',
   #    'item_name':"Order-Itrm-No-3",
   #    'invoice':'INVOICE_NO_3',
   #    'currency_code':"USD",
   #    'notify_url':'http://{}{}'.format(host, reverse("store:paypal-ipn")),
   #    'return-url': 'http://{}{}'.format(host, reverse("store:payment_completed")),
   # }

   # paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)

   # cart_total_amount = 319.00
   # if 'cart_data_obj' in request.session:
   #    return render(request, "store/checkout.html", {"cart_data":request.session['cart_data_obj'], 'cart_total_amount':cart_total_amount, 'paypal_payment_button':paypal_payment_button})

      #  if request.method == 'POST':
      #   # Récupérer les données du produit à partir de la requête POST
      #   product_id = request.POST.get('product_id')
      #   product_price = request.POST.get('product_price')
      #   product_image = request.POST.get('product_image')
      #   # Ajoutez d'autres champs requis
        
      #   # Vous pouvez également vérifier si l'utilisateur est connecté ou si le produit existe, etc.
        
      #   # Créer une instance de CartOrderItems pour représenter le produit dans le panier
      #   cart_item = CartOrderItems.objects.create(
      #       order=request.user,  # Ou toute autre méthode que vous utilisez pour récupérer l'utilisateur connecté
      #       item=product_id,  # Utilisez l'ID du produit comme référence
      #       price=product_price,
      #       image=product_image,
      #       # Ajoutez d'autres champs requis comme la quantité, le numéro de facture, etc.
      #   )
        
      #   # Vous pouvez également renvoyer une réponse JSON pour indiquer le succès de l'ajout au panier
      #   return JsonResponse({'success': True})

def payment_completed_view(request):
   return render(request, 'store/thankyou.html')

def chambre_view(request):
   products = Product.objects.all()
   
   category = Category.objects.get(title='Chambre')
   cid = category.cid
   cat = Category.objects.get(cid=cid)
   products = products.filter(category=cat)

   context ={
      'products': products,
   }
   return render(request,'store/chambre.html', context)

def salon_view(request):
   products = Product.objects.all()
   
   category = Category.objects.get(title='Salon')
   cid = category.cid
   cat = Category.objects.get(cid=cid)
   products = products.filter(category=cat)

   context ={
      'products': products,
   }
   return render(request,'store/salon.html', context)

def cuisine_view(request):
   products = Product.objects.all()
   
   category = Category.objects.get(title='Cuisine')
   cid = category.cid
   cat = Category.objects.get(cid=cid)
   products = products.filter(category=cat)

   context ={
      'products': products,
   }
   return render(request,'store/cuisine.html', context)