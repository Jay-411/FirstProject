import DB


dbc = DB.Database()
dbc.connect()
dbc.test()
dbc.close()

with DB.Database() as dbc:
    dbc.connect()
    dbc.test()
