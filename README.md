## sql_crud_python3
CRUD example in SQLite and Python 3

## Dev Mode 
Set `dev_mode = True` to run the following
### Creates the table structure, if it doesn't exist
create_table()

### Creates a db entry
create_record(fake_opened, fake_last_updated, fake_jsm_ticket, fake_zabbix_id)

### Pulls data from the db
print(read_record(1))

### Updates a current records information
update_record(1, fake_zabbix_id)

### Deletes a particule entry in the sqlite db
delete_record(1)


## Prod Usage
Set `deb_mode = False` too allow normal run

`python .\crud_sqlite.py "zabbix-898"`

> Prod mode run for: zabbix-898
