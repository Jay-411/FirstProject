import DB


dbc = DB.Database()
dbc.connect()
dbc.test()
dbc.close()

#alternative
with DB.Database() as dbc:
    dbc.connect()
    dbc.test()
