# %%
import pandas as pd
from pathlib import Path


def print_cv_items(df: pd.DataFrame):
    for i in range(len(df)):
        start_date_str = df.iloc[i]["Start Date"].strftime("%b %Y")
        end_date_str = df.iloc[i]["End Date"].strftime("%b %Y")

        if not pd.isnull(df.iloc[i]["Description"]):
            desc_str = f"{df.iloc[i]['Description']}"
        else:
            desc_str = ""

        desc_str = f"{df.iloc[i]['Item']}, *{desc_str}*"

        if start_date_str == end_date_str:
            date_str = f"_{start_date_str}_"
        else:
            date_str = f"_{start_date_str} - {end_date_str}_"

        if not pd.isnull(df.iloc[i]["Information"]):
            info_str = f"#grid(columns: (3%, 97%), align(left)[], align(left)[{df.iloc[i]['Information']}])"
        else:
            info_str = ""

        print(
            f"#grid(columns: (75%, 25%), align(left)[{desc_str}], align(right)[{date_str}]) {info_str}"
        )


# %%
pubs_df = pd.read_csv("/home/emiz/projects/e-miz.github.io/cv/pubs.csv")

# need to fill NaN so indexing works
mypubs = pubs_df[pubs_df["Manual Tags"].str.match("mypublication").fillna(False)]
