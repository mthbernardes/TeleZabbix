# TeleZabbix
Stop spending money with SMS, receive in your Telegram chat/group notifications of hosts/webs down.

#Install dependencies
pip install -r dependencies.txt

#Configure your TeleZabbix
Edit the file etc/Telezabbix.conf

api = Your Telegram API KEY

group_id = The chat/group ID, that you want to send the notifications

username = Your zabbix username

password = Your zabbix passowrd

server = The zabbix server (Ex.: http://127.0.0.1/zabbix)

#Start TeleZabbix

python TeleZabbix.py start

#Stop TeleZabbix

python TeleZabbix.py stop

#Status TeleZabbix

python TeleZabbix.py status

