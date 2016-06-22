var d=new Array()
 d[0] = []
 d[1] = ["1","2"]
 d[2] = ["daily"]
 d[3] = ["daily"]
 d[4] = ["daily","PC","PR","PD"]
 d[5] = ["daily"]
 d[6] = ["daily","web"]
 d[7] = ["daily"]
 d[8] = ["daily","rpt","ms_rp"]
 d[9] = ["daily","ccs","blue"]
 d[10] = ["ctdaily","ctweekly","travel"]
 d[11] = ["daily","nps"]
 d[12] = ["daily","CDR"]
function setMajor(){  
    var client_name = $("[name = client_name]").val();  
    var addto = $("[name = addto]");  
    if(client_name!=-1){  
        addto.empty();  
		for(i=0;i<d[client_name].length;i++){  
        var o = new Option(d[client_name][i],i+1);  
        addto.append(o); 
        }
    } else {  
    addto.empty();  
    }  
    } 

$(document).ready(function(){
$("#summit").click(function(){
var c1=$('#client_name option:selected').text()
var c2=$('#addto option:selected').text()
var c3=$("input[id='timestamp']").val()
alert('test')
$.get("check/",{
'c1':c1,
'c2':c2,
'c3':c3
}
,function(ret){
$('#check').html(ret)
});
});
});

	
