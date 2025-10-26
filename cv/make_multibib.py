# %%
import ibis
from ibis import _
import json
from typing import Any

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
        .rename(id="citationKey")
    )
    return key_tags


# This only exists because citeproc/CSL can't parse a dict if a value is null
# So we have to remove it ourselves.
def remove_null_fields(data: dict[Any, Any]) -> None | dict[Any, Any] | list[Any] | Any:
    """
    Recursively remove any keys in a dict which have a value of none.

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    if isinstance(data, dict):
        cleaned_dict = {}
        # Loop over dict and build a new one without None
        for key, value in data.items():
            cleaned_value = remove_null_fields(value)
            if cleaned_value is not None:
                cleaned_dict[key] = cleaned_value
        return (
            cleaned_dict if cleaned_dict else None
        )
    elif isinstance(data, list):
        # Loop over a list and build a new one without None
        cleaned_list = []
        for item in data:
            cleaned_item = remove_null_fields(item)
            if cleaned_item is not None:
                cleaned_list.append(cleaned_item)
        return (
            cleaned_list if cleaned_list else None
        )
    else:
        # This is basically the kernel of the filter,
        # I.e. it's run at the lowest levels of the dict.
        return data if data is not None else None


# %%
key_tags = get_keys_and_tags(zotero_data)
sel_works = (
    key_tags.filter(_.tags["tag"] == "selectedworks")
    .drop("tags")
    .join(csl_pubs, ["id"])
    .execute()
    .to_dict(orient="records")
)

# %%
with open("sel_works.json", "w") as f:
    json.dump(remove_null_fields(sel_works), f)
