#!/usr/bin/env python

import html_render as hr
import cStringIO


# Tests for element place-holder tags to be used by subclasses
def test_E_tags():
    f = cStringIO.StringIO()

    e = hr.Element()
    e.render(f)

    f.reset()
    assert f.read() == open(u'html_E_tag_test.html', 'r').read()
    f.close()

# Test for element content being rendered with correct indentations,
# given at creation of object, or appended later
def test_E_content():
    f = cStringIO.StringIO()

    e = hr.Element(u'Some text.')
    e.append(u'Appended text.')
    e.append(hr.Element(u'Nested element.'))

    e.render(f, u'    ')

    f.reset()
    assert f.read() == open('html_E_ind_test.html', 'r').read()
    f.close()


def test_HTML_tags():
    f = cStringIO.StringIO()

    page = hr.Html(u'Constructed.')
    page.append(u'Appended.')
    page.append(hr.Element(u'Nested.'))

    page.render(f, u'    ')

    f.reset()
    assert f.read() == open(u'HTML_tags_test.html', 'r').read()
    f.close()

# Test for proper overwrite of tag values for subclasses
def test_content_tags():
    f = cStringIO.StringIO()

    page = hr.Html()
    head = hr.Head(u'The Head.')
    body = hr.Body()
    body.append(u'First.')
    body.append(hr.P(u'A paragraph.'))
    ul = hr.Ul(hr.Li())
    body.append(ul)

    page.append(head)
    page.append(body)

    page.render(f, u'    ')

    f.reset()
    assert f.read() == open(u'content_tags_test.html', 'r').read()
    f.close()


def test_E_attributes():
    f = cStringIO.StringIO()

    e = hr.Element(u'Nothing.', attrib=u"some descriptions", another=u"moAR thingz")
    e.append(hr.A(u'a link', u'Content.'))
    e.append(hr.P(u'Text.', style=u"i don't even know; among other things"))
    e.render(f, u'    ')

    f.reset()
    assert f.read() == open(u'html_E_tag_attributes_test.html', 'r').read()
    f.close()


def test_one_liners():
    f = cStringIO.StringIO()

    page = hr.Html()
    head = hr.Head(hr.Title(u'The Title.'))
    body = hr.Body()
    
    for size in range(1, 7):
        body.append(hr.H(size, u'Size {0}'.format(size)))

    body.append(hr.A(u'link', u'content'))

    page.append(head)
    page.append(body)

    page.render(f, u'    ')

    f.reset()
    assert f.read() == open(u'one_liners_test.html', 'r').read()
    f.close()


def test_self_closing():
    f = cStringIO.StringIO()

    page = hr.Html()
    body = hr.Body()
    body.append(hr.Meta(options=u"things"))
    body.append(hr.Br())
    body.append(hr.Hr())
    
    page.append(body)

    page.render(f, u'    ')

    f.reset()
    assert f.read() == open(u'self_closing_test.html', 'r').read()
    f.close()

    

