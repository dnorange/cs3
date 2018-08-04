# Django后台模板 #
模板中包含打包配置setup.py，Python2开发虚拟环境依赖requirements.txt，开发环境配置cs3.settings.dev，生产环境配置cs3.settings.prod，生产环境发布fab脚本，生产环境apache2的conf配置

## 技术栈 ##
django+xadmin+fabric+setuptools+mysql+apache2+linux

## 开发环境配置流程 ##
* 本地开发环境安装python虚拟环境
* pip install -r requirements.txt 安装依赖的python库
* python manage.py makemigrations 生成数据库脚本
* python manage.py migrate 自动创建数据表
* python manage.py createsuperuser 创建django后台管理超级管理员
* python manage.py runserver 启动
* http://locahost:8000/xadmin 进入后台

## 生产环境发布流程 ##
### 初次发布 ###
* 生产环境服务安装python虚拟环境、安装apache2、安装mysql（如有需要）。
* 修改源码中fabfile.py中服务器登录用户、地址，修改deploy()方法中python虚拟环境路径。
* 将源码中conf文件夹下的manage.py、wsgi.py拷贝至服务器单独保存，如/var/www/cs3/下。
* 修改源码中conf文件夹下的cs3.conf，将其中的pythonPath改为服务器上python虚拟环境的路径，将wsgi文件的路过改为上一步所上传的路径，将cs3.conf文件拷贝至服务器，作为apache2的配置文件。
* 本地打包，fab pack
* 上次发布，自动安装，fab deploy
* 生产环境mysql创建数据库，如cs3
* python manage.py makemigrations 生成数据库脚本
* python manage.py migrate 自动创建数据表
* python manage.py createsuperuser 创建django后台管理超级管理员
* http://服务器地址/xadmin 进入后台
* 如服务不正常尝试用 sudo service apache2 restart 重启服务
* 应用错误日志保持在/var/log/apache2/error-cs3.log中

### 更新发布 ###
* 修改源码中setup.py中模块的版本号，如0.0.1 -> 0.0.2
* 本地打包，fab pack
* 上次发布，自动安装，fab deploy

