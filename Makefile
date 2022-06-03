PYCACHE := $(shell find -regex ".*__pycache__")
PYCACHE := $(subst ./,,$(PYCACHE))
.phony: clean
clean: FORCE
	rm -rf $(PYCACHE)
FORCE:
