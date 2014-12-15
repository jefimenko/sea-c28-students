class Element(object):
    opening_tag = u'<>'
    closing_tag = u'</>'
    
    def __init__(self, text=u'', **kwargs):
        self.content = []
        if text:
            self.content.append(text)
        if kwargs:
            print kwargs
            self.opening_tag = self.opening_tag[:-1]
            for key, value in kwargs.iteritems():
                self.opening_tag += u' {style}={options}'.format(style=key, options=value)
            self.opening_tag += u'>'


    def render(self, file_out, ind=u'', depth=1):
        display = []
        file_out.write( u'\n' + ind*(depth-1) + self.opening_tag )
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, ind, depth+1)
            else:
                file_out.write( u'\n' + ind*depth+item )

        file_out.write( u'\n' + ind*(depth-1) + self.closing_tag )
        
        #if depth is 1:
        #    file_out.write(u'\n'.join(display))

        #return display


    def append(self, item):
        self.content.append(item)
        #print self.content


class Html(Element):
    opening_tag = u'<html>'
    closing_tag = u'</html>'


class Body(Element):
    opening_tag = u'<body>'
    closing_tag = u'</body>'


class P(Element):
    opening_tag = u'<p>'
    closing_tag = u'</p>'


class Head(Element):
    opening_tag = u'<head>'
    closing_tag = u'</head>'

    
class OneLineTag(Element):
    
    # Print an element in a single line,
    # even if element contains more than one string.
    def render(self, file_out, ind=u'', depth=1):
        file_out.write( u'\n' + ind*(depth-1) + self.opening_tag )
        for item in self.content:
            file_out.write(item)
        file_out.write( self.closing_tag )


class Title(OneLineTag):
    opening_tag = u'<title>'
    closing_tag = u'</title>'