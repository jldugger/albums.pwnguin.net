#######################
Photologue Demo Project
#######################

About
=====

This project is intended to be a standalone production deployable app for
django-photologue.

Prerequisites
=============:

- python (either 3.7, or 3.x).
- virtualenv strongly commended!

Development Setup
=================
**Note**: the project is configured so that it can run immediately with zero configuration
(especially of settings files).

Clone this code into your project folder::

	git clone https://github.com/jldugger/albums.pwnguin.net

Set up a virtualenv
        cd albums.pwnguin.net
        virtualenv --no-site-packages venv

Activate venv and Install dependencies::
        source venv/bin/activate
	pip install -r requirements.txt

The project is set up to run SQLite in dev so that it can be quickly started
with no configuration required (you can of course specify another database in
the settings file). To setup the database::

	./manage.py migrate

Follow the instructions to configure photologue here: `Photologue Docs <http://django-photologue.readthedocs.org/en/latest/pages/installation.html>`_

And finally run the project (it defaults to a safe set of settings for a dev
environment)::

	./manage.py runserver

Open browser to http://127.0.0.1:8000

Production Setup
================

WORK IN PROGRESS

You probably want to set up Apache `mod_wsgi`, or `uwsgi` and Nginx.

Settings
--------

`album_project/settings.py` defaults to a ready to run env for production. You shuld override
any settings -- DATABASES, SECRET_KEY, DEBUG, etc., -- by adding writing them to a
`album_project/local_settings.py`.

This project also supports a number of additional settings you can optionally define to add
functionality.

`GOOGLE_ANALTYICS_KEY`: unique ID embedded in the GA script to direct vistor data to your acct

`GOOGLE_ADWORDS_KEY`: unique ID for adsense account

`RAVEN_CONFIG`: unique ID to push uncaught exceptions to a Sentry logging server for recording
and alerting.

Thank you
=========
This project is based on the upstream django-photologue example project, which is
in turn based on the earlier `photologue_demo project <https://github.com/richardbarran/photologue_demo>`_.
This project included contributions and input from: crainbf, tomkingston, bmcorser.
