# Use the official Apache HTTP Server image (Debian-based)
FROM httpd:2.4

# Copy your existing HTML file into the default web root
COPY index.html /usr/local/apache2/htdocs/index.html

# Configure Apache to listen on 8081 and 8082
RUN sed -i 's/Listen 80/Listen 8081\nListen 8082/' /usr/local/apache2/conf/httpd.conf && \
    echo '<VirtualHost *:8081>\nDocumentRoot "/usr/local/apache2/htdocs"\n</VirtualHost>' >> /usr/local/apache2/conf/extra/httpd-vhosts.conf && \
    echo '<VirtualHost *:8082>\nDocumentRoot "/usr/local/apache2/htdocs"\n</VirtualHost>' >> /usr/local/apache2/conf/extra/httpd-vhosts.conf && \
    echo 'Include conf/extra/httpd-vhosts.conf' >> /usr/local/apache2/conf/httpd.conf

# Expose both ports
EXPOSE 8081 8082