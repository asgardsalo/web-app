# Use a lightweight Python image with Apache
FROM python:3.10-slim

# Install Apache and required packages, then update all packages to latest security patches
RUN apt-get update && \
    apt-get install -y --no-install-recommends apache2 libapache2-mod-wsgi-py3 && \
    pip install --upgrade pip && \
    pip install flask mysql-connector-python && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# Set environment variables
ENV APP_HOME=/app
WORKDIR $APP_HOME

# Copy app files
COPY . $APP_HOME

# Ensure the web content/data is separate
VOLUME ["/app/data"]

# Configure Apache
COPY apache/flask.conf /etc/apache2/sites-available/000-default.conf

# Expose custom port
EXPOSE 8081

# Start Apache
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]