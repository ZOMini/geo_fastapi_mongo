import runpy

# import sys

runpy.run_path('geo_api/data/data_txt_to_sql.py', run_name='__main__')
runpy.run_path('geo_api/data/index_db.py', run_name='__main__')

# sys.argv = ['', 'runserver']
# runpy.run_path('./manage.py', run_name='__main__')
