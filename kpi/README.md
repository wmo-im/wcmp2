# Key Performance Indicators (KPI)

## Overview

This directory manages the WCMP KPI framework.  This document provides
instructions for adding KPIs and managing the documentation.

### Dependencies

KPI documentation is managed with [Asciidoctor](https://asciidoctor.org).

Link checking is managed with [asciidoc-link-check](https://www.npmjs.com/package/asciidoc-link-check).

### Building

```bash
# create HTML (single page)
asciidoctor --trace -o wcmp2-kpi.html index.adoc
# create PDF
asciidoctor --trace -r asciidoctor-pdf --trace -b pdf -o wcmp2-kpi.pdf index.adoc
```

# check links
```bash
find . -name "???.adoc" -exec asciidoc-link-check -p -c asciidoc-link-check-config.json {} \;
```

**Note**: `Makefile` provides shortcuts to these commands if you are able to run `make`.

## How to add a KPI

- copy `template.adoc` to a new file (i.e. `cp template.adoc core/new-kpi.adoc`)
- update accordingly
- add the file to the end of `index.adoc` with `include::new-kpi.adoc[]`
- check that build works
- ensure links in documents are functional
- commit the updates (`git add new-kpi.adoc && git commit -m 'add new-kpi' new-kpi.adoc index.adoc`)

## Conventions

- Fixed values to always use:
  - WCMP2 schema: https://schemas.wmo.int/wcmp/2.0.0/schemas/wcmp2-bundled.json
- always fence JSON snippets, single element names as code

## Releasing

See https://github.com/wmo-im/wcmp2/wiki/ReleaseProcess for more information.
