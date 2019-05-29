#!/usr/local/python-3.7.3/bin/python3.7

import psycopg2
conn = psycopg2.connect('user=foo password=bar dbname=baz')
curs =conn.cursor()

reply_to = input('Rely to: ')
subject = input('Subject: ')
sender = input('Sender: ')
text=input('Text: ')

if reply_to:
    query = """
    INSERT INTO messages(reply_to, sender, subject, text)
    VALUES({}, '{}', '{}','{}')""".format(reply_to,sender, subject,text)
else:
    query = """
    INSERT INTO messages(sender, subject,text)
    VALUES('{}','{}', '{}')""".format(sender, subject, text)

curs.execute(query)
conn.commit()	



