# Schemas

This directory contains the WCMP2 source schemas.  The schemas are managed
using JSON Schema (https://json-schema.org/draft/2020-12/schema) and represented
in YAML.

## Generating the JSON schema bundle

[Stoplight Studio](https://stoplight.io/studio) (free and open source) is a full GUI environment (web-based
or desktop) for designing schemas, models and APIs (JSON/YAML/OpenAPI).

To generate the WCMP2 JSON schema, following these steps:

- open Stoplight Studio
- click "Open Existing Folder"
- point to the `schemas/` directory
- ensure schema has no errors ("0 Issues" in the top right pane)
- click "Open"
- on the right hand pane, right-click the file `wcmpRecordGeoJSON.yaml` and select "Export"
- select the following from the dialogue box:
  - Format: JSON
  - References: Bundled (Recommended)
  - X-Extensions: unchecked
- click "Save to file"
- save file to the root of this repository, i.e. `/wcmp2-bundled.json`
- commit changes

Note: the above are manual steps to verify and generate the JSON Schema bundle.  Future updates will
include automated workflow via GitHub Actions.
