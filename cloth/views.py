from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ClothTagEinsView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Carhartt")
    template_name = "eins_tag.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Carhartt")


class ClothTagZweiView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Nike")
    template_name = "zwei_tag.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Nike")


class ClothTagDreiView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Кроссовки")
    template_name = "drei_tag.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Кроссовки")


class ClothTagVierView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Футболки")
    template_name = "vier_tag.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Футболки")


class ClothListView(ListView):
    queryset = models.ProductCL.objects.filter().order_by('-id')
    template_name = "cloth_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by('-id')


class OrderCreateView(CreateView):
    template_name = "add_order.html"
    form_class = forms.OrderCLForm
    success_url = "/cloth/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)