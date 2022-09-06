import runpy

# import sys

# sys.argv = ['', 'migrate']
# runpy.run_path('./manage.py', run_name='__main__')

# runpy.run_path('./data/create_superuser.py', run_name='__main__')

runpy.run_path('data/data_txt_to_sql.py', run_name='__main__')

# sys.argv = ['', 'runserver']
# runpy.run_path('./manage.py', run_name='__main__')
