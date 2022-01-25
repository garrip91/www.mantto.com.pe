from django.shortcuts import render

from django.views import View



# Create your views here:
class HomePageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'ManttoApp/home.html', context={})
        
    # def post(self, request):
        # user_form = UserForm(request.POST)
        # if user_form.is_valid():
            # # совершаем какую-либо бизнес-логику
            # # к примеру, сохранение в базе данных
            # User.objects.create(**user_form.cleaned_data)
            # return HttpResponseRedirect('/')
        # return render(request, 'profiles/register.html', context={'user_form': user_form})
        
        
class CategoryNoticiasView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'ManttoApp/category/noticias/category_noticias.html', context={})