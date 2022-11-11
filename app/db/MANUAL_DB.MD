# DB MANUAL

To work with database without changing the alembic and sqlalchemy settings you should set it properly:

 * It should be create with docker image of postgresql
 * The container should be named flats-postgres with postgres password 'password'
 * The database should be named flatsdb
 * The user in postgres who's going to work with the database should be named flatsuser with password 'password'
 * The user should be granted with all right to manage the database


# Commands to run

## **DOCKER COMMAND**
sudo docker run -dp 5432:5432 --name flats-postgres -e POSTGRES_PASSWORD=password postgres:alpine

## **interact with** *flats-postgres* **container**
sudo docker exec -it flats-postgres sh

## **open postgres console**
psql -U postgres

## **create user** *flatsuser* **with password** *password*
create user flatsuser with encrypted password 'password';

## **create db** *flatsdb*
create database flatsdb;

## **GRANT ALL RIGHTS TO WORK WITH** *flatsdb* **TO** *flatsuser*

grant all privileges on database flatsdb to flatsuser;

\c flatsdb;

grant all on schema public to flatsuser;

# Connect docker containers

## **Create a user-defined bridge network** *tulip-net*
docker network create tulip-net

## **Start a container and connect it to the bridge**
docker run --rm --net tulip-net --name tulipnginx -d nginx 

## **Connect containers to the bridge**
docker network connect tulip-net _container_
