#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from pyzabbix import ZabbixAPI
from daemon import Daemon
import telepot,logging,sys

sched = BlockingScheduler()

class daemon_server(Daemon):
    def run(self):
        main()

def get_conf():
    from ConfigParser import ConfigParser
    config = ConfigParser()
    config.read('etc/TeleZabbix.conf')
    api = config.get('Telegram','api')
    group_id = config.get('Telegram','group_id')
    username = config.get('Zabbix','username')
    password = config.get('Zabbix','password')
    server = config.get('Zabbix','server')
    return api,group_id,username,password,server

@sched.scheduled_job('interval', minutes=2)
def check_hosts():
    for h in zapi.host.get(output="extend"):
        if int(h['available']) != 1:
            status = 'Offline'
            bot.sendMessage(group_id, 'ID: '+h['hostid']+'\nStatus: '+status+'\nHost: '+h['host']+'\nNome: '+h['name'])

@sched.scheduled_job('interval', minutes=2)
def chek_web():
    for w in zapi.httptest.get(output='extend',monitored=True,selectSteps="extend"):
        for s in w['steps']:
            if int(s['status_codes']) != 200:
                bot.sendMessage(group_id, 'Nome: '+w['name']+'\nURL: '+s['url']+'\nStatus: '+s['status_codes'])

def main():
    sched.start()

daemon = daemon_server('/var/run/TeleZabbix.pid')

if len(sys.argv) >= 2:

    if sys.argv[1] == 'start':
        api,group_id,username,password,server = get_conf()
        zapi = ZabbixAPI(server)
        zapi.login(username, password)
        bot = telepot.Bot(api)
        daemon.start()

    elif sys.argv[1] == 'stop':
        daemon.stop()

    elif sys.argv[1] == 'restart':
        daemon.stop()
        daemon.start()

    elif sys.argv[1] == 'status':
        daemon.is_running()

else:
    print 'Usage:',sys.argv[0],'star | stop | restart | status'
