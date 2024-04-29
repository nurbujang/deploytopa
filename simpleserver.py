# python -m venv venv
# VM On Linux: source ./venv/bin/activate
# run python simpleserver.py > it will say No module named 'flask'
# so pip install flask, then rerun python simpleserver.py
# http://127.0.0.1:5000 > hello from simple server
# Crtl + C
# pip freeze > requirement.txt > ls > (requirements.txt will be there)
# git commit to github, check to make sure configuration files dont come up there

# login to pythonanywhere > focus on CONSOLE and WEB APPS
# copy https link of deploypa from github
# > in bash console, git clone https://github.com/nurbujang/deploytopa.git 
# > ls > deploytopa should be there
# > cd deploytopa > ls (will have all 4 files there)
# still in bash: 09:52 ~/deploytopa (main)$ pip install -r requirements.txt

# NOW WE NEED TO DEPLOY THIS WEB APPLICATION - WE BASICALLY MAKE A NEW WEB APP
# snake > All Web Apps > add a new web app 
# (if theres alread one, delete it first - delete nurbujang.pythonanywhere.com)
# > next > flask > python 3.10 (ours is 3.11)
# change path to /home/nurbujang/deploytopa/simpleserver.py
# > Configuration for nurbujang.pythonanywhere.com 

####### something wrong bc it got overwritten!!!
# snake > bash > cat simpleserver.py > says hello from flask, instead of hello from simple server

# IN BASH:  10:06 ~/deploytopa (main)$ git pull (Already up to date.)
# edit simpleserver in VScode and push
# git pull in bash > error: Your local changes to the following files would be overwritten by merge:
        # simpleserver.py Please commit your changes or stash them before you merge. Aborting
# use force git pull. How? in bash: git fetch > cat simpleserver.py > but still says Hello from flask
# FAILED, SO USE git reset --hard origin/master. how?
# in bash: 10:16 ~/deploytopa (main)$ git reset --hard origin/main
#                   HEAD is now at 4b48b30 simple server 22
# git pull > already up to date > cat simpleserver.py > says hello from simple server 22
# YAYYYY

# SNAKE, All web apps, reload nurbujang.pythonanywhere.com > will say hello from simple server 22

# go back to pa dashboard, > databases(top right)
# > mysql password rootroot
# MySQL settings
# Connecting:
# Use these settings in your web applications.
# Database host address: nurbujang.mysql.pythonanywhere-services.com
# Username: nurbujang
# create a database > name it project > password rootroot
# click nurbujang$project console (max 2, so kill unused ones)
# mysql> show databases;
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | nurbujang$default  |
# | nurbujang$project  |
# | nurbujang$wsaa     |
# | performance_schema |
# mysql> create database project;
# ERROR 1044 (42000): Access denied for user 'nurbujang'@'%' to database 'project' > WHYYY?
# mysql> show tables;
# Empty set (0.01 sec)

# copy from dr10 - bookDAO.py, bookviewer.html, dbconfig_template.py, server1.py
# put into deploytopa
# mysql> create table book(
#     -> id int not null auto_increment primary key,
#     -> author varchar(250),
#     -> title varchar(250),
#     -> price int);
# mysql> insert into book (title, author, price) values ('test', 'me', 123);
# Query OK, 1 row affected (0.00 sec)
# mysql> select * from book;
# +----+--------+-------+-------+
# | id | author | title | price |
# +----+--------+-------+-------+
# |  1 | me     | test  |   123 |
# +----+--------+-------+-------+
# 1 row in set (0.00 sec)

# edit dbconfig_template.py and save as dbconfig.py
# mysql = {
#     'host':"localhost",
#     'user':"root",
#     'password':"",
#     'database':"project"
# }

# try and upload this without the MySQL package
# if that doesn't work, if I get an error saying that it doesn't work, 
# then I will do it with the package
# on VS venv, push to github (make sure to git pull first if we made changes elsewhere) - if cannot push, git config pull.rebase false > git pull > git push
# check if all are pushed on github - yes

