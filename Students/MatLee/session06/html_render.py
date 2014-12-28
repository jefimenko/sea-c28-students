class Element(object):
    # opening_tag = (u'<', u'>')
    # closing_tag = (u'<', u'/>')
    opening_tag = u'<>'
    closing_tag = u'</>'

    # Construct an html element.
    # Keyword arguments are interpreted and rendered as
    # [key]="values" for each argument given.
    def __init__(self, text=u'', **kwargs):
        self.content = []
        if text:
            self.content.append(text)

        if kwargs:
            self_closing = not bool(self.closing_tag)
            # if self_closing:
                

            if self_closing:
                self.opening_tag = self.opening_tag[:-3]
            else:
                self.opening_tag = self.opening_tag[:-1]
            for key, value in kwargs.iteritems():
                self.opening_tag += u' {style}="{options}"'.format(
                    style=key,
                    options=value)
            if self_closing:
                self.opening_tag += u' />'
            else:
                self.opening_tag += u'>'

    # Render information in html element in a nicely formatted way.
    # Indentation is determined by keyword argument 'ind', while new_line
    # allows an element to be rendered in one line if given an empty string.
    def render(self, file_out, ind=u'    ', depth=1, new_line=u'\n'):
        display = []
        file_out.write( new_line + ind*(depth-1) + self.opening_tag )
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, ind, depth+1)
            else:
                file_out.write( new_line + ind*depth+item )

        file_out.write( new_line + ind*(depth-1) + self.closing_tag )

    def append(self, item):
        self.content.append(item)


class Html(Element):
    opening_tag = u'<html>'
    closing_tag = u'</html>'

    def render(self, file_out, ind=u'', depth=1):
        file_out.write(u'<!DOCTYPE html>')
        Element.render(self, file_out, ind, depth)


class Body(Element):
    opening_tag = u'<body>'
    closing_tag = u'</body>'

class P(Element):
    opening_tag = u'<p>'
    closing_tag = u'</p>'

class Head(Element):
    opening_tag = u'<head>'
    closing_tag = u'</head>'

class Ul(Element):
    opening_tag = u'<ul>'
    closing_tag = u'</ul>'

class Li(Element):
    opening_tag = u'<li>'
    closing_tag = u'</li>'


class OneLineTag(Element):

    # Render an element in a single line,
    # even if element contains more than one string.
    # Assumes there are no tags in content.
    def render(self, file_out, ind=u'', depth=1):
        file_out.write(u'\n' + ind*(depth-1))
        Element.render(self, file_out, ind=u'', depth=1, new_line=u'')

class Title(OneLineTag):
    opening_tag = u'<title>'
    closing_tag = u'</title>'

class A(OneLineTag):
    opening_tag = u'<a>'
    closing_tag = u'</a>'

    def __init__(self, link, content):
        Element.__init__(self, text=content, href=link)

class H(OneLineTag):
    opening_tag = u'<h'
    closing_tag = u'</h'

    def __init__(self, size, content):
        Element.__init__(self, content)
        self.opening_tag += str(size)+u'>'
        self.closing_tag += str(size)+u'>'


class SelfClosingTag(Element):
    opening_tag = u'< />'
    closing_tag = None

    def render(self, file_out, ind=u'', depth=1):
        file_out.write( u'\n' + ind*(depth-1) + self.opening_tag )
        for item in self.content:
            file_out.write(item)

class Hr(SelfClosingTag):
    opening_tag = u'<hr />'

class Br(SelfClosingTag):
    opening_tag = u'<br />'

class Meta(SelfClosingTag):
    opening_tag = u'<meta />'
