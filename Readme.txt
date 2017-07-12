
#在home文件夹下建立名为www的文件夹,并切换到该文件夹
#切换到该文件夹并gitclone


#我们需要安装PIP与virtualenv
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install virtualenv

#安装uwsgi
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential python python-dev
sudo pip install uwsgi

#安装并运行Nginx：
sudo apt-get install nginx
sudo /etc/init.d/nginx start

#创建并激活一个虚拟环境，在其中安装python包
cd /home/www/blog
virtualenv venv
source venv/bin/activate
pip install -r requirement.txt


#并且删除nginx的原始配置文件 在/etc/nginx/conf.d  或/etc/nginx/sites-enabled
删除其中nginx的配置文件


#配置文件使用符号链接到Nginx配置文件文件夹中，重启Nginx
sudo ln -s /home/www/blog/demoapp_nginx.conf /etc/nginx/conf.d/
sudo /etc/init.d/nginx restart


创建一个新文件夹存放uWSGI日志
sudo mkdir -p /home/log/uwsgi


#执行以下代码 则启动uwsgi .
uwsgi --ini /home/www/blog/demoapp_uwsgi.ini

#执行该代码则是在Linux后台永久启动uwsgi服务，并且永久运行该项目。可通过kill来结束进程来停止服务
nohup uwsgi --ini /home/www/blog/demoapp_uwsgi.ini > /dev/null 2>&1 &