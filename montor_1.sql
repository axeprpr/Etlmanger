CREATE OR REPLACE PROCEDURE ETL_MANAGER IS
job_name VARCHAR2(50);
start_time varchar2(50);
end_time varchar2(50);
except_duration varchar2(50);
actual_duration varchar2(50);
percent varchar2(50);
batch_id varchar2(50);
status varchar2(50);
CURSOR c_job IS 
select *  from job_running_monitor a where (not exists (select * from job_running_monitor b where b.job_name=a.job_name and b.batch_id > a.batch_id)) and job_name in (select job_name from etl_duration) order by a.job_name;
BEGIN
    dbms_output.put_line('[');
    FOR c_row IN c_job LOOP
        IF c_row.STATUS='COMPLETED' THEN
            percent:='100';
            select c_row.JOB_NAME,
            to_char(c_row.START_TIME,'yyyy-mm-dd hh24:mi:ss'),
            to_char(c_row.END_TIME,'yyyy-mm-dd hh24:mi:ss'),
            trunc(((to_date(to_char(c_row.END_TIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss')-to_date(to_char(c_row.START_TIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4),
            substr(c_row.BATCH_ID,0,8),
            c_row.STATUS
            into 
            job_name,start_time,end_time,actual_duration,batch_id,status from dual;
            select duration into except_duration from etl_duration where job_name=c_row.JOB_NAME;
            dbms_output.put_line('{"job_name":"'||job_name||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","percent":"'||percent||'","batch_id":"'||batch_id||'","status":"'||status||'"},');
            ELSIF REGEXP_LIKE(c_row.STATUS,'RUNNING|PENDING','i') THEN
            select c_row.JOB_NAME,
            to_char(c_row.START_TIME,'yyyy-mm-dd hh24:mi:ss'),
            to_char(c_row.END_TIME,'yyyy-mm-dd hh24:mi:ss'),
            trunc(((sysdate-to_date(to_char(c_row.START_TIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4),
            substr(c_row.BATCH_ID,0,8),
            c_row.STATUS
            into 
            job_name,start_time,end_time,actual_duration,batch_id,status from dual;
            select duration into except_duration from etl_duration where job_name=c_row.JOB_NAME;
            percent:=trunc((to_number(actual_duration)/to_number(except_duration)),4)*100;
            dbms_output.put_line('{"job_name":"'||job_name||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","percent":"'||percent||'","batch_id":"'||batch_id||'","status":"'||status||'"},');
        ELSIF c_row.STATUS='FAILED' THEN
            actual_duration:='-1';
            percent:='-1';
            select c_row.JOB_NAME,
            to_char(c_row.START_TIME,'yyyy-mm-dd hh24:mi:ss'),
            to_char(c_row.END_TIME,'yyyy-mm-dd hh24:mi:ss'),
            substr(c_row.BATCH_ID,0,8),
            c_row.STATUS
            into 
            job_name,start_time,end_time,batch_id,status from dual;
            select duration into except_duration from etl_duration where job_name=c_row.JOB_NAME;            
            dbms_output.put_line('{"job_name":"'||job_name||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","percent":"'||percent||'","batch_id":"'||batch_id||'","status":"'||status||'"},');            
        END IF;
    END LOOP;
    dbms_output.put_line(']');
END ETL_MANAGER;
