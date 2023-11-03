from account.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView
from .forms import PropertyInformationForm, UserPropertyForm
from .models import PropertyInformation


# Create your views here.


class PropertyDeleteView(DeleteView):
    template_name = ''
    model = PropertyInformation
    success_url = reverse_lazy('')


class UserPropertyView(View):
    def get(self, reqeust, pk):
        user = get_object_or_404(User, id=pk)
        properties = user.property.all()
        property_reserve = user.property.filter(is_reserve=True, is_public=True)
        return render(reqeust, '', {'properties': properties, 'property_reserve':property_reserve})


class UserProperUpdateFormView(View):
    form_class = UserPropertyForm

    def dispatch(self, request, *args, **kwargs):
        if request.user != request.user.id:
            return redirect('')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        form = self.form_class(instance=user)
        return render(request, '', {'form': form})

    def post(self, request, pk):
        user = get_object_or_404(User, id=pk)
        form = self.form_class(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('', user.pk)


class PropertyInformationView(View):
    form_class = PropertyInformationForm
    def get(self, request):
        form = self.form_class()
        return render(request, '', {'form':form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=True)
            new.user = request.user
            new.save()
            return redirect('')

class PropertyInformationUpdateView(View):
    form_class = PropertyInformationForm

    def dispatch(self, request, *args, **kwargs):
        if request.propertyinformation.user.id != request.user.id:
            return redirect('')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        properties = get_object_or_404(PropertyInformation, id=pk)
        form = self.form_class(instance=properties)
        return render(request, '', {'form':form})
    
    def post(self, request, pk):
        properties = get_object_or_404(PropertyInformation, id=pk)
        form = self.form_class(request.POST, request.FILES, instance=properties)
        if form.is_valid():
            form.save()
            return redirect('')
    

class PropertyDetailView(View):
    def get(self, request, pk):
        properties = get_object_or_404(PropertyInformation, id=pk)
        return render(request, '', {'properties':properties})