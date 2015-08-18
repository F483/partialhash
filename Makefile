# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


help:
	@echo "Some usefull development shortcuts."
	@echo "  clean      Remove all generated files."
	@echo "  test       Run tests and analisys tools."
	@echo "  devsetup   Setup development environment."
	@echo "  publish    Build and upload package to pypi."


clean:
	rm -rf env
	rm -rf build
	rm -rf dist
	rm -rf *.egg
	rm -rf *.egg-info
	find | grep -i ".*\.pyc$$" | xargs -r -L1 rm


devsetup: clean
	# setup virtual envs
	virtualenv -p /usr/bin/python2 env/py2
	virtualenv -p /usr/bin/python3 env/py3
	env/py2/bin/python setup.py develop
	env/py3/bin/python setup.py develop
	
	# install development tools                                                 
	env/py2/bin/pip install ipython                                             
	env/py3/bin/pip install ipython                                             
	env/py2/bin/pip install pudb                                                
	env/py3/bin/pip install pudb 


test: devsetup
	env/py2/bin/python setup.py test
	env/py3/bin/python setup.py test


profile: devsetup
	env/py2/bin/python tests/profile.py
	env/py3/bin/python tests/profile.py


publish: test
	@env/py3/bin/python setup.py register sdist upload


# import pudb; pu.db # set break point
