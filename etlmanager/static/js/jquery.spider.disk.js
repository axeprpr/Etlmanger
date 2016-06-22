var data1={ClientName:'RACQ',ServerName:'Host2',CheckDate:'10:00:00',disks:[
{id:'10000',name:'RCQ_DAILY_EDW_ET',value:'-1',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10001',name:'RCQ_DAILY_EDW_LOAD',value:'102',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10002',name:'RCQ_DAILY_GR_LOAD',value:'10',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10003',name:'RCQ_DAILY_DR_LOAD',value:'55',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10004',name:'RCQ_DAILY_RPT_DATAMART_ET',value:'32',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10010',name:'RCQ_DAILY_RESPONSE_LOAD',value:'54',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10005',name:'RCQ_DAILY_RPT_ETL',value:'99',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10006',name:'RCQ_DAILY_COREMETRIC_ET',value:'33',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10007',name:'RCQ_DAILY_COREMETRIC_LOAD',value:'111',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10008',name:'RCQ_PROD_D_CH_EXTRACT',value:'322',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10009',name:'RCQ_PROD_D_OTM_TRIGGER',value:'120',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10010',name:'RCQ_PROD_D_DM_TRIGGER',value:'32',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10011',name:'RCQ_PROD_D_ENG_ET',value:'88',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10012',name:'RCQ_PROD_D_ENG_LOAD',value:'99',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10013',name:'RCQ_PROD_D_M_EDW_PROCESS',value:'66',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10014',name:'RCQ_COS',value:'10',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10015',name:'RCQ_WEEKLY_EDW_LOAD',value:'77',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10016',name:'RCQ_WEEKLY_GR_LOAD',value:'10',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10017',name:'RCQ_MONTHLY_DR_VISA_LOAD',value:'100',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
{id:'10018',name:'RCQ_MONTHLY_DR_LOAD',value:'100',expect_start_time:'10:00:00',duration:'6',actual_start_time:'10:00:00'},
]}; 

$(document).ready(function(){
	refresh(data1);
});
function refresh(data){
	$("#status").disk("poll1",{
		title:'LOAD_STATS',
		//titleColor:'#ff6600',
		width:'100%',
		data:data
	});	
}



var options;
(function ($){
	var defaults = {
		title:null,				
		titleColor:'#999',
		titleFontSize:'13px',
		width:'100%',			
		speed:1000,				
		data:[],				//datejson
		itemStyle:{
			fontSize:'12px',
			bgColor:'#E6E6E6',
			borderColor:'#BCBCBC',
			normalBgColor:'#26A0DA',
            failedBgColor:'#F50000',
			waringBgColor:'#FFFF00',
		}
	};
	
	$.fn.disk = function (id,options){
		$(this).children().remove();
		options = $.extend(defaults,options);
		var dataObj = options.data;
		var o = this;
		var total=0;
		$.each(dataObj.disks,function (i,n){
			total+=parseInt(n.value);
		});
		//alert(JSON.stringify($(this).find("<table>")));
		//$(this).find("<table>").remove();
		$(this).append("<table id='"+id+"' class='tb-disk-list' cellpadding='0' cellspacing='0' style='font-size:"+options.itemStyle.fontSize+";' width='"+defaults.width+"'></table>");
		if(null != options.title){
			$("table",this).append("<tr><td colspan='3' align='left'><span style='color:"+options.titleColor+";font-size:"+options.titleFontSize+";'>"+options.title+"</span></td>"
									  +"<td colspan='3' align='left'><span style='color:"+options.titleColor+";font-size:"+options.titleFontSize+";'>ClientName:<span id='ClientName' style='color: red'> "+dataObj.ClientName+"</span> ServerName:<span  style='color: red;'> "+dataObj.ServerName+" </span> CheckDate:<span style='color: red;'> "+dataObj.CheckDate+" </span></span></td></tr>");			
		} 
		
		var itemDiv="";
		var trs="";
		$.each(dataObj.disks,function (i,n){
		    var index=0;
			var percentage = (n.value*1).toFixed(2);
			if(isNaN(percentage)){
				percentage=0;
			}
			var percentage_tmp=percentage;
			var imgWidth = parseFloat(percentage);
			if(imgWidth)
			{
				if(i>(options.itelTotal-1))
					index = i-(options.itelTotal-1);
				else{
					index = i;
					itemDiv="<div style='border:1px solid "+ options.itemStyle.borderColor+";background-color:"+options.itemStyle.bgColor+";font-size:"+options.itemStyle.fontSize+"'>";
					if(percentage>100){
						percentage=100;
						imgWidth = parseFloat(percentage);
						itemDiv+="<div divWidth='"+imgWidth+"' style='width:0%;height:28px;background-color:"+options.itemStyle.waringBgColor+";' class='poll_plan"+index+"' >";
						itemDiv+="<div class='plan_e' style='background-color:"+options.itemStyle.waringBgColor+";'><div class='plan_c'  style='background-color:"+options.itemStyle.waringBgColor+";'></div></div>";
					}else if(percentage<0){										
						percentage=100;
						imgWidth = parseFloat(percentage);
						itemDiv+="<div divWidth='"+imgWidth+"' style='width:0%;height:28px;background-color:"+options.itemStyle.failedBgColor+";' class='poll_plan"+index+"' >";
						itemDiv+="<div class='plan_e' style='background-color:"+options.itemStyle.failedBgColor+";'><div class='plan_c'  style='background-color:"+options.itemStyle.normalBgColor+";'></div></div>";
					}else{
						itemDiv+="<div divWidth='"+imgWidth+"' style='width:0%;height:28px;background-color:"+options.itemStyle.normalBgColor+";' class='poll_plan"+index+"' >";
						itemDiv+="<div class='plan_e' style='background-color:"+options.itemStyle.normalBgColor+";'><div class='plan_c'  style='background-color:"+options.itemStyle.normalBgColor+";'></div></div>";
					}
					itemDiv+="</div>";
					itemDiv+="</div>";
			
				}
			}
			else{
				itemDiv='';
			}
			//"<tr></tr>"
			var tds="<td width='10%' height='28px' align='center'><strong>"+n.name+"</strong></td><td width='30%' style='bgcolor:"+options.itemStyle.bgColor+";'>"+itemDiv+"</td><td width='15%'>Expect Start Time:"+n.expect_start_time+"</td><td width='15%'>Expect Duration:"+n.duration+" Hours</td><td width='15%'>Actual Start Time:"+n.actual_start_time+"</td><td width='10%'>"+percentage_tmp+"% Completed.</td>";
				i--;
				trs+="<tr>"+tds;
			
		});
	//	if(dataObj.disks.length%2==1){
		//	trs+="<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>";	
		//}
		$("table",o).append(trs);
		$("div",o).each(function(i,n){
			if($(n).attr('divWidth'))
			{
				$(n).animate( { width: $(n).attr('divWidth')+'%'}, options.speed );
				$(n).removeAttr("divWidth");
			}
		});
		return this;
	};
})(jQuery);