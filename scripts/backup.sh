#!/bin/bash

DATE=$(date +%Y-%m-%d)

docker exec disasteralert-mysql \
mysqldump -u root -proot123 disasteralert \
> backups/backup_$DATE.sql

echo "Backup Completed"