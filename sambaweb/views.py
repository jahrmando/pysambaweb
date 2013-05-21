# -*- encoding: utf-8 -*-
# Create your views here.
from django.conf import settings
from django.shortcuts import render
from sambaweb import forms
from sambaweb.models import User, HistPassword
from pysamba import PySamba
import smbpasswd
from django.utils.translation import ugettext_lazy as _


def index(request):
    msg = ''
    result = False
    is_valid = False
    pysmb = PySamba()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            is_valid = True
            nickname = form.cleaned_data['nickname']
            oldpasswd = form.cleaned_data['oldpasswd']
            newpasswd = form.cleaned_data['newpasswd']
            retpasswd = form.cleaned_data['retpasswd']
            if newpasswd == retpasswd:
                if not(newpasswd == oldpasswd) and not(newpasswd == settings.DEFAULT_PASSWD):
                    myuser = User.objects.filter(username=nickname)
                    if myuser.count() > 0:
                        u = User.objects.get(username=nickname)
                        records = HistPassword.objects.filter(user=u).order_by('date_change')
                        records.reverse()[:settings.HISTORY_SIZE]
                        gosave = True
                        for rec in records:
                            if rec.password == smbpasswd.nthash(newpasswd):
                                gosave = False
                                break
                        if gosave:
                            result, msg = pysmb.changePasswd(nickname, oldpasswd, newpasswd)
                            if result:
                                histpasswd = HistPassword(user=u, password=smbpasswd.nthash(newpasswd))
                                histpasswd.save()
                        else:
                            msg = _("You can not use old passwords")
                    else:
                        result, msg = pysmb.changePasswd(nickname, oldpasswd, newpasswd)

                        if result:
                            nvuser = User(username=nickname)
                            nvuser.save()
                            histpasswd = HistPassword(user=nvuser, password=smbpasswd.nthash(newpasswd))
                            histpasswd.save()
                else:
                    msg = _("Your new password is not valid")
            else:
                msg = _("Failed confirmation of your new password")
    else:
        form = forms.UserForm()

    return render(request, 'sambaweb/index.html', {
        'form': form,
        'is_valid': is_valid,
        'result': result,
        'message': msg,
    })
