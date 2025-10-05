API_VERSION=$(cat docs.yaml | grep 'version: *' | cut -f2- -d:)

# Update version in README.md
sed -i '' "s/- API version: .*/- API version: $API_VERSION/" README.md
sed -i '' "s/- Package version: .*/- Package version: $API_VERSION/" README.md

# Update version in setup.py
sed -i '' "s/VERSION = \".*\"/VERSION = \"$API_VERSION\"/" setup.py

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v7.12.0 generate \
-i /local/docs.yaml \
-g python \
--additional-properties=packageName=trivium_python_sdk \
--additional-properties=packageVersion=$(echo $API_VERSION) \
-o /local
