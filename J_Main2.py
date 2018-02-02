tables = {}
tables["pstar"] = """
    CREATE TABLE pstar (
        name varchar(255),
        birthdate date                
    )
    """
tables["pstar2"] = """
    CREATE TABLE pstar (
        name varchar(255),
        birthdate date                
    )
    """

for name, sql in tables.items():
    print(name)
    print(sql)