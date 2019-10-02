#!usr/bin/env python

import sqlite3
import time

conn = sqlite3.connect('db1.db')
c = conn.cursor()



def create_table():
    """Method to create table.
    """
    c.execute('CREATE TABLE IF NOT EXISTS fer_poc(groupID TEXT, name TEXT, faceID Text, datestamp TEXT)')



def data_entry(personGroupId, img_url, face_id, time):
    """Method to add data into the fer_poc database
    
    Arguments:
        personGroupId {String} -- This defines the client company{required for later use as we have to train using this}
        img_url {String} -- name of the file which is being uploaded{has to be changed by the client name when fully functional}
        face_id {String} -- faceId generated by the Cognative API
        time {String} -- Time stamp to save the time when ID was generated.
    """
    conn = sqlite3.connect('db1.db')
    c = conn.cursor()
    c.execute('INSERT INTO fer_poc (groupID, name, faceID, datestamp) VALUES (?, ?, ?, ?)',
              (personGroupId, img_url, face_id, time))
    conn.commit()
    c.close()
    conn.close()


def read_data(query, table_name):
    """Method to read data from the database.
    
    Arguments:
        query {String} -- The fields which has to be fetched.
        table_name {String} -- The table from which data has to be read.
    """

    row_data = []
    conn = sqlite3.connect('db1.db')
    c = conn.cursor()
    c.execute('SELECT {} FROM {}'.format(query, table_name))
    for row in c.fetchall():
        row_data.append(row)
    c.close()
    conn.close()
    return row_data


print(read_data('faceId, groupId', 'fer_poc'))
# create_table()
