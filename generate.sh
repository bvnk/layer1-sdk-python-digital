curl "https://api.sandbox.layer1.com/digital/api-docs" | jq | sed 's/"openId": \[/"oauth2": \[/g' > digital.json

INPUT_FILE="digital.json"
BASE_PACKAGE="com_layer1_clients_digital"
GROUP_ID="com.layer1.clients"
ARTIFACT_ID="digital"

openapi-generator generate -i digital.json -g python -o . \
  --additional-properties hideGenerationTimestamp=true \
  --additional-properties groupId=${GROUP_ID} \
  --additional-properties artifactId=${ARTIFACT_ID} \
  --additional-properties invokerPackage=${BASE_PACKAGE}_invoker \
  --additional-properties apiPackage=${BASE_PACKAGE}_api \
  --additional-properties modelPackage=${BASE_PACKAGE}_model \
  --additional-properties enumUnknownDefaultCase=true \
  --additional-properties generateBuilders=true \
  --additional-properties useSingleRequestParameter=true \
  --additional-properties disallowAdditionalPropertiesIfNotPresent=false 

echo "digital.json" >> .gitignore
echo ".idea/" >> .gitignore

