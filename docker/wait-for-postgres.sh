#!/bin/sh
# wait-for-postgres.sh
set -e
host="$1"
shift
cmd="$@"
until PGPASSWORD="pwd1234" psql -h "$host" -d "test_db" -U "test" -c '\q'; do
>&2 echo "Postgres is unavailable - sleeping"
sleep 1
done
>&2 echo "Postgres is up - executing command"
exec $cmd