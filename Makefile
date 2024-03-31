local_up:
	docker-compose -f docker-compose-local.yml up -d

local_logs:
	docker-compose -f docker-compose-local.yml logs -f

local:
	make local_up -i

local_down:
	docker-compose -f docker-compose-local.yml down

local_db_del:
	rm -rf pg_db_local/
