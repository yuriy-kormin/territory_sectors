#!/bin/sh

if [ -n "$CERTBOT_DOMAINS" ]; then
  DOMAIN=$(echo "$CERTBOT_DOMAINS" | cut -d',' -f1)
  REACT_APP_BACKEND_URL="https://${DOMAIN}/graphql/"
  echo "Setting REACT_APP_BACKEND_URL to $REACT_APP_BACKEND_URL"
  export REACT_APP_BACKEND_URL
else
  echo "CERTBOT_DOMAINS environment variable is not set. REACT_APP_BACKEND_URL will use default."
fi

cd /app/

echo "npm run build"
npm run build

echo "Starting react app"
npm start
