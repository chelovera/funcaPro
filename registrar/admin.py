from django.contrib import admin
# from multiselectfield.admin import msf_filter
# from multiselectfield.admin import MSFChoiceListFilter
from registrar.forms import MamografiaForm, AntecedentesForm
from .models import Persona, Mamografia, Antecedentes
from dal import autocomplete

from registrar.autocomplete import PersonaAutocomplete

# from .forms import PersonForm
# Register your models here.

# class EncuestaAdmin(admin.ModelAdmin):
#     # model = Encuesta
#     # list_display = ['registrado']
#     # list_filter = (
#     #       ('p1', MSFChoiceListFilter),
#     # )
#
#     fieldsets = (
#          ('AEM AUTOEXAMEN MAMARIO', {
#              'fields': ('AEM', 'loHace', 'p2', 'p3', 'p4', 'p5', 'p6'),
#          }),
#     )
#      # extra = 5
#      # class Meta:
#      #     model = Encuesta
#
#
class AdminRegistrado(admin.ModelAdmin):
    #inlines = [encuestaInLine]
    list_display = [
                    "nombres",
                    "paterno",
                    "materno",
                    "del_marido",
                    "cedula",
                    "sexo",
                    "direccion",
                    "departamento",
                    "localidad",
                    "institucion",
                    "ocupacion",
                    "actualizado"]

    # form = RegistradoForm
    list_filter = ['cedula',]
    ordering = ['cedula',]


    fieldsets = (
        ('IDENTIFICACION',{

            'fields': ( ('paterno', 'materno', 'del_marido'),
                        'nombres', ('sexo', 'fecha_nac'),
                        ('cedula', 'ocupacion'))
        }),
        ('DIRECCION', {
            'fields': ( ('direccion','departamento', 'localidad','institucion'),
                        ('telefono', 'celular'))
        }),
        ('AEM AUTOEXAMEN MAMARIO', {
            'fields': ('AEM', 'loHace','bulto_pecho',
                       ('problema_mama', 'mama_detalle'),
                       'hizo_mamo','eco_mama','cancer_mama',
                       'tenido_cancer'),
        }),

    )
    radio_fields = {'sexo':admin.VERTICAL,
                    'AEM':admin.VERTICAL,
                    'loHace':admin.HORIZONTAL,
                    'bulto_pecho':admin.HORIZONTAL,
                    'problema_mama':admin.VERTICAL,
                    'hizo_mamo':admin.VERTICAL,
                    'eco_mama':admin.VERTICAL,
                    'cancer_mama':admin.VERTICAL,
                    'tenido_cancer':admin.VERTICAL}
# class AdminMamo(admin.ModelAdmin):
#     list_display = ["registrado.nombres", "registrado.cedula"]

class AdminMamo(admin.ModelAdmin):
    form = MamografiaForm

    list_display = [
        "registrado",
        "mamoDespi",
        "mamoDiag",
        "nodulo",
        "antecedentes",
        "otros",
        "densidad",
        "descripcion",
        "birads",
        "eg",
        "hallazgos",
        "des_birads",
        "mamas",
        "consistencia",
        "hallazgo_si",
    ]
    fieldsets = (
            ('MAMOGRAFIA', {
            'fields': ('registrado','mamoDespi', 'mamoDiag',('antecedentes', 'antecedentes1'), ('otros','otros1'),
                        'densidad', 'descripcion')
            }),
            ('BIRADS', {
                'fields': ('birads',)

            }),

            ('ECOGRAFIA MAMARIA', {
                'fields': ('eg', ('hallazgos','hallazgo'), 'des_birads')
            }),
            ('PALPACION', {
                'fields': ('mamas', 'consistencia', 'hallazgo_si','descripcio')
            }),
    )
    radio_fields = {'antecedentes':admin.HORIZONTAL,'otros':admin.HORIZONTAL,
                    'densidad': admin.HORIZONTAL, 'birads': admin.VERTICAL,
                    'mamas':admin.VERTICAL,
                    'consistencia':admin.VERTICAL,
                    'hallazgos': admin.VERTICAL,
                    'hallazgo_si':admin.VERTICAL,
                    }

class AdminAntecedentes(admin.ModelAdmin):
    form = AntecedentesForm
    list_display = [
                    "registrado",
                    "peso","estatura",
                    "dire_actual", "de_quien",
                    "IMC","cirugia_mamaria","otras_cirugias",
                    "antecedentes","ante_fam",
                    "cancer_mama","cancer_ovario","cancer_prostata",
                    "cancer_colon","cancer_otro",
                    "hijos","numero","edad_primero",
                    "amamanto","tiempo","anticonceptivos",
                    "tiempo_anti"]
    fieldsets = (
        ('PACIENTE',{
            'fields':('registrado','peso','estatura','IMC',('dire_actual','de_quien')),
        }),
        ('ANTECEDENTES PATOLOGICOS PERSONALES',{
            'fields':('cirugia_mamaria', 'otras_cirugias', 'antecedentes','atec_rt')
        }),
        ('ANTECEDENTES FAMILIARES',{
            'fields': (('ante_fam','candetalles'),'cancer_mama','cancer_ovario',
                       'cancer_prostata','cancer_colon', 'cancer_otro')
        }),
        ('ANTECEDENTES HORMONALES',{
            'fields': (('menarca','hijos','numero','edad_primero'),('amamanto','tiempo'),
                       ('anticonceptivos','tiempo_anti'))
        }),
        ('MENOPAUSIA', {
            'fields': (('menopausia', 'edad_meno', 'anos_repro'), ('trh', 'trh_opciones'))
        }),
        ('ABORTOS', {
            'fields': (('abortos','tipo_aborto'), ('primera_gesta', 'edad_gestacional'),'cuantos_abortos')
        }),

    )
    radio_fields = {'cirugia_mamaria':admin.HORIZONTAL,
                    'otras_cirugias':admin.HORIZONTAL,
                    'antecedentes':admin.HORIZONTAL,
                    'atec_rt':admin.HORIZONTAL,
                    'ante_fam':admin.HORIZONTAL,
                    'cancer_mama':admin.HORIZONTAL,
                    'cancer_ovario':admin.HORIZONTAL,
                    'cancer_prostata':admin.HORIZONTAL,
                    'cancer_colon':admin.HORIZONTAL,
                    'cancer_otro':admin.HORIZONTAL,
                    'menarca':admin.HORIZONTAL,
                    'hijos':admin.HORIZONTAL,
                    'amamanto':admin.HORIZONTAL,
                    'anticonceptivos':admin.HORIZONTAL,
                    'menopausia':admin.HORIZONTAL,
                    'trh':admin.HORIZONTAL,
                    'trh_opciones':admin.VERTICAL,
                    'abortos':admin.HORIZONTAL,
                    'tipo_aborto':admin.VERTICAL,
                    'primera_gesta':admin.HORIZONTAL,
                    }


# class PersonAdmin(admin.ModelAdmin):
#     form = PersonForm


admin.site.register(Persona, AdminRegistrado)
admin.site.register(Antecedentes,AdminAntecedentes)
# admin.site.register(Persona, PersonAdmin)
# admin.site.register(Encuesta)
admin.site.register(Mamografia,AdminMamo)

#admin.site.site_header = "FUNCA"
#admin.site.site_title = "Administracion del sitio"

