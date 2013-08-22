# -*- encoding: utf-8 -*-
#!/usr/bin/env python
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import smbpasswd
import subprocess


class PySamba(object):
    """docstring for PySamba"""

    def saveUser(self, user, password):
        try:
            cmd = "/bin/echo -e '%s\n%s' | (/usr/bin/sudo /usr/bin/smbpasswd -s %s)" % (password, password, user)
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout_value, stderr_value = proc.communicate()
            if not stderr_value:
                return True
            else:
                return False
        except Exception, e:
            return False

    def changePasswd(self, user, oldpass, password):
        is_saved = False
        msg = _("User not found")
        try:
            with open(settings.SMB_DB) as file:
                lines = file.readlines()
            for line in lines:
                user_info = line.strip().split(':')
                if user in user_info:
                    if smbpasswd.nthash(oldpass) in user_info:
                        if self.saveUser(user, password):
                            is_saved = True
                            msg = _("Changed successfully")
                            break
                        else:
                            msg = _("Failed change")
                            break
                    else:
                        msg = _("Wrong password")
                        break
            return is_saved, msg
        except Exception, e:
            msg = _("Failed change")
            return is_saved, e

    def __init__(self):
        super(PySamba, self).__init__()
