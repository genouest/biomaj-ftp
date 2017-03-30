# Biomaj ftp

Biomaj FTP server to access production banks

anonymous access is allow with login *anonymous* and any fake password.
Existing users can access server with the login and API key as password.

Only public or owned banks are accessible

# Config

config.yml contains the server configuration.
Mongo configuration should be the same one than biomaj.

Web endpoint refers to the biomaj API endpoint

# Run

export BIOMAJ_CONFIG=path_to_config.yml

python bin/biomaj_ftp_service.py

# Docker

To run in a Docker container, do not forget to open passive ports range (60000, 65535)
