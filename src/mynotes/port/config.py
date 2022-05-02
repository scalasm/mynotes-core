"""Configuration properties."""
import os

# Stack region - This is set directly by AWS
AWS_REGION = os.getenv("AWS_REGION", "eu-west-1")

# Localstack endpoint, if available
LOCALSTACK_ENDPOINT = os.getenv("LOCALSTACK_ENDPOINT", None)

# HTTP port for the standalone UVicorn HTTP server
MYNOTES_HTTP_PORT = int(os.getenv("MYNOTES_HTTP_PORT", "8000"))
# Enable / disable the development mode (e.g., live code reload)
MYNOTES_DEV_MODE = bool(os.getenv("MYNOTES_DEV_MODE", "True"))
