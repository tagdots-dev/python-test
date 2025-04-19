# NOTE: this file is managed by terraform
# Makefile

usage:
	@echo "Usage:"
	@echo "\tmake build"
	@echo "\tmake test"

build:
	@echo
	@echo "***************************************************************************"
	@echo "******************* Upgrade to the latest python build ********************"
	@echo "***************************************************************************"
	@echo
	python -m pip install -U build

	@echo
	@echo "***************************************************************************"
	@echo "******************** Build software package *******************************"
	@echo "***************************************************************************"
	@echo
	PYTHONWARNINGS=error python -m build

	@echo
	@echo "***************************************************************************"
	@echo "****** Install package into the current active Python environment *********"
	@echo "***************************************************************************"
	@echo
	python -m pip install -e .

test:
	@echo ""
	@echo "***************************************************************************"
	@echo "************************* Running coverage tests **************************"
	@echo "***************************************************************************"
	@echo ""
	coverage run -m unittest -v

	@echo ""
	@echo "Create an HTML report of the coverage of the files"
	coverage html

	@echo ""
	@echo "Report coverage statistics on modules"
	coverage report -m

.PHONY: help build test
