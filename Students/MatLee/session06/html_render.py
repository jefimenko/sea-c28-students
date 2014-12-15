class Element(object):
    opening_tag = u'<>'
    closing_tag = u'</>'
    
    def __init__(self, text=u''):
        self.content = []
        if text:
            self.content.append(text)

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

