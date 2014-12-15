class Element(object):
    opening_tag = u''
    closing_tag = u''
    
    def __init__(self):
        self.content = []

    def render(self, file_out, ind=u''):
        display = []
        for item in self.content:
            if isinstance(item, Element):
                display += item.render(item, file_out, ind+=ind).split('\n')
            else:
                display.append(ind + item)

        all_out = [self.opening_tag] + display + [self.closing_tag]
        print u'\n'.join(all_out)
        return display

    def append(self, item):
        self.content.append(item)


class Html(Element):
    opening_tag = u'<html>'
    closing_tag = u'</html>'


class Body(Element):
    opening_tag = u'<body>'
    closing_tag = u'</body>'


class P(Element):
    opening_tag = u'<p>'
    closing_tag = u'</p>'