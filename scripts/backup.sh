#!/bin/bash

DATE=$(date +%Y-%m-%d)

mysqldump \
-u root \
-proot123 \
-h localhost \
disasteralert \
> backup_$DATE.sql

echo "Backup Completed"