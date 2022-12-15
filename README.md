# mule-sys-python
Mule4 Example. How to use Python 2.x with MuleSoft

## Prerequisite

Add the following Python 2.x Libraries under src/main/resources/lib
- requests
- urllib3
- chardet
- certifi
- idna

## Add the Python Path

-M-Dpython.path=<< Path with Libraries>>

- Dev machine -M-Dpython.path=C:\workspace\mule-sys-python\src\main\resources\lib
- CH 1.0 python.path=/opt/mule/mule-4.4.0/apps/mule-sys-python/lib
- CH 2.0 python.path=/opt/mule/apps/mule-sys-python/lib
