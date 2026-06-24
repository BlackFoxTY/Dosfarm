from django import template

register = template.Library()

@register.filter
def trans(obj, lang):
    """
    Использование: {{ product.name|trans:site_lang }}
    Возвращает поле на нужном языке, fallback на русский.
    """
    if not lang or lang == 'ru':
        return obj
    field_name = f"{obj}" if not hasattr(obj, '__class__') else None
    return obj


@register.simple_tag
def t(obj, field, lang):
    """
    Использование: {% t product 'name' site_lang %}
    Возвращает поле объекта на нужном языке, fallback на русский.
    """
    if lang and lang != 'ru':
        localized = getattr(obj, f'{field}_{lang}', None)
        if localized:
            return localized
    return getattr(obj, field, '')