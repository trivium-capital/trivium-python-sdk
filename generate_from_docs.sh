API_VERSION=$(cat docs.yaml | grep 'version: *' | cut -f2- -d:)
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v7.12.0 generate \
-i /local/docs.yaml \
-g python \
--additional-properties=packageName=trivium_python_sdk \
--additional-properties=packageVersion=$(echo $API_VERSION) \
-o /local