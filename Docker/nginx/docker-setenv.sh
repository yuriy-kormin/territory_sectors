#!/bin/sh
echo "certboot domains = ${CERTBOT_DOMAINS}"
if [ -n "$CERTBOT_DOMAINS" ]; then
  DOMAIN=$(echo "$CERTBOT_DOMAINS" | cut -d',' -f1)
  REACT_APP_BACKEND_URL="http://${DOMAIN}/graphql/"
  echo "Setting REACT_APP_BACKEND_URL to $REACT_APP_BACKEND_URL"
  export REACT_APP_BACKEND_URL
else
  echo "CERTBOT_DOMAINS environment variable is not set. REACT_APP_BACKEND_URL will use default."
fi