CREATE DATABASE musictrends;
CREATE USER music_user WITH PASSWORD 'music_password';
GRANT ALL PRIVILEGES ON DATABASE musictrends TO music_user;
ALTER DATABASE musictrends OWNER TO music_user;