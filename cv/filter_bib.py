# %%
import ibis
from ibis import _

con = ibis.duckdb.connect()
# %%
csl_pubs = con.read_json("pubs.json", table_name="csl_pubs")
bbt_pubs = con.read_json("pubs_bbt.json", table_name="bbt_pubs")
# %%
# Items is an array of structs where each struct is a bib item
# We unnest the array into a column, then from there we split each field
# in the struct into it's own column with lift
sel_works = bbt_pubs.select(_.items.unnest()).items.lift().select(
    # THEN, keeping the citation key we can unnest the array of tags (array of structs)
    # To get the citationkeys with a specific tag
    _.citationKey, _.tags.unnest()
).filter(_.tags["tag"] == "selectedworks").rename(id="citationKey").select("id")

# %%
sel_works.join(csl_pubs, ["id"]).execute()

# %%
