# APACHE AIRFLOW BASIC CONCEPT

## What Is Airflow
- Starts in Airbnb 2014
- Manage Complex workflow
- Top-level apache project 2019
- Workflow management platform
- Written in Python

## Workflow 
workflow is defined as series of task, workflow is defined as DAG, namely directed acyclic graph. 


## DAG, TASK, Operator
- DAG's are the primary way to orcestrate data pipelines, they are built from python and use a wide variety of supporting libraries.
Fundamentally, DAG are comprised of task, operators and sensors. There are new techniques that have been introduced over the years, relating to task group and deferrable operators, that will also cover in this chapters.

- Task defines a unit of work within a DAG as shown in the exmple DAG, it is repesented as a node in DAG,and it is written in python
- Depedency between task
- The Goal of the task is to achive a specific thing, the method is uses is called operator
- While DAG describe how to run a workflow Operatore determine what actual get done by a task. In Airflow, there are many kind of operator like Bashoperator, pythonoperator etc


To Sum up, the operator detemines what is going to be done. The Task implements an operator by defining spesific value for that operator and dag is a collection of all the task you want to run.

### DAG 
a DAG is a collection of all the tasks you want to run, organized in a way that reflects their dependencies
- it helps you define the structure of your entire workflow, showing tasks need to happen before others.


### Operator 
an operator defines a single, ideally idempotent, task in your DAG
Operators allow you to break down you workflow into discreate, manageable piece of work

Airflow has thousand of Operators
- The PythonOperator to execute a Python script or function
- The BashOperator to execute a bash script or command
- The SQL ExecuteQueryOperator to execute a SQL Query to a Database
- The Filesensor to wait for a file

#### Type Of Operator :
Action Operator : Execute an Action
Transfer Operator : Transfer Data
Sensor : Wait for a condition to be met


### Task / Task Instance
- A Task is a Specifice instance of an operator. when an operator is assigned to a DAG, it becomes a task

## Workflow 
A workflow is the entire process defined by your DAG, including all task and their depedencies.


## Execute Date, Task Instance and DAG run :
- The execution_date is the logical date and time which the DAG run, its task instances
- Task Instance is a run of a task at a specific point of time
- DAG RUN is instantiation of a DAG, containing task instances that run for a specific execution_date


# Architecture
## Single Node Architecture
- A node is a single computer or server
- A single node architecture means all components of airflow are running on one machine (this is the typical setup you get when install and run airflow)
- 
# TASK LIFECYCLE AND BASIC ARCHITECTURE
- There are in total 11 different kinds of stages. In the Airflow UI
![image](image\2a.png)

- no_status : scheduler created empty task instance

- scheduled : scheduler determined task instances need to run

- queued : scheduler sent task to executor to run on the queue

- running : worker picked up a task and is now running it

- success : Task completed without error

- upstream_failed : the task's upstream task filed

- up_for_reschedule : reschedule task every certain time interval

- skipped : task is skipped

- up_for_retry : rerun the task

- failed : Task is failed

- shutdown : Task run has been shutdown

![task_lifecycle](image/task_lifecycle.png)


# Basic Architecture
![basic-architecture](basic-architecture.png)
- Data Engineer | Bulding and monitoring ETL processing | Airflow.cfg
- 


# Apache Airflow Dataset
- What's a Dataset :
well think of a data set a logical group of data, like file or like a SQL table, any thing
- Data set has two properties and the first one is the URI (like the path to the data), Unique Identifier of your data. Must compose of only ASCII character.
The URI schem cannot be airflow, case sensitive
- Extra : Json dictionary
- Dataset limitations
Datasets are amazing, but they have limitations as well:
    - DAGs can only use Datasets in the same Airflow instance. A DAG cannot wait for a Dataset defined in another Airflow instance.
    - Consumer DAGs are triggered every time a task that updates datasets completes successfully. Airflow doesn't check whether the data has been effectively updated.
    - You can't combine different schedules like datasets with cron expressions.
    - If two tasks update the same dataset, as soon as one is done, that triggers the Consumer DAG immediately without waiting for the second task to complete.
    - Airflow monitors datasets only within the context of DAGs and Tasks. If an external tool updates the actual data represented by a Dataset, Airflow has no way of knowing that.

# The Executor 
First thing first, that you need to know about it is that it doesn't run your tasks, it doesn't execute

it defines how sistem run your task and basicall you have many different executors that you can use.
For example :
- local executor to run multiple task on a single machine.
- Sequential Executor run on task a time on a single mechine
- remote executors like the self executor to execute your tasks on the celery cluster on multiple machines.
- communities executor to run your tasks on a Kubernetes cluster, same thing on multiple machines in multiple pods.

So as you can see, there are many different

## Sequential Executor 
- Run Task Sequentially
- Its Extremely Simple and youu will use taht executable only for making experiment or debugging some issue
- To configure this executor, you just need to modify the executor setting with the sequential executor value.

## local executor
The local executor is one step further than the sequential executor, as it allows you to execute multiple tasks at the same time.

But on a single machine, it means that you end up with the same, for instance, but with a different database.

It is as simple as defining the executable parameter with local executor and defining the SQL alchemy

icon that contains the connection to your database.

And here it is the connection that you will use to connect to Postgres.

## Celery Executor
Just keep in mind that you need to install the salary queue which may be redis or rabbit in queue For example.

Because of this queue you need to define to additional configuration settings the server result back end and the salary broker URL.