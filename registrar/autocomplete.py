from dal import autocomplete

from registrar.models import Persona

class PersonaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Persona.objects.none()

        qs = Persona.objects.all()

        if self.q:
            qs = qs.filter(cedula__istartswith=self.q)
        return qs
