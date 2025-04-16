#!/bin/sh
set -e  # Exit immediately if any command fails

# Set default values if environment variables are not provided
export APP_WORKERS="${APP_WORKERS:-1}"
export APP_PORT="${APP_PORT:-8000}"

# Run database migrations
litestar --app src.app:app database upgrade

# Start the Litestar application server
litestar --app src.main:app run \
  --workers "${APP_WORKERS}" \
  --host=0.0.0.0 \
  --port="${APP_PORT}"