

JSON_update={'message':'<big>Summary:</big><br><p class="t-overflow">This website is used to monitor the ETL process, check the load status, check the missing files for each load.<br>And also, it will generate some reports by a period of time operation.<br>I hope it will bring you the convenience. More functions, such as log analyze, will be realized in the future.<br>If you have any questions or suggestions, please contact me:<br></p><a class="t-overflow">Yim: axeprpr</a><a class="t-overflow" href="mailto:Axe.Xu@digitalalchemy.asia">Email:  Axe.Xu@digitalalchemy.asia</a><br><p class="t-overflow"><br>Enjoy it! :)</p>',
'update':[{'time':'Axe.Xu - Mon Apr 25 05:19:28 AEST 2016','content':'Test this function'},]
}

$(document).ready(function(){
var STR_update=''
var RTS_update=''
for(var C_update=0;C_update<JSON_update.update.length;C_update++){
STR_update='<div class="media"><div class="media-body"><small class="text-muted">'+JSON_update.update[C_update].time+'</small><br><a class="t-overflow" href="">'+JSON_update.update[C_update].content+'</a></div></div>'
RTS_update+=STR_update
}
$("#summary").append(JSON_update.message);
$("#update").append(RTS_update);

})
