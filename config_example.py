
mail_server = 'smtp.your_company.com'
mail_server_port = '25'
mail_server_ssl_enabled = True 

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
        },
        'emails': [
            'dba@your_company.com',
            'developer@your_company.com',
            'cto@your_company.com',
            'techlead@your_company.com',
            ]
    },
]
