all: clean run

run:
	python blog/blog.py

clean:
	find . -name "*.pyc" -delete
	
post:
	python blog/blog.py
	
rebuild:
	python blog/blog.py --rebuild

sync:
	rsync -av