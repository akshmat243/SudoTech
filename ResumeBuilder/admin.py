from django.contrib import admin
from .models import Resume, PersonalInfo, Experience, Education, Skill, ContactInfo

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1  # Number of empty forms to display

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class ContactInfoInline(admin.StackedInline):
    model = ContactInfo
    extra = 1

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at', 'user')
    inlines = [ExperienceInline, EducationInline, SkillInline, ContactInfoInline]

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('resume', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('resume',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('resume', 'company_name', 'position', 'start_date', 'end_date')
    search_fields = ('company_name', 'position')
    list_filter = ('resume',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('resume', 'institution_name', 'degree', 'start_date', 'end_date')
    search_fields = ('institution_name', 'degree')
    list_filter = ('resume',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('resume', 'name', 'proficiency')
    search_fields = ('name',)
    list_filter = ('resume',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('resume', 'linked_in', 'github', 'portfolio')
    search_fields = ('linked_in', 'github', 'portfolio')
    list_filter = ('resume',)
