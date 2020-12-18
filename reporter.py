#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from datetime import datetime
import psycopg2
from jinja2 import Template

import sys
import logging
import smtplib

from config import *


path = sys.path[0]

logging.basicConfig(filename=path + "/report.log", level=logging.INFO)

def curr_date():
    return datetime.now().strftime("%Y-%m-%d")


def get_query():
    sql = open(path + '/query.tpl').read()
    template = Template(sql)
    return template.render()


def execute_statements(pg_conn, sql):
    cur = pg_conn.cursor()
    try: 
        cur.execute(sql)
        result = cur.fetchall()
    except BaseException:
        result = []
    return result


def get_report(server):
    try:
        pg_conn = psycopg2.connect("host=%s port=%d dbname=%s user=%s password=%s" % (
            server["conn_info"]["address"],
            server["conn_info"]["port"],
            server["conn_info"]["db_name"],
            server["conn_info"]["db_user"],
            server["conn_info"]["db_password"]))
    except psycopg2.OperationalError:
        return []

    result = execute_statements(pg_conn, get_query())
    execute_statements(pg_conn, "SELECT pg_stat_statements_reset();")
    return result


def report(server):
    logging.info("Start report for %s." % server["hostname"])
    result = get_report(server)
    if result: 
        send(server, to_string(result))
    else:
        logging.info("Report for %s failed." % server["hostname"])


def to_string(result):
    return "\n".join(map(lambda x: str(x[0]), result))


def send(server, result):
    conn = smtplib.SMTP(mail_server, mail_server_port)

    if mail_server_ssl_enabled:
        conn.ehlo()
        conn.starttls()

    body = "\r\n".join((
        "From: %s" % sender_mail,
        "To: %s" % ",".join(server["emails"]),
        "Subject: PostgreSQL report from %s" % server["name"], 
        "",
        result
        ))

    conn.sendmail(sender_mail, server["emails"], body)
    conn.quit()


def main():
    logging.info("Start reporting %s" % curr_date())
    for server in servers:
        report(server)


if __name__ == '__main__':
    main()

