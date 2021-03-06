from django.contrib import admin

from cms.models import (
    Partner, Technology, Programme, ServiceOffered,
    Quote, Link, InsightsTag, Text
)


class TextInline(admin.TabularInline):
    model = Text
    extra = 0


class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 0


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0


class InsightsTagInline(admin.TabularInline):
    model = InsightsTag
    extra = 0


class PartnerAdmin(admin.ModelAdmin):

    # Methods
    # ==

    def has_delete_permission(self, request, obj=None):
        return False

    def delete_selected(self, request, queryset):
        queryset.update(published=False)

    def publish_selected(self, request, queryset):
        queryset.update(published=True)

    def shorter_description(self, obj):
        if len(obj.short_description) < 70:
            return obj.short_description
        else:
            return obj.short_description[0:64-1] + "[...]"

    def page_url(self, obj):
        if obj.dedicated_partner_page and obj.published:
            return '<a href="/{slug}">{slug}</a>'.format(slug=obj.slug)

    # Standalone functions
    # ==

    def technology(obj):
        return ",\n".join([str(o) for o in obj.technology.all()])

    def programme(obj):
        return ",\n".join([str(o) for o in obj.programme.all()])

    def service_offered(obj):
        return ",\n".join([str(o) for o in obj.service_offered.all()])

    actions = ['delete_selected', 'publish_selected']

    delete_selected.short_description = "Unpublish selected partners"
    publish_selected.short_description = "Publish selected partners"

    page_url.short_description = 'Page URL'
    page_url.allow_tags = True

    shorter_description.short_description = 'Short Description'

    technology.short_description = 'Technology'
    programme.short_description = 'Programme'
    service_offered.short_description = 'Service Offered'

    list_display = (
        'name',
        'page_url',
        'logo',
        'published',
        'shorter_description',
        'featured',
        'dedicated_partner_page',
        technology,
        programme,
        service_offered,
    )
    list_filter = (
        'published',
        'featured',
        'dedicated_partner_page',
        'technology',
        'programme',
        'service_offered',
    )
    list_editable = (
        'published',
    )
    search_fields = ['name']

    fieldsets = (
        ("Notes", {
            'classes': ('collapse',),
            'fields': ('notes',)
        }),
        ('Partner Information', {
            'fields': (
                'name',
                'featured',
                'short_description',
                'published',
                'logo',
                'partner_website',
                'fallback_website',
            )
        }),
        ('Categories', {
            'fields': (
                'technology',
                'programme',
                'service_offered',
            )
        }),
        ('Detailed partner Information', {
            'classes': ('collapse',),
            'fields': (
                'dedicated_partner_page',
                'long_description',
            )
        }),
    )
    inlines = [
        TextInline,
        QuoteInline,
        LinkInline,
        InsightsTagInline
    ]
    filter_horizontal = [
        'technology',
        'programme',
        'service_offered',
    ]
    change_form_template = 'admin/asterix_change_form.html'


class TechnologyAdmin(admin.ModelAdmin):
    pass


class ProgrammeAdmin(admin.ModelAdmin):
    pass


class ServiceOfferedAdmin(admin.ModelAdmin):
    pass


class MetadataAdmin(admin.ModelAdmin):
    pass


class QuoteAdmin(admin.ModelAdmin):
    pass


class LinkAdmin(admin.ModelAdmin):
    pass


class InsightsTagAdmin(admin.ModelAdmin):
    pass


class TextAdmin(admin.ModelAdmin):
    pass


admin.site.register(Partner, PartnerAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(ServiceOffered, ServiceOfferedAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(InsightsTag, InsightsTagAdmin)
admin.site.register(Text, TextAdmin)
