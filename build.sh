#!/bin/bash

# Build script for Netlify deployment
echo "Starting build process..."

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p netlify/functions

# Copy static files to publish directory
cp -r static/* ./publish/

echo "Build completed successfully!"
