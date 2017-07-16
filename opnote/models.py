"""
opnote models.
"""
from django.db.models import fields, Model, ForeignKey, ManyToManyField

from opal import models
from opal.core.lookuplists import LookupList

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""

class CancerType(LookupList):
    pass

class AnaestheticType(LookupList):
    pass

class AsaType(LookupList):
    pass

class Urgency(LookupList):
    pass

class StaffMember(LookupList):
    pass
    
class OperationNote(models.EpisodeSubrecord):

    start_time = fields.TimeField()
    end_time = fields.TimeField()
    date = fields.DateField()

    lead_surgeon = models.ForeignKeyOrFreeText(StaffMember, related_name = "%(class)s_lead_surgeon")
    lead_anaesthetist = models.ForeignKeyOrFreeText(StaffMember, related_name = "%(class)s_lead_anaesthetist")

    surgeon = ManyToManyField(StaffMember, related_name = "%(class)s_surgeon")
    assistant = ManyToManyField(StaffMember, related_name = "%(class)s_assistant")
    anaesthetist = ManyToManyField(StaffMember, related_name = "%(class)s_anaesthetist")

    dvt_heparin = fields.BooleanField()
    dvt_ted_stockings = fields.BooleanField()
    dvt_pnematic = fields.BooleanField()
    dvt_aspirin = fields.BooleanField()

    antibiotics = fields.CharField(max_length = 40)
    indication = fields.CharField(max_length = 20)
    position = fields.CharField(max_length = 20)
    incision = fields.CharField(max_length = 20)
    findings = fields.TextField()
    procedure = fields.TextField()

    anaesthetic = models.ForeignKeyOrFreeText(AnaestheticType)
    cancer = models.ForeignKeyOrFreeText(CancerType)
    asa = models.ForeignKeyOrFreeText(AsaType)
    urgency = models.ForeignKeyOrFreeText(Urgency)
