# WELCOME
This is a Django API connected to a MySQL database to store and retrieve Gw2 percentile data.

If you haven't already...
## 1. Install Python 
Skip this step if already installed. 
Download and install [Python](https://www.python.org/downloads/) for your OS.

## 2. Clone Repo.
```commandline
cd /your_project_folder/
git clone https://github.com/Mapleia/LogCompareAPI.git
```

## 3. Install MySQL.
Skip this step if already installed.
Download and install [MySQL](https://dev.mysql.com/downloads/installer/) for your OS.

If you know how, open MySQL command line. Otherwise, from your MySQL dev default install,
open **MySQL Client Command Line**. Open, then login.
From MySQL command line, create the database if you haven't already.
```sql
CREATE DATABASE logcomparedb;
```
To confirm:
```sql
SHOW DATABASES;
```
You should see "logcomparedb".

## Base Setup
1. Setup virtual environment (this is an example for VS Code).
    
    a. If not already in the LogCompareAPI folder,
    ```shell script
    cd /LogCompareAPI/
    ```
    *else, skip to b*.
    
    b. Install [virtualenv](https://pypi.org/project/virtualenv/). 
    *If already installed, skip to c.*
    ```shell script
    pip install virtualenv
    ```
    
    c. Create virtual environment with virtualenv. 
    ```shell script
    virtualenv venv_old
    ```
    d. Activate virtual environment. (shell script)
    ```shell script
    venv_old/Scripts/activate
    ```
   
2. Install requirements.
    
    Once your virtual environment is running, the terminal should show:
    ```shell script
    (venv_old) C:\path_to_project_folder\LogCompareAPI>
    ```
   
   In here, pip install the requirements.
   ```shell script
   pip install -r requirements.txt
    ```
   
3. Setup your .env file to store your secrets.
    Create a file in the home directory of the project (C:\path_to_project_folder\LogCompareAPI) 
    called **.env**.
    
    ```.env
    DB_PASS='INSERT YOUR DATABASE PASSWORD HERE'
    SECRET_KEY='INSERT SECRET DJANGO KEY HERE'
   ```
    
## Setup Django.
While you're still in your virtual environment:
```shell script
py manage.py makemigrations
py manage.py migrate
```

### Super User
If you'd like to create an admin account run the commands below to be taken
through the process of setting up an admin account.
```shell script
py manage.py createsuperuser
```
## Run Django Server
```shell script
py manage.py runserver
```