import sqlite3
import datetime
from random import randrange # only used for testing


# Random Vars
table_name = 'tracking.db'
c_time = (datetime.datetime.now())


# testing data for script
fake_opened = c_time
fake_last_updated = c_time
fake_jsm_ticket = f'MOSAICX-{randrange(200, 5000)}'
fake_zabbix_id = f'ZABBIX-{randrange(200, 5000)}'
# end of testing data


# Attempt to connect to the database and create a new table if it doesn't exist
def create_table():
    
    conn = sqlite3.connect(table_name)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tracking_info (id INTEGER PRIMARY KEY, opened TEXT, last_updated TEXT, jsm_tcket TEXT, zabbix_id TEXT)')
    conn.commit()
    cur.close()


#add current dt to output
def create_record(opened, last_updated, jsm_ticket, zabbix_id):
    # Connect to the database and insert a record
    conn = sqlite3.connect(table_name)
    cur = conn.cursor()
    cur.execute("INSERT INTO tracking_info (opened, last_updated, jsm_ticket, zabbix_id) VALUES (?, ?)", (opened, last_updated, jsm_ticket, zabbix_id))
    conn.commit()
    cur.close()


def read_record(zabbix_id):
    # Connect to the database and retrieve a record
    conn = sqlite3.connect(table_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tracking_info WHERE zabbix_id=?", (zabbix_id,))
    row = cur.fetchone()
    if row is not None:
        return row[1], row[2]
    else:
        return None


def update_record(id, last_updated):
    # Connect to the database and update a record's information
    conn = sqlite3.connect(table_name)
    cur = conn.cursor()
    cur.execute("UPDATE tracking_info SET last_updated=? WHERE id=?", (last_updated, id))
    conn.commit()
    cur.close()

# Connect to the database and delete a record
def delete_record(id):
    
    conn = sqlite3.connect(table_name)
    cur = conn.cursor()
    cur.execute("DELETE FROM tracking_info WHERE id=?", (id,))
    conn.commit()
    cur.close()

# check db for a current zabbix issue with a jsm ticket
def check_for_ticket(zabbix_id):
    
    ticket_exist = read_record(zabbix_id)    
    
    if ticket_exist > 0:
        # if it does exist, run the update_record function
        update_record()
    else:
        # if it doens't exist, run the create_record function
        create_record()

        

# Creates the table structure, if it doesn't exist
create_table()

# Creates a db entry
create_record(fake_opened, fake_last_updated, fake_jsm_ticket, fake_zabbix_id)

# Pulls data from the db
print(read_record(1))

# Updates a current records information
update_record(1, fake_opened, fake_last_updated, fake_jsm_ticket, fake_zabbix_id)

# Deletes a particule entry in the sqlite db
#delete_record(1)

print(f'Script finished at {c_time}')