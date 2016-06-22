# Etlmanger
This website develop to monitor the ETL process of my company.
Each ETL process will record its status into a table called JOB_RUNNING_MONITOR. So I write two procedures in database to transform the data from table to JSON.
Here is the structure of this table:
```
SQL> desc job_running_monitor;
 Name					   Null?    Type
 ----------------------------------------- -------- ----------------------------
 JOB_NAME				   NOT NULL VARCHAR2(50)
 START_TIME					    TIMESTAMP(6)
 END_TIME					    TIMESTAMP(6)
 STATUS 					    VARCHAR2(20)
 BATCH_ID				   NOT NULL VARCHAR2(20)
```
Then```monitor_1.sql``` generates data like this:
```
SQL> set serveroutput on
SQL> set line 300
SQL> exec etl_manager;
[
{"job_name":"A","start_time":"2016-06-02 03:30:22","end_time":"2016-06-02 08:48:18","except_duration":"5","actual_duration":"5.2988","percent":"100","batch_id":"20160601","status":"COMPLETED"},
{"job_name":"B","start_time":"2016-06-02 10:00:26","end_time":"","except_duration":"15.5","actual_duration":"6.8319","percent":"44.07","batch_id":"20160602","status":"RUNNING"},
{"job_name":"C","start_time":"2016-06-02 01:02:49","end_time":"2016-06-02 01:57:32","except_duration":".88","actual_duration":".9119","percent":"100","batch_id":"20160601","status":"COMPLETED"},
]
PL/SQL procedure successfully completed.
```
On website, it will use the JOSN data to generate htmls to show the status of current jobs, and also a line chart for fifteen days situations.
