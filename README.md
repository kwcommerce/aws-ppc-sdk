# How to generate SDK for a specific set of endpoints?

```bash
docker run --rm \
  -v $PWD:/local openapitools/openapi-generator-cli generate \
  --input-spec-root-directory /local/sponsored_display/schemas \
  -g python \
  -o /local/sponsored_display --additional-properties=generateSourceCodeOnly=true
```