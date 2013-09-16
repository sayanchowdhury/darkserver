#!/usr/bin/env python
"""darkserver"""
from distutils.core import setup
from distutils.core import Command
from setuptools import find_packages
import os

setup(name='darkserver',
      version='0.8.2',
      description="GNU build-id web service",
      long_description = "GNU build-id web service",
      platforms = ["Linux"],
      author="Kushal Das",
      author_email="kushaldas@gmail.com",
      url="https://github.com/kushaldas/darkserver",
      license = "http://www.gnu.org/copyleft/gpl.html",
      packages = find_packages(exclude=['tests']),
      include_package_data = True,
      data_files=[('/etc/httpd/conf.d/', ['configs/darkserver-httpd.conf']),
          ('/usr/sbin/', ['configs/darkserver.wsgi', 'darkbuildqueue',\
                          'darkjobworker', 'darkproducer', 'darkdashboard']),
          ('/etc/darkserver/', ['darkserverweb/settings.py', 'configs/darkserverweb.conf',\
                                'configs/dark-distros.json', 'configs/darkjobworker.conf',\
                                'configs/redis_server.json', 'configs/email.json',\
                                'configs/darkserverurl.conf']),
          ('/usr/share/darkserver/static', ['static/index.html', 'static/404.html', \
                                            'static/500.html']), ]
      )
