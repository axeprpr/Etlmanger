function my_chart(div_job_name,d1) {
    if ($(div_job_name)[0]) {
        $.plot(div_job_name, [ {
            data: d1,
            label: "Duration",
		},],

            {
                series: {
                    lines: {
                        show: true,
                        lineWidth: 1,
                        fill: 0.25,
                    },

                    color: 'rgba(255,255,255,0.7)',
                    shadowSize: 0,
                    points: {
                        show: true,
                    }
                },

                yaxis: {
                    tickColor: 'rgba(255,255,255,0.15)',
                    tickDecimals: 0,
                    font :{
                        lineHeight: 13,
                        style: "normal",
                        color: "rgba(255,255,255,0.8)",
                    },
                    shadowSize: 0,
                },
                xaxis: {
					mode: "time",
					timeformat: "%y/%m/%d",
					minTickSize:[1,"day"],
                    tickColor: 'rgba(255,255,255,0)',
                    tickDecimals: 0,
                    font :{
                        lineHeight: 13,
                        style: "normal",
                        color: "rgba(255,255,255,0.8)",
                    }
                },
                grid: {
                    borderWidth: 1,
                    borderColor: 'rgba(255,255,255,0.25)',
                    labelMargin:10,
                    hoverable: true,
                    clickable: true,
                    mouseActiveRadius:6,
                },
                legend: {
                    show: false
                }
            });
   
	}

	var div_job_name_2=div_job_name+'-tooltip'
	$(div_job_name).bind("plothover", function (event, pos, item) {
        if (item) {
            var x = new Date(item.datapoint[0]).getFullYear()+"/"+
			("00"+(new Date(item.datapoint[0]).getMonth()+1)).substr(-2)+"/"+
			("00"+(new Date(item.datapoint[0]).getDate())).substr(-2),
                y = item.datapoint[1].toFixed(2);
            $(div_job_name_2).html(item.series.label + " of " + x + " = " + y).css({top: item.pageY+5, left: item.pageX+5}).fadeIn(200);
        }
        else {
            $(div_job_name_2).hide();
        }
	
	div_job_name=div_job_name.replace("#","");
    $('<div id='+div_job_name+'-tooltip class="chart-tooltip"></div>').appendTo("body");
});

};




	
function add_chartdiv_to_body(){
	var STR="";
	var RTS="";
	var STR2="";
	RTS+='<div class="tab-container tile media"><ul class="tab pull-left tab-vertical nav nav-tabs">';
	RTS+='<li class="active"><a href="#'+JSON[0].job_name+'">'+JSON[0].job_name+'</a></li>';
	for(var q=1;q<JSON.length;q++){
	STR='<li><a href="#'+JSON[q].job_name+'">'+JSON[q].job_name+'</a></li>';	
	RTS+=STR;
	};
	RTS+='</ul>';
	RTS+= '<div class="tab-content media-body">'
	RTS+='<div class="tab-pane fade in active" id="'+JSON[0].job_name+'"><div class="col-md-8"><div class="row"><div class="tile"><h2 class="tile-title">Duration</h2><div class="p-10"><div id="'+JSON[0].job_name+'_CHART" class="main-chart" style="height: 250px"></div></div></div><table class="table tile"><thead><tr><th>batch_id</th><th>start_time</th><th>end_time</th><th>except_duration</th><th>actual_duration</th><th>status</th></tr></thead><tbody>';
	
for(var w=0;w<JSON[0].detial.length;w++){
	STR='<tr><td>'+JSON[0].detial[w].batch_id+'</td><td>'+JSON[0].detial[w].start_time+'</td><td>'+JSON[0].detial[w].end_time+'</td><td>'+JSON[0].detial[w].except_duration+'</td><td>'+JSON[0].detial[w].actual_duration+'</td><td>'+JSON[0].detial[w].status+'</td></tr>';	
	RTS+=STR;
	};
	RTS+='</tbody></table></div></div>';
	RTS+='<div class="col-md-4"><div class="tile"><h3 class="tile-title">'+JSON[0].job_name+'</h3>';
	RTS+='<div class="tile text-center"><div class="pie-chart-tiny" data-percent="'+JSON[0].percent+'"><span class="percent"></span></div></div></div><table class="table tile"><thead><tr><th>DEPENDENCE_NAME</th><th>DEPENDENCE_TYPE</th><th>DEPENDENCE_OFFSET</th></tr></thead><tbody>';
	for(var e=0;e<JSON[0].dependence.length;e++){
	STR='<tr><td>'+JSON[0].dependence[e].dependence_name+'</td><td>'+JSON[0].dependence[e].dependence_type+'</td><td>'+JSON[0].dependence[e].dependence_offset+'</td></tr>';
	RTS+=STR;
	}
	RTS+='</tbody></table></div></div>'
	for(var r=1;r<JSON.length;r++){
		RTS+='<div class="tab-pane fade" id="'+JSON[r].job_name+'"><div class="col-md-8"><div class="row"><div class="tile"><h2 class="tile-title">Duration</h2><div class="p-10"><div id="'+JSON[r].job_name+'_CHART" class="main-chart" style="height: 250px"></div></div></div><table class="table tile"><thead><tr><th>batch_id</th><th>start_time</th><th>end_time</th><th>except_duration</th><th>actual_duration</th><th>status</th></tr></thead><tbody>';
	for(var t=0;t<JSON[r].detial.length;t++){
	STR='<tr><td>'+JSON[r].detial[t].batch_id+'</td><td>'+JSON[r].detial[t].start_time+'</td><td>'+JSON[r].detial[t].end_time+'</td><td>'+JSON[r].detial[t].except_duration+'</td><td>'+JSON[r].detial[t].actual_duration+'</td><td>'+JSON[r].detial[t].status+'</td></tr>';	
	RTS+=STR;
	};
	RTS+='</tbody></table></div></div>';
	RTS+='<div class="col-md-4"><div class="tile"><h3 class="tile-title">'+JSON[r].job_name+'</h3>';
	RTS+='<div class="tile text-center"><div class="pie-chart-tiny" data-percent="'+JSON[r].percent+'"><span class="percent"></span></div></div></div><table class="table tile"><thead><tr><th>DEPENDENCE_NAME</th><th>DEPENDENCE_TYPE</th><th>DEPENDENCE_OFFSET</th></tr></thead><tbody>';
	for(var y=0;y<JSON[r].dependence.length;y++){
	STR='<tr><td>'+JSON[r].dependence[y].dependence_name+'</td><td>'+JSON[r].dependence[y].dependence_type+'</td><td>'+JSON[r].dependence[y].dependence_offset+'</td></tr>';
	RTS+=STR;	
	};
	RTS+='</tbody></table></div></div>';				
	};
	RTS+='</div></div>';
	$("#mychart").append(RTS);
	
$(function() {
    $('.pie-chart-tiny').easyPieChart({
        easing: 'easeOutBounce',
        barColor: 'rgba(255,255,255,0.75)',
        trackColor: 'rgba(0,0,0,0.3)',
        scaleColor: 'rgba(255,255,255,0.3)',
        lineCap: 'square',
        lineWidth: 4,
        size: 100,
        animate: 3000,
        onStep: function(from, to, percent) {
            $(this.el).find('.percent').text(Math.round(percent));
        }
    });

    var chart = window.chart = $('.pie-chart-tiny').data('easyPieChart');
});
};

add_chartdiv_to_body();

$(document).ready(function(){
for (var u=0;u<JSON.length;u++){
	var d1=new Array();
	var div_job_name='#'+JSON[u].job_name+'_CHART';
	for (var i=0;i<JSON[u].detial.length;i++){
	var str_date=JSON[u].detial[i].batch_id;
	str_date=str_date.substr(0,4)+'/'+str_date.substr(4,2)+'/'+str_date.substr(6,2);	//alert(str_date2);
	str_date=new Date(Date.parse(str_date));
	
	d1[i]=[str_date,JSON[u].detial[i].actual_duration];
	};
	my_chart(div_job_name,d1);
};
});
