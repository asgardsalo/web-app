# Use a lightweight Linux base with Apache
FROM ubuntu:22.04

# Install Apache
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy your index.html into Apache's web root
COPY index.html /var/www/html/index.html

# Configure Apache to listen on ports 8081 and 8082
RUN sed -i 's/Listen 80/Listen 8081\nListen 8082/' /etc/apache2/ports.conf && \
    echo '<VirtualHost *:8081>\nDocumentRoot /var/www/html\n</VirtualHost>' > /etc/apache2/sites-available/000-default.conf && \
    echo '<VirtualHost *:8082>\nDocumentRoot /var/www/html\n</VirtualHost>' >> /etc/apache2/sites-available/000-default.conf

# Expose both ports
EXPOSE 8081 8082

# Start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]