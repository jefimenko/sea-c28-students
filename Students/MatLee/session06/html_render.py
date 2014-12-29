class Element(object):
    opening_tag = (u'<', u'', u'>')
    closing_tag = (u'</', u'', u'>')
    ind = u'    '

    # Construct an html element.
    # Keyword arguments are interpreted and rendered as
    # key="values" for each argument given.
    def __init__(self, text=u'', tag=u'', **kwargs):
        self.self_closing = not bool(self.closing_tag)
        self.opening_tag = list(self.opening_tag)
        if not self.self_closing:
            self.closing_tag = list(self.closing_tag)
        self.content = []
        if text:
            self.content.append(text)

        if kwargs:
            for key, value in kwargs.items():
                self.opening_tag.insert(-1, u' {0}="{1}"'.format(key, value))

        self.opening_tag[1] = tag
        if self.self_closing:
            self.opening_tag[-1] = u' />'
        if not self.self_closing:
            self.closing_tag[1] = tag


    # Render information in html element in a nicely formatted way.
    # Indentation is determined by global symbol 'ind'.
    def render(self, file_out):
        file_out.write(u'\n'.join(self.content_former()))

    # Return a list containing content with appropriate indentation.
    def content_former(self, depth=1):
        display = []
        display.append(self.ind * (depth - 1) + u''.join(self.opening_tag))
        for item in self.content:
            # Grow the list by appending individual items of content.
            # If an item is an element, that item's content will be fetched and
            # used to grow the display list before this current loop continues
            # to another item.
            try:
                current = item.content_former(depth)
                for inner in current:
                    try:
                        inner.content_former(depth+1)
                    except AttributeError:
                        display.append(self.ind * depth + inner)
                    
            except AttributeError:
                display.append(self.ind * depth + item)

        if not self.self_closing:
            display.append(self.ind * (depth - 1) + u''.join(self.closing_tag))
        return display

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
    def content_former(self, depth=1):
        one_liner = Element.content_former(self, depth)
        for place, item in enumerate(one_liner[1:]):
            one_liner[place + 1] = item.strip()
        display = [u''.join(one_liner)]
        return display

class Title(OneLineTag):

    def __init__(self, content):
        Element.__init__(self, text=content, tag=u'title')

class A(OneLineTag):

    def __init__(self, link, content):
        Element.__init__(self, text=content, tag=u'a', href=link)

class H(OneLineTag):

    def __init__(self, size, content):
        Element.__init__(self, content, tag=u'h'+str(size))



class SelfClosingTag(Element):
    closing_tag = None

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'', **kwargs)

class Hr(SelfClosingTag):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'hr', **kwargs)

class Br(SelfClosingTag):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'br', **kwargs)

class Meta(SelfClosingTag):

    def __init__(self, text=u'', **kwargs):
        Element.__init__(self, text, tag=u'meta', **kwargs)
