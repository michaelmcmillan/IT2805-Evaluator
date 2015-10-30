BIN="./bin"
CODE="./src/"
TEST="./test/"
JAVA=java
SELENIUM_FLAGS=-jar
SELENIUM_SERVER=$(BIN)/selenium-server-standalone-2.48.2.jar

test:
	@python -B -m unittest discover -s $(TEST) -p *_test.py 

install:
	@pip install -r requirements.txt

start:
	$(JAVA) $(SELENIUM_FLAGS) $(SELENIUM_SERVER)

.PHONY: test install
