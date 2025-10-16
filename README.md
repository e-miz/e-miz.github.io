# Quarto Website

## Citations

- Citations are managed in a Zotero library and exported using the CSL JSON format[^1]
- Citations formatting is largely controlled using a custom CSL file. You can control things like:
    - The sort order
    - Displaying the year next to citations instead of the citation number

[^1]: Pandoc can [directly accept CSL files](https://pandoc.org/demo/example33/9.1-specifying-bibliographic-data.html), which [save a conversion step](https://retorque.re/zotero-better-bibtex/exporting/pandoc/index.html#use-csl-not-bibtex-with-pandoc) make using a CSL file much clearer.

### Adding Citations

The CSL file has been customized for the following types:

| Zotero           | CSL                |
|------------------|--------------------|
| Conference Paper | `paper-conference` |
| Preprint         | `article`          |
| Journal Article  | `article-journal`  |
| Software         | `software`         |

#### Presentations, talks, etc

- The Zotero type should be **Conference Paper**

#### Preprints and Journal Articles

- Both of these Zotero types work fine, i.e. from arxiv or published journals

#### Software

- This is a pretty barebones type. You can try to make use of the Extra field here and display the `note` in the CSL file.
