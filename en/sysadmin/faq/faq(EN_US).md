Frequently asked questions and our answers

# How do I make a service accessible via TCP port?

The example of PostgreSQL, which runs in its own docker container:

PostgreSQL and the other services are by default not directly TCP port accessible but only docker internally.

To allow this, add the Start command for the PostgreSQL container to the line:

		-p 127.0.0.1:5432:5432 \

... for an availability on the IP address 127.0.0.1, so only locally on the same system.

You can also specify an official IP, which the server already uses, instead of 127.0.0.1.

In any case, the container must be re-created by PostgreSQL. To meet all dependencies, all containers should be terminated and recreated.

## Please note

In the case of addresses other than 127.0.0.1, a firewall should be used to ensure that only trustworthy accesses occur.

## Good to know

In addition, there is, of course, access control within PostgreSQL.

Here is the procedure for viewing this configuration:

    docker exec -ti easydb-pgsql cat /etc/postgresql/9.4/main/pg_hba.conf

Instead of "cat ..." you can also specify "bash" and then move in the container. With apt-get install, you can also install programs there. However, these are only available temporarily until the container is generated the next time.