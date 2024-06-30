from django.urls import path, include
from . import views

app_name = 'report_potholes'

urlpatterns = [
    # admin categories
    path('category/', views.CategoryBrowseView.as_view(), name='category_browse'),
    path('category/list', views.CategoryListView.as_view(), name='category_list'),
    # path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    # admin potholes
    path('potholes',views.PotholeBrowseView.as_view(), name='potholes_browse'),
    path('potholes/list',views.PotholesListView.as_view(), name='potholes_list'),
    path('pothole/<int:pk>/detalles', views.PotholeDetailviewAdmin.as_view(), name='pothole_detail'),
    path('pothole/add/', views.PotholeCreateView.as_view(), name='pothole_add'),
    path('pothole/<int:pk>/edit/', views.PotholeUpdateView.as_view(), name='pothole_edit'),


    path('solicitude', views.UnapprovedPotholeListView.as_view(), name='solicitude_potholes'),
    path('approve_pothole/<int:pk>/', views.approve_pothole, name='approve_pothole'),
    path('delete/<int:pk>/', views.PotholeDeleteView.as_view(), name='delete_pothole'),
    path('deletepoint/<int:pk>/', views.PotholePointDeleteView.as_view(), name='delete_potholepoint'),
    path('pothole/<int:pk>/', views.PotholeDetailMapView.as_view(), name='pothole_detail_map'),
]
