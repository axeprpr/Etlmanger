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
select *  from DELTA_SLA_LOAD_LOG a where (not exists (select * from DELTA_SLA_LOAD_LOG b where b.process=a.process and b.file_timestamp > a.file_timestamp)) and process in (select process from etl_duration) order by a.process;
BEGIN
    dbms_output.put_line('[');
    FOR c_row IN c_job LOOP
        IF REGEXP_LIKE(c_row.STATUS,'SUCC|COMPLETE|Exceptions','i') THEN
            percent:='100';
            select replace(c_row.process,' ','_'),
            to_char(c_row.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
            to_char(c_row.END_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
            trunc(((to_date(to_char(c_row.END_DATETIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss')-to_date(to_char(c_row.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4),
            to_char(c_row.FILE_TIMESTAMP,'yyyymmdd'),
            c_row.STATUS
            into 
            job_name,start_time,end_time,actual_duration,batch_id,status from dual;
            select duration into except_duration from etl_duration where process=c_row.process;
            dbms_output.put_line('{"job_name":"'||job_name||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","percent":"'||percent||'","batch_id":"'||batch_id||'","status":"'||status||'"},');
        ELSIF REGEXP_LIKE(c_row.STATUS,'FAIL','i') THEN
            actual_duration:='-1';
            percent:='-1';
            select c_row.process,
            to_char(c_row.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
            to_char(c_row.END_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
            to_char(c_row.FILE_TIMESTAMP,'yyyymmdd'),
            c_row.STATUS
            into 
            job_name,start_time,end_time,batch_id,status from dual;
            select duration into except_duration from etl_duration where process=c_row.process;            
            dbms_output.put_line('{"job_name":"'||job_name||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","percent":"'||percent||'","batch_id":"'||batch_id||'","status":"'||status||'"},'); 
        ELSE
            select c_row.process,
            to_char(c_row.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
            to_char(c_row.END_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
            trunc(((sysdate-to_date(to_char(c_row.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4),
            to_char(c_row.FILE_TIMESTAMP,'yyyymmdd'),
            c_row.STATUS
            into 
            job_name,start_time,end_time,actual_duration,batch_id,status from dual;
            select duration into except_duration from etl_duration where process=c_row.process;
            percent:=trunc((to_number(actual_duration)/to_number(except_duration)),4)*100;
            dbms_output.put_line('{"job_name":"'||job_name||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","percent":"'||percent||'","batch_id":"'||batch_id||'","status":"'||status||'"},');                  
        END IF;
    END LOOP;
    dbms_output.put_line(']');
END ETL_MANAGER;
