
# pg_reporter
PostgreSQL bad queries reporter

Quick start:

	git clone https://github.com/dezconnect/pg_reporter.git
	sudo cp pg_reporter /opt 
	cd /opt/pg_reporter
	sudo cp config_example.py config.py


Configure config.py:

```python
mail_server = 'smtp.your_company.com'
mail_server_port = '25'
sender_mail = 'pg_reporter@you_company.com'

servers = [
    # Config example
    {
        'hostname': 'pg-server.your_company.com',
        'name': 'pg-server',
        'server_description': 'Some PostgreSQL Server',
        'conn_info': {
                'address': '10.10.10.1',
                'port': 5432,
                'db_name': 'postgres',
                'db_user': 'postgres',
                'db_password': 'pg_password',
        }
        'emails': [
            'dba@your_company.com',
            'developer@your_company.com',
            'cto@your_company.com',
            'techlead@your_company.com',
            ]
    },
]
```


Reset statements statistic for actual values on your PostgreSQL server

```sql 
SELECT pg_stat_statements_reset();
```

Add reporter to root crontab:

	0 0 * * * 	/opt/pg_reporter/reporter_py >> /tmp/pg_reporter.log 2>&1  # For daily start at 0:00 AM
