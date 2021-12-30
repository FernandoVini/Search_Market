using Pkg

# Pkg.add("SQLite")
# Pkg.add("DataFrames")
# Pkg.add("InlineStrings")
# Pkg.add("IterableTables")
# Pkg.add(url="https://github.com/lungben/TableIO.jl")
# Pkg.add("JDF")
# Pkg.add("HTTP")
# Pkg.add("Gumbo")

# Uncomment to install packages

using SQLite
using DataFrames
using IterableTables
using TableIO
using HTTP 
using Gumbo


function getting_sites()
    db = SQLite.DB("supermarkets.db")  # Reading database

    println(SQLite.tables(db))
    
    df_sites = DataFrame(read_table(db, "supermarket"); copycols=false) # Converting SQLite database to DataFrame object

    println(df_sites)

    return df_sites


end

function scrapping_pages(df::DataFrame)
    sites = df[!, "site"]
    
    for idx in sites
        try
            req = HTTP.get("https://"*idx)
            println("Request: ")
            parsed = parsehtml(String(req.body))
            println(parsed)

        catch err
            println(err)
            continue
        end

    end


end


df = getting_sites()

scrapping_pages(df)
