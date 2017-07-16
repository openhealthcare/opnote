"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from opnote import models

class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.OperationNote
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()
