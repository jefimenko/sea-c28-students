class Element(object):
    opening_tag = (u'<', u'', u'>')
    closing_tag = (u'</', u'', u'>')
    ind = u'    '

    # Construct an html element.
    # Keyword arguments are interpreted and rendered as
    # [key]="values" for each argument given.
    def __init__(self, text=u'', tag=u'', **kwargs):
        self.opening_tag = list(self.opening_tag)
        self.closing_tag = list(self.closing_tag)
        self.content = []
        if text:
            self.content.append(text)
        

        if kwargs:
            self_closing = not bool(self.closing_tag)
            if self_closing:
                self.opening_tag.insert(2, kwargs)
        self.opening_tag[1] = tag
        self.closing_tag[1] = tag

            # if self_closing:
                # self.opening_tag = self.opening_tag[:-3]
            # else:
                # self.opening_tag = self.opening_tag[:-1]
            # for key, value in kwargs.iteritems():
                # self.opening_tag += u' {style}="{options}"'.format(
                    # style=key,
                    # options=value)
            # if self_closing:
                # self.opening_tag += u' />'
            # else:
                # self.opening_tag += u'>'

    # Render information in html element in a nicely formatted way.
    # Indentation is determined by keyword argument 'ind', while new_line
    # allows an element to be rendered in one line if given an empty string.
    def render(self, file_out, depth=1, display=[]):
        display.append(self.ind * (depth - 1) + u''.join(self.opening_tag))

        for item in self.content:
            try:
                item.render(file_out, depth + 1)
            except AttributeError:
                display.append(self.ind * depth + item)
        display.append(self.ind * (depth - 1) + u''.join(self.closing_tag))

        if depth == 1:
            file_out.write(u'\n'.join(display))

        # file_out.write( new_line + ind + self.opening_tag )
        # for item in self.content:
            # if isinstance(item, Element):
                # item.render(file_out, ind, depth+1)
            # else:
                # file_out.write( new_line + ind*depth+item )

        # file_out.write( new_line + ind*(depth-1) + self.closing_tag )

    def append(self, item):
        self.content.append(item)


class Html(Element):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'html', **kwargs)

    def render(self, file_out):
        file_out.write(u'<!DOCTYPE html>\n')
        Element.render(self, file_out)


class Body(Element):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'body', **kwargs)

class P(Element):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'p', **kwargs)

class Head(Element):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'head', **kwargs)

class Ul(Element):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'ul', **kwargs)

class Li(Element):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'li', **kwargs)


class OneLineTag(Element):

    # Render an element in a single line,
    # even if element contains more than one string.
    # Assumes there are no tags in content.
    def render(self, file_out, ind=u'', depth=1):
        file_out.write(u'\n' + ind*(depth-1))
        Element.render(self, file_out, ind=u'', depth=1, new_line=u'')

class Title(OneLineTag):
    # opening_tag[1] = u'title'
    # closing_tag[1] = u'title'
    pass

class A(OneLineTag):
    # opening_tag[1] = u'a'
    # closing_tag[1] = u'a'

    def __init__(self, link, content):
        Element.__init__(self, text=content, href=link)

class H(OneLineTag):
    # opening_tag[1] = u'<h'
    # closing_tag[1] = u'</h'

    # def __init__(self, size, content):
        # Element.__init__(self, content)
        # self.opening_tag += str(size)+u'>'
        # self.closing_tag += str(size)+u'>'
    pass


class SelfClosingTag(Element):
    closing_tag = None

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'html', **kwargs)

    def render(self, file_out, ind=u'', depth=1):
        file_out.write( u'\n' + ind*(depth-1) + self.opening_tag )
        for item in self.content:
            file_out.write(item)

class Hr(SelfClosingTag):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'html', **kwargs)

class Br(SelfClosingTag):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'html', **kwargs)

class Meta(SelfClosingTag):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'html', **kwargs)
