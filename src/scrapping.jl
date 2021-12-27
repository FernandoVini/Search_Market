using Pkg

# Pkg.add("SQLite")
# Pkg.add("DataFrames")
# Pkg.add("InlineStrings")
# Pkg.add("IterableTables")
# Pkg.add(url="https://github.com/lungben/TableIO.jl")
# Pkg.add("JDF")

# Uncomment to install packages

using SQLite
using DataFrames
using IterableTables
using TableIO


function getting_sites()
    db = SQLite.DB("supermarkets.db")  # Reading database

    println(SQLite.tables(db))
    
    df_sites = DataFrame(read_table(db, "supermarket"); copycols=false) # Converting SQLite database to DataFrame object

    println(df_sites)

    return df_sites


end


getting_sites()


