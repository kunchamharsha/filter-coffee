# filter-coffee
Filter coffee is a business rule engine with UI to help businesses write complex business rules without developers interfering. 


Pre-requisites
- mysql 
- django 


Installation process for developers

> Install venv 

> virtualenv -p python3

> pip3 install -r requirements.txt 

> create a new file dev.env 

> fill in sample.env values in dev.env

> python3 manage.py migrate // To install mysql tables 

To Run the server 

> python3 manage.py run 

Installation errors you might face 

- NameError: name '_mysql' is not defined after setting change to mysql

> export DYLD_LIBRARY_PATH="/usr/local/mysql/lib:$PATH"



POSTMAN collection 
- https://www.getpostman.com/collections/d7158f2ffcadad070596
