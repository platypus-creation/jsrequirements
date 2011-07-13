from django.template import Template
from django.template import Library, Variable, Node
from jsrequirements.settings import VARNAME
register = Library()

@register.tag
def jsrequire(parser, token):
    """Add js requirements, except if they were alredy added."""
    nodelist = parser.parse(('endjsrequire',))
    parser.delete_first_token()
    return JSRequireNode(nodelist)

class JSRequireNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        storage = Variable(VARNAME).resolve(context)
        rendered_nodes = self.nodelist.render(context)
        # Deduplicate
        if not rendered_nodes in storage:
            storage.append(rendered_nodes)
        # This tag doesn't render anything
        return ''


@register.tag
def jsrequirements(parser, token):
    """Returns the js requirements that have been added through require."""
    return JSRequirementsNode()

class JSRequirementsNode(Node):
    def render(self, context):
        return '\n'.join(Variable(VARNAME).resolve(context))
