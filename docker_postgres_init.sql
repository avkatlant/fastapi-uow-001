CREATE USER backend_user_local WITH PASSWORD 'backend_password_local' CREATEDB;

ALTER ROLE backend_user_local SUPERUSER;
ALTER USER backend_user_local SET client_encoding='UTF8';
ALTER ROLE backend_user_local SET default_transaction_isolation TO 'read committed';
ALTER ROLE backend_user_local SET timezone TO 'UTC';

CREATE DATABASE backend_db_local
    WITH
    OWNER = backend_user_local
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

GRANT ALL PRIVILEGES ON DATABASE backend_db_local TO backend_user_local;

\c backend_db_local

GRANT ALL ON ALL TABLES IN SCHEMA public to backend_user_local;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to backend_user_local;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to backend_user_local;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION pg_trgm;
ALTER EXTENSION pg_trgm SET SCHEMA public;
UPDATE pg_opclass SET opcdefault = true WHERE opcname='gin_trgm_ops';
