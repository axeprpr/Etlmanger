$(document).ready(function(){
        // function for Mornitring.
        var STR="";
        var RTS="";
        RTS+='<div class="table-responsive overflow"><table class="tile table table-bordered table-striped"><thead><tr><th>Job Name</th><th>Processing</th><th>StartTime</th><th>EndTime</th><th>ExceptDuration</th><th>Actual_Duration</th><th>Percent</th><th>BatchID</th><th>Status</th></tr></thead><tbody>'
        for(var k=0;k<JSON.length;k++){
                if(JSON[k].percent<0){
                        JSON[k].percent=100;
                        STR='<tr><td>'+JSON[k].job_name+'</td><td><div class="progress progress-small"><a data-toggle="tooltip" title="" class="tooltips progress-bar progress-bar-danger" style="width: '+JSON[k].percent+'%;" data-original-title="'+JSON[k].percent+'%"><span class="sr-only">'+JSON[k].percent+'% Completed</span></a></div></td><td>'+JSON[k].start_time+'</td><td>'+JSON[k].end_time+'</td><td>'+JSON[k].except_duration+'  hours</td><td>'+JSON[k].actual_duration+' hours</td><td>'+JSON[k].percent+'%</td><td>'+JSON[k].batch_id+'</td><td>'+JSON[k].status+'</td></tr>';
                }else if(JSON[k].percent>100){
                        JSON[k].percent=100;
                        STR='<tr><td>'+JSON[k].job_name+'</td><td><div class="progress progress-small"><a data-toggle="tooltip" title="" class="tooltips progress-bar progress-bar-warning" style="width: '+JSON[k].percent+'%;" data-original-title="'+JSON[k].percent+'%"><span class="sr-only">'+JSON[k].percent+'% Completed</span></a></div></td><td>'+JSON[k].start_time+'</td><td>'+JSON[k].end_time+'</td><td>'+JSON[k].except_duration+'  hours</td><td>'+JSON[k].actual_duration+' hours</td><td>'+JSON[k].percent+'%</td><td>'+JSON[k].batch_id+'</td><td>'+JSON[k].status+'</td></tr>';
                }else{
                        STR='<tr><td>'+JSON[k].job_name+'</td><td><div class="progress progress-small"><a data-toggle="tooltip" title="" class="tooltips progress-bar progress-bar-success" style="width: '+JSON[k].percent+'%;" data-original-title="'+JSON[k].percent+'%"><span class="sr-only">'+JSON[k].percent+'% Completed</span></a></div></td><td>'+JSON[k].start_time+'</td><td>'+JSON[k].end_time+'</td><td>'+JSON[k].except_duration+'  hours</td><td>'+JSON[k].actual_duration+' hours</td><td>'+JSON[k].percent+'%</td><td>'+JSON[k].batch_id+'</td><td>'+JSON[k].status+'</td></tr>';
                };
        RTS+=STR;
        };
        RTS+='</tbody></table></div>';
        $("#status").append(RTS);
})

