#- * - coding: utf - 8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

SIONO = (
    ('S', 'Si'),
    ('N', 'No'),
    )
SION = (
        ('S','Si'),
        ('N','No'),
    )
SEXOS = (
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    )

SIONO2 = (
        ('S','Si'),
        ('N','No'),
        ('NS', 'No se'),

    )
HACER = (
        ('R', 'REGULARMENTE'),
        ('A', 'A veces'),
        ('NU', 'NUNCA'),
    )
CANCER = (
    ('N','No'),
    ('CAM', 'Ca de Mama'),
    ('CAO', 'Ca de Ovario'),
    ('Otro', 'Otro Ca'),
)
ATEC = (
    ('T','Toracica'),
    ('G', 'Ginecol'),
    ('O', 'Otro'),
)
DENSI = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
    )
BIRAD =(
        ('0', 'Estudio insuficiente - Se recomienda'),
        ('1', 'Normal'),
        ('2', 'Anormal,Benigno'),
        ('3', 'Anormal, probablemente benigno'),
        ('4a', 'Anormal, probablemente benigno (baja)'),
        ('4b', 'Anormal, probablemente benigno(intermedia) '),
        ('4c', 'Anormal, probablemente benigno(alta)'),
        ('5', 'Anormal, maligno'),
        ('6', 'Anorma, maligno ya biopsiado'),
)
ANTICON =(
    ('S','SI'),
    ('N','NO'),
    ('A','ACO'),
    ('I','IM')
)
VIAS = (
    ('V.O','Via Oral'),
    ('G','Gel'),
    ('I','Intramuscular'),
    ('O','Otros'),
    ('NO','Ninguno')
)
ABORTOS = (
    ('PRO','Provocados'),
    ('PER', 'Perdida'),
    ('NO', 'Ninguno')
)

MAMA = (
    ('PoM','Pequenas o Moderadas'),
    ('Vol', 'Voluminosas')
)
CONSISTENCIA = (
    ('Bl', 'Blandas o faciles de Examinar'),
    ('Int', 'Intermedio'),
    ('F/MF', 'Firmes/Muy Firmes')
)
HALLAZGO = (
    ('NO', 'NO'),
    ('Nod', 'Nodulo o Tumor'),
    ('Mas', 'Masa mal definida'),
    ('Sec', 'Secrecion'),
    ('O', 'Otros')
)
ATEC = (
    ('N','No'),
    ('T','Toracica'),
    ('G','Ginecologica'),
    ('O', 'Otro')
)
class Persona(models.Model):


    cedula = models.CharField(blank=True, null=True, unique=True, max_length=10)
    nombres = models.CharField(max_length=50, blank=False, null=False)
    paterno = models.CharField('Apellido Paterno',max_length=20, blank=False, null=False)
    materno = models.CharField('Apellido Materno',max_length=20, blank=True, null=True)
    del_marido = models.CharField('Apellido del Marido',max_length=20, blank=True, null=True)
    fecha_nac = models.DateField(blank=False, null=False)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null= True)
    direccion = models.CharField(max_length = 50, blank= True, null=True)
    departamento = models.CharField(max_length=50, blank= True, null=True)
    localidad = models.CharField(max_length=50, blank=True, null=True)
    institucion = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=3, choices=SEXOS,null= False)
    # sexo = MultiSelectField(choices=SEXOS, null=True)
    ocupacion = models.CharField(max_length = 50, blank = True, null = True)
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    AEM = models.CharField(verbose_name='Sabes lo que es?',default='N',choices=SIONO, max_length=3)
    loHace = models.CharField(verbose_name='Lo haces?', choices=HACER, default='NU' , max_length=3)
    bulto_pecho = models.CharField(verbose_name='Alguna vez sentiste un bulto en el pecho?',null=False,default='N',choices=SIONO2, max_length=3)
    problema_mama = models.CharField(verbose_name='Alguna vez consultaste por un problema de la mama?',choices=SIONO,default='N', max_length=3)
    mama_detalle= models.CharField(verbose_name='Cual',max_length= 200, blank=True, null= True)
    hizo_mamo = models.CharField(verbose_name='Alguna vez te hiciste Mamografia?',default='N',choices=SIONO, max_length=3)
    eco_mama= models.CharField(verbose_name='Alguna vez te hiciste una ecografia mamaria?',default='N',choices=SIONO, max_length=3)
    cancer_mama = models.CharField(verbose_name='Alguien en la familia alguna vez tuvo cancer de mama?',default='N',choices=SIONO, max_length=3)
    tenido_cancer = models.CharField(verbose_name='Conoces a alguien que haya tenido cancer de mama?',default='N',choices=SIONO, max_length=3)

    # def __unicode__(self):
    #     return str(self.cedula)

    def __unicode__(self):
        return "%s - %s %s %s"%(self.cedula,self.nombres,self.paterno,self.materno)

    # def __unicode__(self):
    #     return self.nombres


    class Meta:
        verbose_name = 'Ficha de Paciente'
        verbose_name_plural = 'Ficha de Pacientes'


