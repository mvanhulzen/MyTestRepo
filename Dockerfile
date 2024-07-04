FROM python:3

WORKDIR /usr/src/app

RUN echo precopy
COPY ./src .
RUN echo postcopy

RUN pip install --no-cache-dir -r requirements.txt

# Install cron
RUN apt-get update && apt-get install -y cron

# Add crontab file in the cron directory
COPY crontab /etc/cron.d/crontab

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontab

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Apply cron job
RUN crontab /etc/cron.d/crontab

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log