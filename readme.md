# FXTest测试平台
### flask + Python3  实现的API自动化测试平台。
###  下面有介绍python flask部署相关的文章链接。为自己部署的记录文章
### 前后端开始进行分离，通过接口进行交互



### flask +gevent+nginx+Gunicorn+supervisor部署flask应用请用flaskapi_su.conf，用gunicorn部署应用，因为在使用uwsgi部署会影响定时任务的执行
### supervisor配置可见super.conf文件。
### 钉钉群发送多用例测试任务的执行情况的时候，需要在config.py里面进行配置钉钉群自定义机器人webhook，目前体验服没有钉钉配置
### 定时任务模块定时任务测试完毕会按照config.py设置的钉钉群自定义机器人的配置进行发送通知的，当定时任务完成后，配置钉钉群会默认接受到一条钉钉机器人消息，显示定时任务的完成情况。
### 定时任务现在依赖与redis做持久化，如果有报redis错误，请安装redis服务。

