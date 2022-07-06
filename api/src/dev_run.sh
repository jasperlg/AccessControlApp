#!/bin/bash

echo "Setting up database..."
exec python3 -u setup.py &

echo "Starting application..."
exec python3 -u app.py
