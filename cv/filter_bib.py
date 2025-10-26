# %%
import ibis
from ibis import _

con = ibis.duckdb.connect()
# %%
csl_pubs = con.read_json("pubs.json")
zotero_data = con.read_json("zotero_bbt_export.json")


# %%
def get_keys_and_tags(zotero_data):
    """
    Zotero data contains "items" which is an array of structs where each struct is a bib item
    We unnest the array into a column, then from there we split each field
    in the struct into it's own column with lift. The resulting tags field is also an array of structs.
    With one struct per tag on an item.
    """
    key_tags = (
        zotero_data.select(_.items.unnest())
        .items.lift()
        .select(
            # THEN, keeping the citation key we can unnest the array of tags (array of structs)
            # To get the citationkeys with a specific tag
            _.citationKey,
            _.tags.unnest(),
        )
        .select("citationKey")
        .rename(id="citationKey")
    )
    return key_tags


# %%
key_tags = get_keys_and_tags(zotero_data)
key_tags.filter(_.tags["tag"] == "selectedworks").join(csl_pubs, ["id"]).to_json(
    "sel_works.json"
)
