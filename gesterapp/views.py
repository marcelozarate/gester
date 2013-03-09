# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from gesterapp.forms import UserForm, TermoForm, MateForm, BombillaForm
from gesterapp.forms import PrestamoForm
from gesterapp.models import Usuario, Termo, Mate, Bombilla, Prestamo
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.util import ErrorList
from django.utils import simplejson


def home(request):
    if not request.user.is_authenticated():
        return TemplateResponse(request, 'gester/home.html',)
    else:
        return TemplateResponse(request, 'gester/homeuser.html',)


def about(request):
    return TemplateResponse(request, 'gester/about.html',)


class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return u''
#        return u'<div class="alert alert-error"><strong>&iexcl;Error!</strong>
#%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])
        error_list = ''.join(
            [u'<div class="error">{0}</div>'.format(e) for e in self])
        return (
            u'<div class="alert alert-error">'
            u'<strong>&iexcl;Error!</strong>{0}</div>'
        ).format(error_list)


@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, auto_id=False, error_class=DivErrorList)
        if form.is_valid():
            user = form.save(commit=False)
            user.fechaingreso = timezone.now()
            user.creadopor = request.user
            user.save()
            return HttpResponseRedirect(reverse('list-users'))
    else:
        form = UserForm()
    return TemplateResponse(request,
             'gester/add_user.html', {'form': form, })


@login_required
def add_termo(request):
    if request.method == 'POST':
        form = TermoForm(request.POST, auto_id=False, error_class=DivErrorList)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-termos'))
    else:
        form = TermoForm()
    return TemplateResponse(request,
             'gester/add_termo.html', {'form': form, })


@login_required
def add_mate(request):
    if request.method == 'POST':
        form = MateForm(request.POST, auto_id=False, error_class=DivErrorList)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-mates'))
    else:
        form = MateForm()
    return TemplateResponse(request,
             'gester/add_mate.html', {'form': form, })


@login_required
def add_bombilla(request):
    if request.method == 'POST':
        form = BombillaForm(request.POST,
                auto_id=False, error_class=DivErrorList)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-bombillas'))
    else:
        form = BombillaForm()
    return TemplateResponse(request,
             'gester/add_bombilla.html', {'form': form, })


@login_required
def list_users(request, orderby=None, ordertype=None):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        usuarios = Usuario.objects.all().order_by('id')
    except Usuario.DoesNotExist:
            return render_to_response('gester/list_users.html',
            {'usuario': usuarios,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('gester/list_users.html', {'usuario': usuarios,
        "mensaje": mensaje}, context_instance=RequestContext(request))


@login_required
def list_termos(request, orderby=None, ordertype=None):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        termos = Termo.objects.all().order_by('id')
    except termos.DoesNotExist:
            return render_to_response('gester/list_termos.html',
            {'termo': termos,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('gester/list_termos.html', {'termo': termos,
        "mensaje": mensaje}, context_instance=RequestContext(request))


@login_required
def list_mates(request, orderby=None, ordertype=None):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        mates = Mate.objects.all().order_by('id')
    except mates.DoesNotExist:
            return render_to_response('gester/list_mates.html',
            {'mate': mates,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('gester/list_mates.html', {'mate': mates,
        "mensaje": mensaje}, context_instance=RequestContext(request))


@login_required
def list_bombillas(request, orderby=None, ordertype=None):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        bombillas = Bombilla.objects.all().order_by('id')
    except bombillas.DoesNotExist:
            return render_to_response('gester/list_bombillas.html',
            {'bombilla': bombillas,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('gester/list_bombillas.html',
        {'bombilla': bombillas, "mensaje": mensaje},
        context_instance=RequestContext(request))


@login_required
def list_prestamos(request, orderby=None, ordertype=None):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        prestamos = Prestamo.objects.all().order_by('id')
    except prestamos.DoesNotExist:
            return render_to_response('gester/list_prestamos.html',
            {'prestamo': prestamos,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('gester/list_prestamos.html',
        {'prestamo': prestamos, "mensaje": mensaje},
        context_instance=RequestContext(request))


@login_required
def prestar(request):
    return TemplateResponse(request, 'gester/prestar.html',)


@login_required
def get_usuarios(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        usuarios = Usuario.objects.filter(nombre__icontains=q)[:20]
        results = []
        for usuario in usuarios:
            usuario_json = {}
            usuario_json['id'] = usuario.id
            usuario_json['label'] = usuario.nombre
            usuario_json['value'] = usuario.nombre
            results.append(usuario_json)
        data = simplejson.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


@login_required
def add_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST,
                auto_id=False, error_class=DivErrorList)
        if form.is_valid():
            prestamo = form.save(commit=False)

            if request.POST.get('usuarios'):
                miuser = request.POST.get('usuarios', '')
            else:
                miuser = ''
            prestamo.cliente = Usuario.objects.get(nombre__exact=miuser)
            prestamo.fecha = timezone.now()
            prestamo.devuelto = False
            prestamo.save()
            return HttpResponseRedirect(reverse('list-prestamos'))
    else:
        form = PrestamoForm()
    return TemplateResponse(request,
             'gester/add_prestamo.html', {'form': form, })
