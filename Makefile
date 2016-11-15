build:
	rm -rf public
	hugo

watch: clean
	hugo server -w

create-index:
	cd algolia;python make_algolia_index.py;cd ..

update-index:
	cd algolia;python sync_algolia_index.py;cd ..

make-index: create-index update-index

clean:
	-rm -rf public

sync:
	aws s3 --profile <yourawsprofile> sync --acl "public-read" public/ s3://example.com
	
build-deploy-local: build sync 

all: build-deploy-local bust-cache