# go to bash console, 11:48 ~/deploytopa (main)$ git pull 
# should have gitignore, license, readme, bookDAO, bookviewer, dbconfig, dbconfig_template, requirements, server1, simpleserver

# in .gitignore: (to not push db.config on github)
# # Pyre type checker
# .pyre/
# dbconfig
# push on github from venv VS
# git pull on bash

# Next:
# 1. update dbconfig on bash
# in bash: 13:16 ~/deploytopa (main)$ vi dbconfig.py, 
# change these: 'host':"localhost", 'user':"root", 'password':"rootroot", 'database':"project" } to:
        # get info to replace: go back to dash > Databases > 
        # MySQL settings
        # Connecting:
        # Use these settings in your web applications.
        # Database host address:
        # nurbujang.mysql.pythonanywhere-services.com
        # Username:
        # nurbujang
# in vi, use arrow to go to where to edit, type i, 
# then can paste nurbujang.mysql.pythonanywhere-services.com as host
# username nurbujang
# password rootroot
#  database nurbujang$project
# press escape (insert will disappear from bottom left)
# press :wq (writing quit), enter (will go back to bash). to quit without changing :q! enter

# from dash, click Web (top right), reload nurbujang.pythonanywhere.com 
# click Configuration for nurbujang.pythonanywhere.com > still hello simple server 22

# So, need to change to server I'm running to
# ls on bash -  we want to use server1.py
# so how to change? 
    #   click web, click WSGI configuration file: /var/www/nurbujang_pythonanywhere_com_wsgi.py (this is the configuration file)
    # change: # import flask app but need to call it "application" for WSGI to work #from simpleserver import app as application  # noqa
    # to : from server1 import app as application  # noqa
# web > reload nurbujang.pythonanywhere.com >  Configuration for nurbujang.pythonanywhere.com 
# will get: Not Found The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
# change url to: http://nurbujang.pythonanywhere.com/books (i got test, 1, 123, me)
######################## andrew got internal Server Error > go back to Web > Log files > Error log nurbujang.pythonanywhere.com.error.log (access denied for andrew bc of wrong password)
# change url to http://nurbujang.pythonanywhere.com/bookviewer.html > will see table but no (i got test, 1, 123, me)
# so check bookviewer.html, change url in all Ajax
# function getAllAjax(){
#         # $.ajax({
#         #     "url": "http://127.0.0.1:5000/books", <<<<<< change to /books
# function createBookAjax(book){
#         //var car = {"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}
#         console.log(JSON.stringify(book));
#         $.ajax({
#             "url": "http://127.0.0.1:5000/books", <<<<<< change to /books
# function updateBookAjax(book){
#         //var car = {"reg":"12 D 1234","price":8000}
#         console.log(JSON.stringify(book));
#         $.ajax({
#             "url": "http://127.0.0.1:5000/books/"+encodeURI(book.id), <<<<<< change to /books
# function deleteBookAjax(id){
#         //console.log(JSON.stringify('deleting '+id));
#         $.ajax({
#             "url": "http://127.0.0.1:5000/books/"+encodeURI(id), <<<<<< change to /books
# push to github from  venv
# git pull on bash
# > reload nurbujang.pythonanywhere.com >  Configuration for nurbujang.pythonanywhere.com
# go to http://nurbujang.pythonanywhere.com/bookviewer.html, 
# # will get Books
# id 	Title 	Author 	Price 	Update 	Delete
# 1	me	test	123	

# lets create, ud, can click to delete, update etc
# andrew got error, BookDAO object has no attribute db
# def delete(self, id):
#         cursor = self.getcursor()
#         sql="delete from book where id = %s"
#         values = (id,)

#         cursor.execute(sql, values)

#         self.connection.commit() <<<< andrew had it as self.db.commit()
# push from venv, pull in bash. 
# > reload nurbujang.pythonanywhere.com >  Configuration for nurbujang.pythonanywhere.com




from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/', methods=['Get'])

def getAllBands():
    return "hello from simple server 22"

if __name__ == "__main__":
    app.run(debug=True)

# save to folder deploy2pa