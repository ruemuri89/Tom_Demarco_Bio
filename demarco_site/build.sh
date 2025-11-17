#!/usr/bin/env bash
# Render build script for Django

# Exit on errors
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt


# Run database migrations
python manage.py migrate --noinput

echo "Loading seed data..."
python manage.py loaddata demarco_seed.json || echo "Seed data already loaded or skipped."

# Collect static files
python manage.py collectstatic --noinput