class Mamografia(models.Model):
    class Meta:
        verbose_name = 'Mamografia'
        verbose_name_plural = 'Mamografias'

    # registrado = models.OneToOneField(
    #     Persona, null=False, blank=False,
    #     on_delete=models.CASCADE,
    #     #primary_key=True
    # )
    registrado = models.ForeignKey(Persona, unique=True)
    mamoDespi = models.CharField('Mamografia despistaje',max_length=100, null=True, blank=True)
    mamoDiag = models.CharField('Mamografia Diagnostica',max_length=100, null=True, blank=True)
    nodulo = models.CharField('Nodulo', max_length=100, null=True, blank=True)
    antecedentes = models.CharField('Antecedentes familiares', max_length=100, null=True, blank=True)
    otros = models.CharField('Otros factores de riesgo',max_length=100, null=True, blank=True)
    densidad = models.CharField('Densidad', choices=DENSI, null=True, max_length=3, blank=True)
    descripcion=models.CharField('Descripcion', max_length=100, null=True, blank=True)
    birads = models.CharField('BIRADS', choices = BIRAD, null= True, max_length=3, blank=True)
    eg = models.CharField('EG', max_length=100, null=True, blank=True)
    hallazgos = models.CharField('Hallazgos?, si o no y descripcion', max_length=100, null=True,blank=True)
    des_birads = models.CharField('Birads', max_length=150, null=True, blank=True)
    mamas =  models.CharField('Mamas', choices= MAMA,null=True, blank=True, max_length=5)
    consistencia = models.CharField('Consistencia', choices=CONSISTENCIA, null=True, blank=True,max_length=5)
    #hallazgo = models.CharField('Hallazgo', choices=SIONO, null=True, blank=True, max_length= 5 )
    hallazgo_si = models.CharField('Hallazgo', choices=HALLAZGO, null=True, blank=True,max_length=5)
    descripcio = models.CharField('Descripcion', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return str(self.registrado)


class Antecedentes(models.Model):

    class Meta:
        verbose_name = 'Ficha de Recoleccion de Datos'
        verbose_name_plural = 'Ficha de Recoleccion de Datos'

    # registrado = models.OneToOneField(
    #     Persona, null=False, blank=False,
    #     on_delete=models.CASCADE,
    #     #primary_key=True
    #
    # )
    registrado = models.ForeignKey(Persona,unique=True)
    dire_actual= models.CharField(verbose_name='Direccion Actual',blank=True, null=True,max_length=50)
    de_quien= models.CharField(verbose_name='De quien es esta direccion?',blank=True, null=True,max_length=50)
    peso = models.IntegerField(blank=True, null=True)
    talla = models.IntegerField(blank=True, null=True)
    IMC= models.IntegerField(blank=True, null=True)
    cirugia_mamaria = models.CharField('Cirugias Mamarias',default='N', max_length=3, choices=SION)
    otras_cirugias = models.CharField('Otras Cirugias',default='N', max_length=3, choices=SION)
    antecedentes = models.CharField('Antecedentes de Cancer',default='N', max_length=8, choices=CANCER)
    atec_rt= models.CharField('Atec de RT', choices=ATEC, default=False,max_length=5, null=True, blank=True)
    ante_fam = models.CharField('Hay antecedentes familiares?',default='N', max_length=3, choices=SION)
    detalles = models.CharField('detalles', null=True, blank=True, max_length=100)
    cancer_mama = models.CharField(verbose_name='Cancer de mama', default='N', max_length=3, choices=SION)
    cancer_ovario = models.CharField(verbose_name='Cancer de ovario', default='N', max_length=3, choices=SION)
    cancer_prostata = models.CharField(verbose_name='Cancer de prostata', default   ='N', max_length=3, choices=SION)
    cancer_colon = models.CharField(verbose_name='Cancer de colon', default='N', max_length=3, choices=SION)
    cancer_otro = models.CharField(verbose_name='Otro cancer', default='N', max_length=3, choices=SION)
    candetalles = models.CharField(verbose_name='Detalles', null=True, blank=True, max_length=100)
    hijos = models.CharField(default='N',max_length=3, choices=SION)
    numero = models.IntegerField(null=True, blank=True)
    edad_primero = models.IntegerField(verbose_name='Edad del Primero?', blank=True, null=True)
    amamanto = models.CharField(verbose_name='Amamanto?', default='N', max_length=3, choices=SION)
    tiempo = models.IntegerField(blank=True, null=True)
    anticonceptivos = models.CharField(choices=ANTICON,max_length=3, default='N')
    tiempo_anti=models.IntegerField(verbose_name='Tiempo',blank=True, null= True)
    menopausia = models.CharField(verbose_name='Menopausia',default='N',max_length=5,choices=SION)
    edad_meno = models.IntegerField(verbose_name='Edad', blank=True, null=True)
    anos_repro= models.CharField(verbose_name='Años reproductivos', blank=True, null=True, max_length=50)
    trh = models.CharField(verbose_name='THR',default='N',max_length=5,choices=SION)
    trh_opciones = models.CharField(verbose_name='Opciones',choices=VIAS,max_length=5, default='NO', null=True, blank=True)
    abortos = models.CharField(verbose_name='Abortos',choices=ABORTOS, max_length=5, default='NO')
    cuantos_abortos = models.CharField(verbose_name='Cuantos?', blank=True, null=True,max_length=50)
    primera_gesta= models.CharField(verbose_name='Primera gesta?', default='N',max_length=5,choices=SION)
    edad_gestacional = models.IntegerField(verbose_name='Edad gestacional', null=True, blank=True)

    def __unicode__(self):
        return str(self.registrado)

    # def __str__(self):
    #     return str(self.nombres) + " " + str(self.paterno)

