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

CURSOR c_job IS select *  from DELTA_SLA_LOAD_LOG a where (not exists (select * from DELTA_SLA_LOAD_LOG b where b.process=a.process and b.file_timestamp > a.file_timestamp)) and process in (select process from etl_duration) order by a.process;
BEGIN
    dbms_output.put_line('[');
    FOR c_row IN c_job LOOP
        select replace(c_row.process,' ','_') into job_name from dual; 
        dbms_output.put_line('{"job_name":"'||job_name||'",');      
        IF REGEXP_LIKE(c_row.STATUS,'SUCC|COMPLETE|Exceptions','i') THEN
            percent:='100';
        ELSIF REGEXP_LIKE(c_row.STATUS,'FAIL','i') THEN
            percent:='-1';
        ELSE
            select trunc(((sysdate-to_date(to_char(c_row.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4) into temp_a from dual;
            select duration into temp_b from etl_duration where process=c_row.process;
            percent:=trunc((to_number(temp_a)/to_number(temp_b)),4)*100;

        END IF;
        dbms_output.put_line('"percent":"'||percent||'",');
        dbms_output.put_line('"dependence":[');
        dbms_output.put_line('{"dependence_name":"","dependence_type":"","dependence_offset":""},');
        dbms_output.put_line('],');
        dbms_output.put_line('"detial":[');
            for c_row3 IN (select * from (select * from DELTA_SLA_LOAD_LOG where process=c_row.process order by file_timestamp desc) where rownum<=15) LOOP
                 IF REGEXP_LIKE(c_row.STATUS,'SUCC|COMPLETE|Exceptions','i') THEN
                    select
                    to_char(c_row3.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
                    to_char(c_row3.END_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
                    trunc(((to_date(to_char(c_row3.END_DATETIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss')-to_date(to_char(c_row3.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4),
                    to_char(c_row3.FILE_TIMESTAMP,'yyyymmdd'),
                    c_row3.STATUS
                    into 
                    start_time,end_time,actual_duration,batch_id,status from dual;
                    select duration into except_duration from etl_duration where process=c_row.process;
                    dbms_output.put_line('{"batch_id":"'||batch_id||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","status":"'||status||'"},');
                ELSIF REGEXP_LIKE(c_row.STATUS,'FAIL','i') THEN
                    actual_duration:='-1';
                    select
                    to_char(c_row3.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
                    to_char(c_row3.END_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
                    to_char(c_row3.FILE_TIMESTAMP,'yyyymmdd'),
                    c_row3.STATUS
                    into 
                    start_time,end_time,batch_id,status from dual;
                    select duration into except_duration from etl_duration where process=c_row.process;            
                    dbms_output.put_line('{"batch_id":"'||batch_id||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","status":"'||status||'"},');
                ELSE
                    select
                    to_char(c_row3.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
                    to_char(c_row3.END_DATETIME,'yyyy-mm-dd hh24:mi:ss'),
                    trunc(((sysdate-to_date(to_char(c_row3.START_DATETIME,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*24),4),
                    to_char(c_row3.FILE_TIMESTAMP,'yyyymmdd'),
                    c_row3.STATUS
                    into 
                    start_time,end_time,actual_duration,batch_id,status from dual;
                    select duration into except_duration from etl_duration where process=c_row.process;
                    dbms_output.put_line('{"batch_id":"'||batch_id||'","start_time":"'||start_time||'","end_time":"'||end_time||'","except_duration":"'||except_duration||'","actual_duration":"'||actual_duration||'","status":"'||status||'"},');

                END IF;
            END LOOP;
            dbms_output.put_line('],},');
    END LOOP;
            dbms_output.put_line(']');
END ETL_REPORT;
commit;



