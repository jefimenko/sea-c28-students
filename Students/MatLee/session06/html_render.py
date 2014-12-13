class Element(list):
    opening_tag = u'<>'
    closing_tag = u'</>'

    def render(self, file_out, ind=u''):
        content = [ind + item for item in self]

        all_out = [self.opening_tag] + content + [self.closing_tag]
        print u'\n'.join(all_out)


class Body(Element):
    opening_tag = u'<body>'
    closing_tag = u'</body>'


class P(Element):
    opening_tag = u'<p>'
    closing_tag = u'</p>'