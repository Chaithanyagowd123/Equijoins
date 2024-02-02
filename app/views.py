from django.shortcuts import render
from django.db.models import *
# Create your views here.
from app.models import *
from django.db.models.functions import Length


def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=20)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='CHICAGO')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)#False
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename='MARTIN')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(Q(deptno__dname='ACCOUNTING')|Q(deptno__dname='RESEARCH'))
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__isnull=True)

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    Empmgrobjects=Emp.objects.select_related('mgr').all()
    Empmgrobjects=Emp.objects.select_related('mgr').filter(ename='KING')
    Empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    Empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING',sal__gte=1200)
    Empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='JONES',sal__gte=1000)
    Empmgrobjects=Emp.objects.select_related('mgr').filter(Q(mgr=7698)|Q(mgr=7902))
    Empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__deptno=20)
    Empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__deptno=20,mgr__ename='JONES')
    Empmgrobjects=Emp.objects.select_related('mgr').filter(Q(ename='SMITH')|Q(ename='FORD'))
    Empmgrobjects=Emp.objects.select_related('mgr').filter(Q(deptno__deptno=10)|Q(deptno__deptno=30))
    Empmgrobjects=Emp.objects.select_related('mgr').filter(Q(deptno__deptno=10)|Q(deptno__deptno=30)&Q(sal__gte=1200))[:1:]
    Empmgrobjects=Emp.objects.select_related('mgr').filter(Q(deptno__deptno=10)|Q(deptno__deptno=30)&Q(sal__gte=1000))[2::]
    Empmgrobjects=Emp.objects.select_related('mgr')[2:6:]
   
    Empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__empno=7566)
    
    d={'Empmgrobjects':Empmgrobjects}
    return render(request,'selfjoins.html',d)



def emp_mgr_objects(request):
    emd=Emp.objects.select_related('mgr','deptno').all()
    emd=Emp.objects.select_related('mgr','deptno').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('mgr','deptno').filter(mgr='7902')
    emd=Emp.objects.select_related('mgr','deptno').filter(sal__gte=200)
    emd=Emp.objects.select_related('mgr','deptno').filter(ename__endswith='S')
    emd=Emp.objects.select_related('mgr','deptno').filter(ename__startswith='A')
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dname='ACCOUNTING')
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dlocation='NEWYORK')
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dname__startswith='S')
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dname__endswith='H')
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(deptno__deptno=10)|Q(deptno__deptno=30)&Q(sal__gte=1000))
    emd=Emp.objects.select_related('mgr','deptno').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('mgr','deptno').filter(mgr__isnull=False)
    emd=Emp.objects.select_related('mgr','deptno').filter(mgr__ename='JONES',sal__gte=100)
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dlocation__endswith='O')
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dlocation__startswith='D')
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(deptno__deptno=10)|Q(deptno__deptno=30))
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(ename='JONES')|Q(ename='ALLEN'))
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(deptno__deptno=10)|Q(deptno__deptno=30)&Q(sal__gte=1000))[2::]
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(ename='JONES')|Q(deptno=10))
    emd=Emp.objects.select_related('mgr','deptno').all().order_by('ename')
    emd=Emp.objects.select_related('mgr','deptno').all().order_by('-ename')[:2]
    emd=Emp.objects.select_related('mgr','deptno').all().order_by(Length('ename'))
    emd=Emp.objects.select_related('mgr','deptno').all().order_by(Length('ename').desc())
    emd=Emp.objects.select_related('mgr','deptno').all().order_by(Length('ename'))[:4]
    emd=Emp.objects.select_related('mgr','deptno').filter(hiredate__year=2021)
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__dname='ACCOUNTING')
    emd=Emp.objects.select_related('mgr','deptno').filter(deptno__deptno='20')
    emd=Emp.objects.select_related('mgr','deptno').filter(sal__isnull=False)
    emd=Emp.objects.select_related('mgr','deptno').filter(comm__isnull=True)


    d={'emd':emd}
    return render(request,'emp_mgr_objects.html',d)
