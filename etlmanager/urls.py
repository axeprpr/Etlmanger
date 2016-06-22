"""ETLmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','etlmanager.views.monitor_racq'),
    url(r'wow/$', 'etlmanager.views.monitor_wow'),
    url(r'api/$', 'etlmanager.views.monitor_api'),
    url(r'^racq/$', 'etlmanager.views.monitor_racq'),
    url(r'^bookshop/$', 'etlmanager.views.monitor_bookshop'),
    url(r'^gdt/$', 'etlmanager.views.monitor_gdt'),
    url(r'^news/$', 'etlmanager.views.monitor_news'),
    url(r'^spark/$', 'etlmanager.views.monitor_spark'),
    url(r'^vmb/$', 'etlmanager.views.monitor_vmb'),
    url(r'^vmy/$', 'etlmanager.views.monitor_vmy'),
    url(r'^nib/$', 'etlmanager.views.monitor_nib'),
    url(r'^paypal/$', 'etlmanager.views.monitor_paypal'),
    url(r'^foxtel/$', 'etlmanager.views.monitor_foxtel'),
    url(r'^ikea/$', 'etlmanager.views.monitor_ikea'),
    
    url(r'^wow.*monitor/$', 'etlmanager.views.monitor_wow'),
    url(r'^api.*monitor/$', 'etlmanager.views.monitor_api'),
    url(r'^racq.*monitor/$', 'etlmanager.views.monitor_racq'),
    url(r'^bookshop.*monitor/$', 'etlmanager.views.monitor_bookshop'),
    url(r'^gdt.*monitor/$', 'etlmanager.views.monitor_gdt'),
    url(r'^news.*monitor/$', 'etlmanager.views.monitor_news'),
    url(r'^spark.*monitor/$', 'etlmanager.views.monitor_spark'),
    url(r'^vmb.*monitor/$', 'etlmanager.views.monitor_vmb'),
    url(r'^vmy.*monitor/$', 'etlmanager.views.monitor_vmy'),
    url(r'^nib.*monitor/$', 'etlmanager.views.monitor_nib'),
    url(r'^paypal.*monitor/$', 'etlmanager.views.monitor_paypal'),
    url(r'^foxtel.*monitor/$', 'etlmanager.views.monitor_foxtel'),
    url(r'^ikea.*monitor/$', 'etlmanager.views.monitor_ikea'),

    url(r'^wow.*dependence/$', 'etlmanager.views.dependence_wow'),
    url(r'^api.*dependence/$', 'etlmanager.views.dependence_api'),
    url(r'^racq.*dependence/$', 'etlmanager.views.dependence_racq'),
    url(r'^bookshop.*dependence/$', 'etlmanager.views.dependence_bookshop'),
    url(r'^gdt.*dependence/$', 'etlmanager.views.dependence_gdt'),
    url(r'^news.*dependence/$', 'etlmanager.views.dependence_news'),
    url(r'^spark.*dependence/$', 'etlmanager.views.dependence_spark'),
    url(r'^vmb.*dependence/$', 'etlmanager.views.dependence_vmb'),
    url(r'^vmy.*dependence/$', 'etlmanager.views.dependence_vmy'),
    url(r'^nib.*dependence/$', 'etlmanager.views.dependence_nib'),
    url(r'^paypal.*dependence/$', 'etlmanager.views.dependence_paypal'),
    url(r'^foxtel.*dependence/$', 'etlmanager.views.dependence_foxtel'),
    url(r'^ikea.*dependence/$', 'etlmanager.views.dependence_ikea'),
    
    url(r'^wow.*chart/$', 'etlmanager.views.chart_wow'),
    url(r'^api.*chart/$', 'etlmanager.views.chart_api'),
    url(r'^racq.*chart/$', 'etlmanager.views.chart_racq'),
    url(r'^bookshop.*chart/$', 'etlmanager.views.chart_bookshop'),
    url(r'^gdt.*chart/$', 'etlmanager.views.chart_gdt'),
    url(r'^news.*chart/$', 'etlmanager.views.chart_news'),
    url(r'^spark.*chart/$', 'etlmanager.views.chart_spark'),
    url(r'^vmb.*chart/$', 'etlmanager.views.chart_vmb'),
    url(r'^vmy.*chart/$', 'etlmanager.views.chart_vmy'),
    url(r'^nib.*chart/$', 'etlmanager.views.chart_nib'),
    url(r'^paypal.*chart/$', 'etlmanager.views.chart_paypal'),
    url(r'^foxtel.*chart/$', 'etlmanager.views.chart_foxtel'),
    url(r'^ikea.*chart/$', 'etlmanager.views.chart_ikea'),
    
    url(r'^wow.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^api.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^racq.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^bookshop.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^gdt.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^news.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^spark.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^vmb.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^vmy.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^nib.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^paypal.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^foxtel.*filemanager/$', 'etlmanager.views.filemanager'),
    url(r'^ikea.*filemanager/$', 'etlmanager.views.filemanager'),

    url(r'^.*check/$','etlmanager.views.check'),
]
