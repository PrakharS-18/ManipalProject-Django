from django.urls import path
from .views import Index, RentalProduct, RentalSubProducts, Login, Register,Logout
from .views import RecieverForm
from .views import ShowPage, PastOrders, Order
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('home', Index.as_view(), name='homepage'),
    path('form_fill', RecieverForm.as_view(), name='recieverform'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('subcategory/', RentalProduct.as_view(), name='subcategory'),
    path('formPost', ShowPage.as_view()),
    path('pastOrders', PastOrders.as_view()),
    path('order', Order.as_view()),
    path('', RentalSubProducts.as_view()),
]