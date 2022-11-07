from django.shortcuts import render,redirect
from django.views import View
from .models.subproduct import SubProduct
from .models.product import Product
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password

# login into the website
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        Hospital_Name_tobe_verified = request.POST.get('username')
        password_tobe_verified = request.POST.get('password')
        customer = Customer.get_by_hospitalName(Hospital_Name_tobe_verified)
        user_type = request.POST.get('user')
        error_message = None

        print(customer)

        if customer:
            flag = check_password(password_tobe_verified, customer.Hospital_Password)
            if flag:
                # maintaining the session dictionary(object) iske help se hi ho rha keys ka dhyaan dena
                request.session['customer'] = customer.Hospital_Id
                request.session['Hospital_Name'] = customer.Hospital_Name
                if user_type == "1":
                    return redirect('homepage')
                else:
                    return render(request, 'donarDashboard.html')
            else:
                error_message = "Email or Password Invalid"

        else:
            error_message = "Email or Password Invalid"
        return render(request, 'login.html', {'error_message': error_message})


# signup for new User
class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        try:
            Hospital_Name = request.POST.get('username')
            Hospital_Location = request.POST.get('address')
            Hospital_City = request.POST.get('cityName')
            Hospital_Id = request.POST.get('uniqueID')
            Hospital_Number = request.POST.get('contact')
            Hospital_Email = request.POST.get('email')
            Hospital_Password = request.POST.get('password')
            User = request.POST.get('user')
            Donor = request.POST.get('donor')

            UserType = None

            if User == "1":
                UserType = User
            else:
                UserType = Donor

            customer = Customer(Hospital_Name=Hospital_Name, Hospital_Location=Hospital_Location,
                                Hospital_City=Hospital_City, Hospital_Id=Hospital_Id, Hospital_Number=Hospital_Number,
                                Hospital_Email=Hospital_Email, Hospital_Password=Hospital_Password, UserType=UserType)

            # Hashing the Hospital_Password to HashPassword using the make_password built-in function
            customer.Hospital_Password = make_password(Hospital_Password)

            # saving the customer to
            customer.save()
            return redirect('homepage')
        except:
            return render(request, 'register.html')


# logout the user
class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect('login')


# landing Page
class Index(View):
    def get(self, request):
        product = Product.objects.all()
        data = {
            'products': product
        }
        return render(request, 'home.html', data)


# Product Page
class RentalProduct(View):
    def get(self, request):
        subproducts = None
        product_name = None

        product_id = request.GET.get('product')

        product_detail = Product.objects.get(id = product_id)
        # print(product_detail)

        if product_id:
            subproducts = SubProduct.get_by_productid(product_id)
            product_name = product_detail.title
            request.session['product_name'] = product_name
        else:
            subproducts = SubProduct.objects.all()

        return render(request, 'subcategory.html', {'subproducts': subproducts, 'product_detail': product_detail, 'product_name': product_name})


# SubProject Page
class RentalSubProducts(View):
    def get(self, request):
        subproduct_detail = None
        subproduct_name = None
        subproduct_id = request.GET.get('subproduct')

        if subproduct_id:
            subproduct_detail = SubProduct.objects.get(id = subproduct_id)
            subproduct_name = subproduct_detail.title
            request.session['subproduct_name'] = subproduct_name
        else:
            subproduct_detail = SubProduct.objects.all()

        return render(request, 'description.html', {'subproduct_detail': subproduct_detail})


# receiver order form
class RecieverForm(View):
    def post(self, request):
        type = None
        RentNew = request.POST.get('new')
        if RentNew:
            type = RentNew
        else:
            type = "Rent Old"

        Hospital_Name = request.session['Hospital_Name']
        product_name = request.session['product_name']
        subproduct_name = request.session['subproduct_name']
        data = {
            'Hospital_Name': Hospital_Name,
            'subproduct_name': subproduct_name,
            'product_name': product_name,
            'type': type,
        }
        return render(request, 'form.html', data)


# displaying Hospital's after filtering
class ShowPage(View):
    def post(self, request):

        filter_type = None

        emergency = request.POST.get('emergency')
        rating = request.POST.get('rating')

        #order_by Sorts according to the given ratings
        Hospitals_Rating = Customer.objects.filter(UserType = "2").order_by('Hospital_Id').values

        # sort according to distance
        Hospitals_Distance = Customer.objects.filter(UserType = "2").order_by('Hospital_Location')

        # sort according availability
        Hospitals_available = Customer.objects.filter(UserType="2").order_by('Hospital_Name')

        if emergency == "1":
            filter_type = Hospitals_Distance
        elif rating == "2":
            filter_type = Hospitals_Rating
        else:
            filter_type = Hospitals_available

        quantity_required = request.POST.get('quantity')
        due_date = request.POST.get('date')
        product_name = request.session['product_name']
        subproduct_name = request.session['subproduct_name']

        data = {
            'filter_type': filter_type,
            'subproduct_name': subproduct_name,
            'quantity_required': quantity_required,
            'product_name': product_name,
            'due_date': due_date,
        }
        return render(request, 'show.html', data)


# for maintaining past orders of the suppliers
class PastOrders(View):
    def get(self, requests):
        equipment_name = requests.GET.get('equipmentName')
        hospital_name = requests.GET.get('hospitalName')
        quantity = requests.GET.get('equipmentrequired')
        rental_cost = requests.GET.get('equipmentCost')

        data= {
            'equipment_name': equipment_name,
            'hospital_name': hospital_name,
            'quantity': quantity,
            'rental_cost': rental_cost,
        }
        return render(requests, 'pastOrders.html', data)



class Order(View):
    def post(self, request):
        return redirect('homepage')