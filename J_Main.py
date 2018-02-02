import J_Mysql as db


with db.Database() as dbc:
    dbc.createTables()
    dbc.dropTables()
