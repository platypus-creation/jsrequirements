from jsrequirements.settings import VARNAME

def jsrequirements(request=None):
    """
    Simple context processor which makes sure that the Set is
    available in all templates.
    """
    return {VARNAME: []}