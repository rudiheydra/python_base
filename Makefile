install: 
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	
post-install:
	python -m textblob.download_corpora
	
lint:
	pylint --disable=R,C *.py devopslib
	
test:
	python -m pytest -vv test_*.py
	
format:
	black *.py devopslib/*.py
	
deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 949510079382.dkr.ecr.us-east-1.amazonaws.com
	docker build -t fast_api .
	docker tag fast_api:latest 949510079382.dkr.ecr.us-east-1.amazonaws.com/fast_api:latest
	docker push 949510079382.dkr.ecr.us-east-1.amazonaws.com/fast_api:latest
	
all: install post-install lint test format deploy