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
    ('CAM', 'Ca de Mama'),
    ('CAO', 'Ca de Ovario'),
    ('Otro', 'Otro Ca'),
)
DENSI = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
    )
BIRAD =(
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4a', '4a'),
        ('4b', '4b'),
        ('4c', '4c'),
        ('5', '5'),
        ('6', '6'),
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
)
ABORTOS = (
    ('PRO','Provocados'),
    ('PER', 'Perdida'),
)

MAMA = (
    ('PoM','Pequenas o Moderadas'),
    ('Vol', 'Voluminosas')
)
CONSISTENCIA = (
    ('Bl', 'Blandas faciles de Examinar'),
    ('Int', 'Intermedio'),
    ('F/MF', 'Firmes/Muy Firmes')
)
HALLAZGO = (
    ('Nod', 'Nodulo o Tumor'),
    ('Mas', 'Masa mal definida'),
    ('Sec', 'Secrecion'),
    ('O', 'Otros')
)
ATEC = (

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
    telefono = models.IntegerField('Teléfono(linea baja)',blank=True, null=True)
    celular = models.IntegerField('Telefono(celular) ',blank=True, null= True)
    direccion = models.CharField('Direccion habitual', max_length = 50, blank= True, null=True)
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
    cancer_mama = models.CharField(verbose_name='Alguien en la familia alguna vez tuvo Cancer de mama?',default='N',choices=SIONO, max_length=3)
    tenido_cancer = models.CharField(verbose_name='Conoces a alguien que haya tenido Cancer de mama?',default='N',choices=SIONO, max_length=3)

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
    mamoDiag = models.CharField('Mamografia Diagnóstica',max_length=100, null=True, blank=True)
    nodulo = models.CharField('Nodulo', max_length=100, null=True, blank=True)
    antecedentes = models.CharField('', max_length=2, choices=SION, default='N')
    antecedentes1 = models.CharField('Antecedentes familiares', max_length=100, null=True, blank=True)
    otros = models.CharField('',max_length=2, choices=SION, default='N')
    otros1 = models.CharField('Otros factores de riesgo', max_length=100, null=True, blank=True)
    densidad = models.CharField('Densidad', choices=DENSI, max_length=3)
    descripcion=models.TextField('Descripcion', max_length=100, null=True, blank=True)
    birads = models.CharField('BIRADS', choices = BIRAD, max_length=3)
    cero = models.CharField('0:Estudio insuficiente - Se recomienda', max_length=100)
    eg = models.TextField('EG', max_length=100, null=True, blank=True)
    hallazgos = models.CharField('Hallazgos', choices=SION, max_length=5)
    hallazgo = models.TextField('', max_length=300, null=True, blank=True)
    des_birads = models.TextField('Birads', max_length=300, null=True, blank=True)
    mamas =  models.CharField('Mamas', choices= MAMA, max_length=5)
    consistencia = models.CharField('Consistencia', choices=CONSISTENCIA,max_length=5)
    hallaz = models.CharField('Hallazgo', choices=SION, max_length= 5,null=False )
    hallazgo_si = models.CharField('', choices=HALLAZGO,max_length=5, null= True, blank=True, default=None)
    descripcio = models.TextField('Descripcion', max_length=100, null=True, blank=True)

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
    peso = models.DecimalField(max_digits=3, decimal_places=1)
    estatura = models.DecimalField(max_digits=3, decimal_places=2)
    # estatura = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    # def _get_IMC(self):
    #     return (self.peso/(self.estatura*self.estatura))

    IMC = models.DecimalField(max_digits=3, decimal_places=1)
    cirugia_mamaria = models.CharField('Cirugias Mamarias',default='N', max_length=3, choices=SION)
    otras_cirugias = models.CharField('Otras Cirugias',default='N', max_length=3, choices=SION)
    antecedentes_ca= models.CharField('Antecedentes de Cancer', max_length=8, choices=SION, null=True, default='N')
    antecedentes = models.CharField(' ', max_length=8, choices=CANCER, null=True, blank=True, default=None)
    atec_rt= models.CharField('Atec de RT', choices=SION,max_length=5, null= True,default='N')
    atc_rt = models.CharField(' ', choices=ATEC, max_length=5, null=True, blank=True, default=None)

    ante_fam = models.CharField('Hay antecedentes familiares?',default='N', max_length=3, choices=SION)
    detalles = models.TextField('detalles', null=True, blank=True, max_length=300)
    cancer_mama = models.CharField(verbose_name='Cáncer de mama', default='N', max_length=3, choices=SION)
    cancer_ovario = models.CharField(verbose_name='Cancer de ovario', default='N', max_length=3, choices=SION)
    cancer_prostata = models.CharField(verbose_name='Cancer de próstata', default   ='N', max_length=3, choices=SION)
    cancer_colon = models.CharField(verbose_name='Cancer de colon', default='N', max_length=3, choices=SION)
    cancer_otro = models.CharField(verbose_name='Otro Cancer', default='N', max_length=3, choices=SION)
    candetalles = models.TextField(verbose_name='Detalles', null=True, blank=True, max_length=100)
    menarca = models.CharField(default='N', max_length=3 , choices=SION)
    hijos = models.CharField(default='N',max_length=3, choices=SION)
    numero = models.IntegerField(null=True, blank=True)
    edad_primero = models.IntegerField(verbose_name='A que Edad se embarazo?', blank=True, null=True)
    amamanto = models.CharField(verbose_name='Amamanto?', default='N',max_length=3, choices=SION)
    tiempo = models.IntegerField(blank=True, null=True)
    anticonceptivos = models.CharField(verbose_name='Anticonceptivos Hormonales',choices=ANTICON,max_length=3, default='N')
    tiempo_anti=models.IntegerField(verbose_name='Tiempo',blank=True, null= True)
    menopausia = models.CharField(verbose_name='Menopausia',default='N',max_length=5,choices=SION)
    edad_meno = models.IntegerField(verbose_name='Edad', blank=True, null=True)
    anos_repro= models.CharField(verbose_name='Anos reproductivos', blank=True, null=True, max_length=50)
    trh = models.CharField(verbose_name='TRH',default='N',max_length=5,choices=SION)
    trh_opciones = models.CharField(' ',choices=VIAS,max_length=5, null=True, blank=True, default=None)
    abortos = models.CharField(verbose_name='Abortos',choices=SION, max_length=5, default='N')
    cuantos_abortos = models.CharField(verbose_name='Cuantos?', blank=True, null=True,max_length=50)
    tipo_aborto = models.CharField(verbose_name=' ', max_length=10, choices=ABORTOS, null=True, blank=True, default=None)
    primera_gesta= models.CharField(verbose_name='Primera gesta?', default='N',max_length=5,choices=SION)
    edad_gestacional = models.IntegerField(verbose_name='Edad gestacional', null=True, blank=True)

    def __unicode__(self):
        return str(self.registrado)

    # def __str__(self):
    #     return str(self.nombres) + " " + str(self.paterno)

