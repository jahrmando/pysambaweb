PySambaWeb
==========

A web application to change user passwords on Samba SMB

* Translation language automatic (English, Spanish)
* Password history
* Of course change your SMB password

INSTALLATION
------------
- Install dependencies.

`$ pip install-r requirements.txt`

- Create the configuration file.

`$ cp pysambaweb/local_settings.py.example pysambaweb/local_settings.py`

- Create the database

`$ python manage.py syncdb`

- Settings for SAMBA SMB service

`$ vim /etc/samba/smb.conf`

`#Add this configuration`

`passdb backend = smbpasswd`

`encrypt passwords = True`

`security = user`

`smb passwd file = /etc/samba/db/smbpasswd`

- Assign permissions

`chown apache /etc/samba/db/smbpasswd`

- Settings for SUDO

`$ visudo`

`#Add this configuration`

`apache ALL=(root) NOPASSWD:/usr/bin/smbpasswd`

TEST
----
- Run the service (dedug mode is enabled)

`$ python manage.py runserver`

- Run the service (dedug mode is disabled)

`$ python manage.py runserver - insecure`
