BIN="./bin"
CODE="./src/"
TEST="./test/"
JAVA=java
SELENIUM_SERVER=$(BIN)/selenium-server-standalone-2.48.2.jar
SELENIUM_FLAGS=-jar ${SELENIUM_SERVER} -log log/selenium.log 

test:
	@python -B -m unittest discover -s $(TEST) -p *_test.py 

install:
	@pip install -r requirements.txt

start-selenium:
	$(JAVA) $(SELENIUM_FLAGS) &

stop-selenium:
	kill -9 `pidof java`

start: start-selenium
stop: stop-selenium

.PHONY: test install
