certbot certonly --agree-tos --keep-until-expiring \
--webroot -w /var/www/letsencrypt --no-eff-email \
--email "${CERTBOT_EMAIL}" -d "${CERTBOT_DOMAINS}" \
#--dry-run

cert_dir="/etc/letsencrypt/live/${CERTBOT_DOMAINS}"

NGINX_CONF_DIR="/nginx/"

if [ -z "$CERTBOT_DOMAINS" ]; then
    echo "ERROR: $CERTBOT_DOMAINS environment variable is not set."
    exit 1
fi
#check if cert exist
if [ -d "${cert_dir}" ]; then
  echo "cert dir exists - cert received or exist"

  if [ -f "${NGINX_CONF_DIR}nginx-ssl.tmp" ]; then
    echo "-----  exchanging nginx to nginx.ssl  -----"

    if [ -e "${NGINX_CONF_DIR}nginx-ssl.conf" ]; then
      rm "${NGINX_CONF_DIR}nginx-ssl.conf"
      echo "nginx-ssl.conf  removed before applying a new one"
    fi

    echo "replacing DOMAIN NAME from .env "
    sed -i "s|\$CERTBOT_DOMAINS|${CERTBOT_DOMAINS}|g" "${NGINX_CONF_DIR}nginx-ssl.tmp"

    echo "   renaming nginx-ssl.tmp to nginx-ssl.conf"
    mv "${NGINX_CONF_DIR}nginx-ssl.tmp" "${NGINX_CONF_DIR}nginx-ssl.conf"

    echo "   removing old conf"
    rm "${NGINX_CONF_DIR}nginx.conf"
  else
    echo "ssl conf exist. skip"

  fi

else
  echo "ERROR Cert dir doesnot exists - cert not received"
  exit 1
fi