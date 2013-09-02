#!/usr/bin/env python
# -*- coding: utf-8 -*-


def extract(list,i):
    transfer=[]
    for j in range(i):
        transfer.append(list[j])
    return transfer
def monomef(list,m,i,k=1):
    a=-sum(extract(list,i))
    f=lambda(x): (10**a)*k*(x**(m-i))
    return f
def sommef(list,i):
    def f(x):
        a=0
        for j in range(i):
            a +=list[j](x)
        return a
    return f
def fpart(i):
    m=int(raw_input('nombre de Ka de la famille acidobasique no %s' %i))
    name=[]
    Concentrations=[]
    a=raw_input('nom du %s-acide' %m)
    name.append(a)
    a=float(raw_input('Concentration de %s' %(name[0])))
    Concentrations.append(a)
    for j in range(m):
        name.append(raw_input('nom de %s deprotone %s fois' %(name[0],j+1)))
        Concentrations.append(float(raw_input('concentration de %s' %(name[j+1]))))
    Tableau1=[name,Concentrations]
    pKalist=[]
    pKavalues=[]
    for j in range(m):
        pKalist.append('pKa %s/%s' %(name[j],name[j+1]))
        pKavalues.append(float(raw_input(pKalist[j])))
    c=0
    d=0
    partf=[]
    partg=[]
    for j in range(m+1):
        d +=j*Concentrations[j]
        c +=Concentrations[j]
        partf.append(monomef(pKavalues,m,j))
        partg.append(monomef(pKavalues,m,j,j))
    f=sommef(partf,m+1)
    g=sommef(partg,m+1)
    t=lambda(h): c*g(h)/f(h)-d
    return t
def Solver(f,y0=0,x0=7,a=0,b=14):
    u=f(a)
    d=0
    v=f(x0)
    w=f(b)
    while not (d==1000 or u==y0 or v==y0 or w==y0):
        d +=1
        if (u-y0)*(v-y0)<0:
            if (u-y0)/(v-y0)<-100:
                c=x0-2*(x0-a)*(v-y0)/(v-u)
                z=f(c)
                if (v-y0)*(z-y0)<0:
                    a=c
                    u=z
                else:
                    c=x0-(x0-c)*(v-y0)/(v-z)
                    z=f(c)
                    if (v-y0)*(z-y0)<0:
                        a=c
                        u=z
                    else:
                        x0=c
                        v=z
            elif (v-y0)/(u-y0)<-100:
                c=a+2*(x0-a)*(y0-u)/(v-u)
                z=f(c)
                if (u-y0)*(z-y0)<0:
                    x0=c
                    v=z
                else:
                    c=a+(c-a)*(y0-u)/(z-u)
                    z=f(c)
                    if (u-y0)*(z-y0)<0:
                        x0=c
                        v=z
                    else:
                        a=c
                        u=z
            else:
                c=a+(x0-a)*(y0-u)/(v-u)
                z=f(c)
                if (u-y0)*(z-y0)<0:
                    x0=c
                    v=z
                else:
                    a=c
                    u=z
        elif (v-y0)*(w-y0)<0:
            c=x0+(b-x0)*(y0-v)/(w-v)
            z=f(c)
            if (w-y0)*(z-y0)<0:
                x0=c
                v=z
            else:
                b=c
                w=z
        else:
            print "Erreur : TVI non applicable"
            d=1000
    if abs(u-y0)<1.0e-6:
        return a
    elif abs(v-y0)<1.0e-6:
        return x0
    elif abs(w-y0)<1.0e-6:
        return b
    else:
        print "Aucune valeur trouvee"
        return "ERROR"
def SolvAcidBas():
    n=int(raw_input('nombre de familles acido-basiques'))
    k=1.0e-14
    t=lambda(h): (k/h)-h
    fonctions=[t]
    for i in range(n):
        fonctions.append(fpart(i+1))
    u=sommef(fonctions,n+1)
    p=lambda(h): 10**-h
    a=tuple(raw_input("Connaissez-vous une valeur approximative du pH?\nSi oui entrez 'Oui', pH0.\nSi vous savez que le pH est acide ou basique entrez 'Oui','A' (ou B)\nSinon entrez 'non'"))
    def f(x):
        return u(p(x))
    if a[0]=='Oui':
        if a[1]=='A':
            pH=Solver(f,0,3.5,0,7)
        elif a[1]=='B':
            pH=Solver(f,0,10.5,7)
        else:
            pH=Solver(f,0,a[1])
    else:
        pH=Solver(f)
    print "pH=%s" %(pH)
    return pH
SolvAcidBas()
