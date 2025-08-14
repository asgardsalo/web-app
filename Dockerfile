# Use the official Apache HTTP Server image (Debian-based)
FROM httpd:2.4-alpine3.22

# Switch Apache to listen on 8081 (single internal port)
RUN sed -i 's/^Listen 80$/Listen 8081/' /usr/local/apache2/conf/httpd.conf \
    && echo 'IncludeOptional conf/extra/httpd-vhosts.conf' >> /usr/local/apache2/conf/httpd.conf

# Optional: create a vhost pointing to the default docroot
# (keeps things explicit; you can remove if you prefer the default)
RUN printf '%s\n' \
   '<VirtualHost *:8081>' \
   '  DocumentRoot "/usr/local/apache2/htdocs"' \
   '  <Directory "/usr/local/apache2/htdocs">' \
   '    Options Indexes FollowSymLinks' \
   '    AllowOverride All' \
   '    Require all granted' \
   '  </Directory>' \
   '</VirtualHost>' \
   > /usr/local/apache2/conf/extra/httpd-vhosts.conf

EXPOSE 8081
