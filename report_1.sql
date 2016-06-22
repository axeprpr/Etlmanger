
CREATE OR REPLACE PROCEDURE ETL_REPORT IS
job_name VARCHAR2(50);
start_time varchar2(50);
end_time varchar2(50);
except_duration varchar2(50);
actual_duration varchar2(50);
current_status varchar2(50);
batch_id varchar2(50);
percent varchar2(50);
status varchar2(50);

dependence_name varchar2(50);
dependence_type varchar2(50);
dependence_offset varchar2(50);
temp_a varchar2(20);
temp_b varchar2(20);
temp_c varchar2(20);
temp_d varchar2(20);
temp_e varchar2(20);

CURSOR c_job IS select * from job_running_monitor a where (not exists (select * from job_running_monitor b where b.job_name=a.job_name and b.batch_id > a.batch_id)) and job_name in (select job_name from etl_duration) order by a.job_name;
BEGIN
    dbms_output.put_line('[');
    FOR c_row IN c_job LOOP
        job_name:=c_row.job_name;
        dbms_output.put_line('{"job_name":"'||job_name||'",');      
        IF c_row.STATUS='COMPLETED' THEN
            percent:='100';
            ELSIF REGEXP_LIKE(c_row.STATUS,'RUNNING|PENDING','i') THEN
            select trunc(((sysdate-to_date(to_char(c_row.START_TIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4) into temp_a from dual;
            select duration into temp_b from etl_duration where job_name=c_row.JOB_NAME;
            percent:=trunc((to_number(temp_a)/to_number(temp_b)),4)*100;
        ELSIF c_row.STATUS='FAILED' THEN
            percent:='-1';
        END IF;
        dbms_output.put_line('"percent":"'||percent||'",');
        dbms_output.put_line('"dependence":[');
            FOR c_row2 IN (select * from job_dependence where job_name=c_row.job_name) LOOP
            select c_row2.dependence_name,c_row2.dependence_type,c_row2.dependence_offset into dependence_name,dependence_type,dependence_offset from dual;
            dbms_output.put_line('{"dependence_name":"'||dependence_name||'","dependence_type":"'||dependence_type||'","dependence_offset":"'||dependence_offset||'"},');
            END LOOP;
        dbms_output.put_line('],');
        dbms_output.put_line('"detial":[');
            for c_row3 IN (select * from (select * from job_running_monitor where job_name=c_row.job_name order by batch_id desc) where rownum<=15) LOOP
                IF c_row3.STATUS='COMPLETED' THEN
                    select
                    to_char(c_row3.START_TIME,'yyyy-mm-dd hh24:mi:ss'),
                    to_char(c_row3.END_TIME,'yyyy-mm-dd hh24:mi:ss'),
                    trunc(((to_date(to_char(c_row3.END_TIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss')-to_date(to_char(c_row3.START_TIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4),
                    substr(c_row3.BATCH_ID,0,8),
                    c_row3.STATUS
                    into 
                    start_time,end_time,actual_duration,batch_id,status from dual;
                    select duration into except_duration from etl_duration where job_name=c_row.JOB_NAME;
                    dbms_output.put_line('{"batch_id":"'||batch_id||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","status":"'||status||'"},');
                ELSIF c_row3.STATUS='RUNNING' THEN
                    select
                    to_char(c_row3.START_TIME,'yyyy-mm-dd hh24:mi:ss'),
                    to_char(c_row3.END_TIME,'yyyy-mm-dd hh24:mi:ss'),
                    trunc(((sysdate-to_date(to_char(c_row3.START_TIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4),
                    substr(c_row3.BATCH_ID,0,8),
                    c_row3.STATUS
                    into 
                    start_time,end_time,actual_duration,batch_id,status from dual;
                    select duration into except_duration from etl_duration where job_name=c_row.JOB_NAME;
                    dbms_output.put_line('{"batch_id":"'||batch_id||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","status":"'||status||'"},');
                ELSIF c_row3.STATUS='FAILED' THEN
                    actual_duration:='-1';
                    select
                    to_char(c_row3.START_TIME,'yyyy-mm-dd hh24:mi:ss'),
                    to_char(c_row3.END_TIME,'yyyy-mm-dd hh24:mi:ss'),
                    substr(c_row3.BATCH_ID,0,8),
                    c_row3.STATUS
                    into 
                    start_time,end_time,batch_id,status from dual;
                    select duration into except_duration from etl_duration where job_name=c_row.JOB_NAME;            
                    dbms_output.put_line('{"batch_id":"'||batch_id||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","status":"'||status||'"},');
                END IF;
            END LOOP;
            dbms_output.put_line('],},');
    END LOOP;
            dbms_output.put_line(']');
END ETL_REPORT;

