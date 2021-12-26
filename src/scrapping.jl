using Pkg

Pkg.add("SQLite")

using SQLite

db = SQLite.DB("supermarkets.db")

print(SQLite.tables(db))