from django.utils.safestring import SafeString
import json
import os
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def monitor_racq(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh racq_fi etl_manager`').read()
	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/racq.jpg",
        'client':"RACQ",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/RACQ/RACQ+Home",
        'json_monitor':json_monitor
        })

def monitor_wow(request):
    	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh woolworths etl_manager`').read()
	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/wow.jpg",
        'client':"Woolworths",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/WOW/Woolworths+Limited+Home",
	'json_monitor':json_monitor
	})

def monitor_api(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh api_full_impl etl_manager`').read()
    	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/api.jpg",
        'client':"api",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/API/API+%28Priceline%29+Home",
 	'json_monitor':json_monitor
	 })

def monitor_paypal(request):
    	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh paypal etl_manager`').read()
    	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/paypal.jpg",
        'client':"paypal",
        'server':"@tengri",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/PAYP/PayPal+Home",
	'json_monitor':json_monitor,
  })

def monitor_ikea(request):
    	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh ikea etl_manager`').read()
   	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/ikea.jpg",
        'client':"ikea",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/IKEA/IKEA+Home",
	'json_monitor':json_monitor,
  })

def monitor_foxtel(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh foxtel etl_manager`').read()
    	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/foxtel.jpg",
        'client':"foxtel",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/FOX/Foxtel+Home",
	'json_monitor':json_monitor,
  })

def monitor_spark(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh dmxuser etl_manager`').read()
    	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/spark.jpg",
        'client':"spark",
        'server':"@thor",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/SPK/Spark+Home",
	'json_monitor':json_monitor,
  })

def monitor_gdt(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh gdt etl_manager`').read()
	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/gdt.jpg",
        'client':"gdt",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/pages/viewpage.action?pageId=17138129",
	'json_monitor':json_monitor,  
})

def monitor_nib(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh nib etl_manager`').read()
	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/nib.jpg",
        'client':"nib",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/pages/viewpage.action?pageId=17138129",
	'json_monitor':json_monitor, 
})

def monitor_vmb(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh vmobile_fi etl_manager`').read()
    	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/vmb.jpg",
        'client':"vmb",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/VB/Virgin+Mobile+Home",
	'json_monitor':json_monitor, 
})

def monitor_vmy(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh vmoney etl_manager`').read()
	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/vmy.jpg",
        'client':"vmy",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/VMON/Virgin+Money+Home",
	'json_monitor':json_monitor,
  })

def monitor_news(request):
	json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh news_care etl_manager`').read()
    	return render(request, 'monitor.html',{
        'logo':"/static/img/logo/news.jpg",
        'client':"news",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/NEWS/News+Limited+Home",
	'json_monitor':json_monitor, 
})

def monitor_bookshop(request):
        json_monitor=os.popen('echo `/home/axe.xu/etlmanager.sh bookshop etl_manager`').read()
        return render(request, 'monitor.html',{
        'logo':"/static/img/logo/coop.jpg",
        'client':"Bookshop",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/COOP/CO-OP+Home",
        'json_monitor':json_monitor,
})


#CHART

def chart_racq(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh racq_fi etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/racq.jpg",
        'client':"RACQ",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/RACQ/RACQ+Home",
        'json_report':json_report
        })

def chart_wow(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh woolworths etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/wow.jpg",
        'client':"Woolworths",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/WOW/Woolworths+Limited+Home",
        'json_report':json_report
        })

def chart_api(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh api_full_impl etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/api.jpg",
        'client':"api",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/API/API+%28Priceline%29+Home",
        'json_report':json_report
         })

def chart_paypal(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh paypal etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/paypal.jpg",
        'client':"paypal",
        'server':"@tengri",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/PAYP/PayPal+Home",
        'json_report':json_report,
  })

def chart_ikea(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh ikea etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/ikea.jpg",
        'client':"ikea",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/IKEA/IKEA+Home",
        'json_report':json_report,
  })

def chart_foxtel(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh foxtel etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/foxtel.jpg",
        'client':"foxtel",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/FOX/Foxtel+Home",
        'json_report':json_report,
  })

def chart_spark(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh dmxuser etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/spark.jpg",
        'client':"spark",
        'server':"@thor",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/SPK/Spark+Home",
        'json_report':json_report,
  })

