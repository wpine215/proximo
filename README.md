# proximo
Location-based social network

## Installation (Debian/Ubuntu)
Update all packages and install basic utilities:

    $ sudo apt-get update -qq
    $ sudo apt-get install -y -qq unzip wget git`

Install Python and PostgreSQL:

    $ sudo apt-get install -y -qq python3 python3-dev python3-pip python3-virtualenv
    $ sudo apt-get install -y -qq postgresql postgresql-contrib python3-psycopg2

Install GeoDjango/PostGIS and dependencies:

    $ sudo apt-get install -y -qq binutils libproj-dev gdal-bin postgis

Clone the repository, initialize and activate venv (virtualenv might need to be added to PATH):

    $ git clone https://github.com/wpine215/proximo.git
    $ cd proximo
    $ virtualenv -p python3 env
    $ source env/bin/activate
    $ pip3 install -r requirements.txt

Set up PostgreSQL and PostGIS extension:

    $ sudo -u postgres createuser proximodb --interactive
    $ sudo -u postgres createdb proximo
    $ sudo -u postgres psql
    postgres=# alter user proximodb with encrypted password 'proximo';
    postgres=# grant all privileges on database proximo to proximodb;
    postgres=# \c proximo
    proximo=# CREATE EXTENSION postgis;
    proximo=# \q
    
Be sure to modify /backend/settings.py to reflect database credentials, host, and port.
Make sure localhost IP address (not 127.0.0.1) is added to ALLOWED_HOSTS in settings.py for deployment.
