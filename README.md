# Quarto Website

## Citations

- Citations are managed in a Zotero library and exported using the Better Biblatex format
- Citations formatting is largely controlled using a custom CSL file. You can control things like:
    - The sort order
    - Displaying the year next to citations instead of the citation number

Formatting is tricky to manage because each field in a citation (e.g. the title) has a different label depending on the context. Within Zotero a citation type may be a `Conference Paper`, but this is exported as `inproceedings`, which is treated as an `article` in hayagriva, but is treated as `paper-conference` in CSL.

``` mermaid
flowchart LR
    Zotero-->Biblatex-->Hayagriva
    Biblatex-->CSL
    Hayagriva-->CSL
    CSL-->Hayagriva
```

Zotero to Biblatex:

- Manually examine the output

Zotero to CSL:

- [See this table](https://hughandbecky.us/Hugh-CV/books/zotero-examples/zotero-to-csl-variables/)
- [Force a type using the "Extra" field and input `Type: CSL-Type`](https://hughandbecky.us/Hugh-CV/books/zotero-examples/zotero-extra-field/#adding-csl-types-and-variables)

Biblatex to Hayagriva:

- [Use this converter](https://jonasloos.github.io/bibtex-to-hayagriva-webapp/)

Hayagriva and CSL:

- Examine the source code ([variables](https://github.com/typst/hayagriva/blob/799cfdcc5811894f62949a63b155878e2f30b879/src/csl/taxonomy.rs#L302), [source types](https://github.com/typst/hayagriva/blob/799cfdcc5811894f62949a63b155878e2f30b879/src/interop.rs#L177))

Hayagriva is especially "lossy" since it has a restrictive schema with a [limited number of fields](https://github.com/typst/hayagriva/blob/main/docs/file-format.md#reference). This is because it attempts to convert a "book chapter" into a nested pair of a "chapter" inside of a "book".

### Adding Citations

The CSL file has been customized for the following types:

| Zotero           | Biblatex        | CSL                | Hayagriva |
|------------------|-----------------|--------------------|-----------|
| Conference Paper | `inproceedings` | `paper-conference` | `article` |
| Preprint         | `online`        | `webpage?`         | `web`     |
| Journal Article  | `article`       | `article?`         | `article` |
| Software         | `software`      | `software?`        | `misc`    |

#### Presentations, talks, etc

- The Zotero type should be **Conference Paper**

#### Preprints and Journal Articles

- Both of these Zotero types work fine, i.e. from arxiv or published journals

#### Software

- This is a pretty barebones type. You can try to make use of the Extra field here and display the `annote` in the CSL file.