def chart_gdt(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh gdt etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/gdt.jpg",
        'client':"gdt",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/pages/viewpage.action?pageId=17138129",
        'json_report':json_report,
})

def chart_nib(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh nib etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/nib.jpg",
        'client':"nib",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/pages/viewpage.action?pageId=17138129",
        'json_report':json_report,
})

def chart_vmb(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh vmobile_fi etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/vmb.jpg",
        'client':"vmb",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/VB/Virgin+Mobile+Home",
        'json_report':json_report,
})

def chart_vmy(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh vmoney etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/vmy.jpg",
        'client':"vmy",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/VMON/Virgin+Money+Home",
        'json_report':json_report,
  })

def chart_news(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh news_care etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/news.jpg",
        'client':"news",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/NEWS/News+Limited+Home",
        'json_report':json_report,
})

def chart_bookshop(request):
        json_report=os.popen('echo `/home/axe.xu/etlmanager.sh bookshop etl_report`').read()
        return render(request, 'chart.html',{
        'logo':"/static/img/logo/coop.jpg",
        'client':"Bookshop",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/COOP/CO-OP+Home",
        'json_report':json_report,
})

#dependence
def dependence_racq(request):
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/racq.jpg",
        'client':"RACQ",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/RACQ/RACQ+Home",
        'dependence':"/static/img/dependence/dependence_racq.jpg"
        })

def dependence_wow(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/wow.jpg",
        'client':"Woolworths",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/WOW/Woolworths+Limited+Home",
        'dependence':"/static/img/dependence/dependence_wow.jpg"
        })

def dependence_api(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/api.jpg",
        'client':"api",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/API/API+%28Priceline%29+Home",
        'dependence':"/static/img/dependence/dependence_api.jpg"
         })

def dependence_paypal(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/paypal.jpg",
        'client':"paypal",
        'server':"@tengri",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/PAYP/PayPal+Home",
        'dependence':"/static/img/dependence/dependence_paypal.jpg",
  })

def dependence_ikea(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/ikea.jpg",
        'client':"ikea",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/IKEA/IKEA+Home",
        'dependence':"/static/img/dependence/dependence_ikea.jpg",
  })

def dependence_foxtel(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/foxtel.jpg",
        'client':"foxtel",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/FOX/Foxtel+Home",
        'dependence':"/static/img/dependence/dependence_foxtel.jpg",
  })

def dependence_spark(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/spark.jpg",
        'client':"spark",
        'server':"@thor",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/SPK/Spark+Home",
        'dependence':"/static/img/dependence/dependence_spark.jpg",
  })

def dependence_gdt(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/gdt.jpg",
        'client':"gdt",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/pages/viewpage.action?pageId=17138129",
        'dependence':"/static/img/dependence/dependence_gdt.jpg",
})

def dependence_nib(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/nib.jpg",
        'client':"nib",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/pages/viewpage.action?pageId=17138129",
        'dependence':"/static/img/dependence/dependence_nib.jpg",
})

def dependence_vmb(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/vmb.jpg",
        'client':"vmb",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/VB/Virgin+Mobile+Home",
        'dependence':"/static/img/dependence/dependence_vmb.jpg",
})

def dependence_vmy(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/vmy.jpg",
        'client':"vmy",
        'server':"@colossus",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/VMON/Virgin+Money+Home",
        'dependence':"/static/img/dependence/dependence_vmy.jpg",
  })

def dependence_news(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/news.jpg",
        'client':"news",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/NEWS/News+Limited+Home",
        'dependence':"/static/img/dependence/dependence_news.jpg",
})

def dependence_bookshop(request):
        
        return render(request, 'dependence.html',{
        'logo':"/static/img/logo/coop.jpg",
        'client':"Bookshop",
        'server':"@poseidon",
        'manual':"https://davinci.digitalalchemy.net.au:8443/display/COOP/CO-OP+Home",
        'dependence':"/static/img/dependence/dependence_coop.jpg",
})

def filemanager(request):
        return render(request, 'filemanager.html',{
        'logo':"/static/img/logo/axe.jpg",
        'client':"helloworld",
        'server':"@gizmo",
        'manual':"#",
})

def check(request):
	c1=request.GET['c1']
	c2=request.GET['c2']
	c3=request.GET['c3']
	return  HttpResponse(c1)
