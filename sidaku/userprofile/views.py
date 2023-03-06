from django.views import View
from django.shortcuts import render,redirect
from django.contrib import messages
from userprofile.forms import UserRegistrationForm
from userprofile.forms import UserListForm
from userprofile.forms import UserProfileForm, form_validation_error
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.core.paginator import Paginator

from userprofile.models import UserProfile


# @login_required(login_url=settings.LOGIN_URL)
@method_decorator(login_required(login_url=settings.LOGIN_URL), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = UserProfile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserProfileForm(instance=self.profile)
        context = {
            'profile': self.profile,
            'side_active'   : 'selfprof',
            'form': form
         }
        return render(request, 'users/profile.html', context)

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            
            # to save user model info
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name  = form.cleaned_data.get('last_name')
            profile.user.email      = form.cleaned_data.get('email')
            profile.user.save()
            
            messages.success(request, 'Profile saved successfully')

            return redirect('userprofile:selfprofile')
        else:
            messages.error(request, form_validation_error(form))



@login_required(login_url=settings.LOGIN_URL)
def master_userp(request):
    search =""
    tables =""

    if request.GET:
        search = request.GET.get('search')
        query = (Q(nik__icontains=search) | Q(phone__icontains=search) | 
        Q(user__first_name__icontains=search) | Q(user__last_name__icontains=search) | 
        Q(user__username__icontains=search) | Q(user__email__icontains=search)) 
        tables = UserProfile.objects.filter(query)
    else:
        tables = UserProfile.objects.all()

    

    paginator   = Paginator(tables, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    list_data = {
        'side_active'   : 'profile',
        'tables' : tables,
        'page_obj' : page_obj,
    }

    return render (request, 'users/master_userp.html', list_data)




@login_required(login_url=settings.LOGIN_URL)
def update_userp(request, user_id):

    tables = UserProfile.objects.get(id = user_id)

    template = 'users/update_userp.html'
    if request.POST:
        form = UserProfileForm(request.POST, request.FILES, instance = tables)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_by = str(request.user)
            post.save()


            post.user.first_name = form.cleaned_data.get('first_name')
            post.user.last_name  = form.cleaned_data.get('last_name')
            post.user.email      = form.cleaned_data.get('email')
            post.user.save()
            # form.save()
            messages.success(request, "Data Berhasil Di Ubah")
            return redirect('userprofile:update_userp', user_id)
        else:
            messages.error(request, "Data Gagal Di Ubah")
            form = UserProfileForm(instance=tables)
        
    else:
        form = UserProfileForm(instance=tables)

    list_data = {
        'side_active'   : 'profile',
        'form'          : form,
        'tables'        : tables
    }
    return render (request, template, list_data)

@login_required(login_url=settings.LOGIN_URL)
def add_userp(request):
    tables = UserProfile.objects.all()

    if request.POST:
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            userpost = form.save(commit=False)
            userpost.save()
            UserProfile.objects.get_or_create(user=userpost)
            form = UserRegistrationForm()

            messages.success(request, "data berhasil disimpan")
            list_data = {
                'side_active'   : 'profile',
                'form'          : form,
                'tables'        : tables,
            }
            return render(request, "users/add_userp.html", list_data)
        else:
            messages.error(request, "data gagal disimpan")

    else:
        form = UserRegistrationForm()

    list_data = {
        'side_active'   : 'profile',
        'form'          : form,
        'tables'        : tables,
    }

    return render (request, 'users/add_userp.html', list_data)

@login_required(login_url=settings.LOGIN_URL)
def del_userp(request, user_id):
    field = UserProfile.objects.filter(id = user_id)
    user = field.User
    field.delete()
    user.delete()
    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('userprofile:master_userp')



def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
    )