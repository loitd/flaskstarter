# flaskstarter
Loitd Flask Starter Template

# How to run
## Install VirtualEnvironment
```pip3 install virtualenvwrapper```
```pip3 install virtualenvwrapper-win```
`mkvirtualenv -p C:\Python36\python.exe rocket`
... Show all virtual environments:
`lsvirtualenv`
`rmvirtualenv rocket`
`cpvirtualenv ENVNAME [TARGETENVNAME]`
`allvirtualenv pip install -U pip`
... Switch to new created environment
`workon rocket`
... Save and reinstall the requirement
`(rocket)$ pip freeze > requirements.txt`
`pip install -r requirements.txt`
