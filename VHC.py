#!/usr/bin/env python
import os

# Clear the console.
os.system("clear")

def msg(stat):
    print '\033[1;42m'+'\033[1;37m'+stat+'\033[1;m'+'\033[1;m'

def newline():
    print ""

def new_hosts(domain):
    msg(" What would be the public directory name? \n - Press enter to keep default name (\"public_html\") ")
    public_dir = raw_input()

    # Check and set name of the public directory.
    if public_dir == "":
        public_dir = "public_html"

    newline()

    # Define the webserver parent directory
    msg(" What would be the server parent directory? \n - Press enter to keep \"/var/www/\" as default location. ")
    server_parent_dir = raw_input()
    if server_parent_dir == "":
        server_parent_dir = "/var/www/"
    else:
        if os.path.exists(server_parent_dir) == False:
            msg(" Parent directory (\""+server_parent_dir+"\") was not found! \n Please enter server parent directory again: ")
            server_parent_dir = raw_input()
        else:
            msg(" Server parent directory has changed to:(\""+server_parent_dir+"\") ")

    newline()

    msg(" Creating the Directory Structure ")
    os.system("sudo mkdir -p "+server_parent_dir+domain+"/"+public_dir)

    newline()

    msg(" Change directory permissions? \n It will give current user permission for this vhost and permit read access. \n If you want to change permission then type Y and press enter \n If you are not sure then press enter and skip this step")
    uper = raw_input()
    if (uper == "Y" or uper == "y"):
        msg(" Granting Proper Permissions ")
        os.system("sudo chown -R $USER:$USER "+server_parent_dir+domain+"/"+public_dir)
        print("Proper Permissions Granted")
        newline()

        msg(" Making Sure Read Access is Permitted ")
        os.system("sudo chmod -R 755 "+server_parent_dir+domain+"/"+public_dir)
        print("Read Access is Permitted")
    else:
        msg( "Permission process skipped" )

    newline()

    msg(" Adding A Demo Page ")
    file_object = open(server_parent_dir+domain+"/"+public_dir+"/index.html", "w")
    file_object.write("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Virtual Hosts Created Successfully!</title><style>html{background-color: #508bc9; color: #fff;font-family: sans-serif, arial;}.container{width: 80%;margin: auto  auto;}.inl{text-align: center;}.inl img{border-radius: 10px;}a{color: #f2d8ab;  }</style></head><body><div class='container'><h1>Virtual Hosts Created Successfully!</h1><p><b>Apache-VHC</b> has successfully created a virtual host on your server.</body></html>")
    file_object.close()
    print("Demo Page Added")

    newline()

    msg(" Creating Virtual Host File ")
    host_file = open("/tmp/"+domain+".conf", "w")
    host_file.write("<VirtualHost *:80>\nServerAdmin localserver@localhost\nServerName "+domain+"\nServerAlias www."+domain+"\nDocumentRoot "+server_parent_dir+domain+"/"+public_dir+"\nErrorLog ${APACHE_LOG_DIR}/error.log\nCustomLog ${APACHE_LOG_DIR}/access.log combined\n</VirtualHost>")
    host_file.close()
    os.system("sudo mv \"/tmp/"+domain+".conf\" \"/etc/apache2/sites-available/\"")
    print("Virtual Host File added")

    newline()

    msg(" Activating New Virtual Host ")
    os.system("sudo a2dissite 000-default.conf")
    os.system("sudo a2ensite "+domain+".conf")

    newline()

    msg(" Restarting Apache Server ")
    os.system("sudo service apache2 restart")
    os.system("service apache2 reload")
    print("Apache Server Restarted")

    newline()

    msg(" Setting Up Local Host File ")
    if host_flag == 0:
        os.system("sudo sed -i -e '1i127.0.1.1   "+domain+"\' \"/etc/hosts\"")
    else:
        print " There already is a Local Host File. "

    print "\nSuccess! Please visit http://"+domain+"/ from any web browser\n\n"

host_flag = 0

newline()

print "\n Welcome to Apache-VHC\n - This script will setup and configure Apache Virtual Hosts for you.\n - All you have to do is answer these questions.\n - IMPORTANT: Make sure you have Apache configured.\n"

newline()

msg(" What would be the domain name? ")
domain = raw_input()

if os.path.exists("/var/www/"+domain):
    msg(" IMPORTANT: It seems that you have already configured a virtual hosts with the same domain name \n If you continue then all your data of "+domain+" will be overwritten and this cannot be undone \n Do you want to continue? (yes/no) ")
    flag = raw_input()
    host_flag = 1

    if (flag == "no" or flag == ""):
        newline()
        msg(" New Virtual Host was not created due to a conflict. \n Please choose a different name and try again. ")
        newline()
    if flag == "yes":
        newline()
        msg(" Existing host "+domain+" will be overwritten ... ")
        new_hosts(domain)
else:
    new_hosts(domain)
