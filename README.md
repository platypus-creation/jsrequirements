JS Requirements
===============

It's a best practice to only load JS files at the end of your HTML documents, as their loading stops everything else from loading on the page.

JS Requirements allows you to mark js files or scripts as required from your templates and your includes, and only have them loaded at the end of your document.

Installation
------------

    pip install git+git://github.com/platypus-creation/jsrequirements.git

or:

    git clone git://github.com/platypus-creation/jsrequirements.git
    cd jsrequirements
    python setup.py install
    
Usage
-----

In your templates add some required scripts:

    {% extends "base.html" %}
    {% load jsrequire %}
    
    {% block content %}
        {% for item in items %}
            <li>{{ item }}</li>
            {% jsrequire %}<script src="{{ STATIC_URL }}js/jsScript.js" type="text/javascript" charset="utf-8"></script>{% endjsrequire %}
            {% jsrequire %}
            <script type="text/javascript" charset="utf-8">
                // YOUR JS CODE HERE
                // ...
            </script>
            {% endjsrequire %}
        {% endfor %}
    {% endblock %}    

And in your base.html you add them at the end of your file.

    {% load jsrequire %}
    <html>
        <head>
            ...
        </head>
        <body>
            ...
            
            {% block content %}
            {% end block content %}
            
            ...
            
            {% jsrequirements %}
        </body>
    </html>


jsrequirements will automatically deduplicates requirements, only importing them once. Moreover as you can see on this example, if there are no elements in the items array, the jsrequire wont be added and unnecessary scripts wont be loaded.



Compatibility with Django-Compressor
------------------------------------

Out of the box jsrequirements works wonderfully with the great django-compressor, simply wrap your `{% jsrequirements %}` with the compress tag.

    {% compress js %}
        {% jsrequirements %}
    {% endcompress %}
