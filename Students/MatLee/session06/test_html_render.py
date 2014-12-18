#!/usr/bin/env python

import html_render as hr
import cStringIO


# Tests for element place-holder tags to be used by subclasses
def test_E_tags():
    f = cStringIO.StringIO()

    e = hr.Element()
    e.render(f)

    f.reset()
    assert f.read() == open(u'html_e_tag_test.html', 'r').read()
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
    assert f.read() == open('html_e_ind_test.html', 'r').read()
    f.close()


def test_HTML_tags():
    f = cStringIO.StringIO()

    page = hr.Html(u'Constructed.')
    page.append(u'Appended.')
    page.append(hr.Element(u'Nested.'))
    
    page.render(f, u'    ')
    
    f.reset()
    assert f.read() == open(u'HTML_tags_test.html').read()
    f.close()
# Body
# P
 # attributes
# Head
# Ul
# Li

# One liner
# Title
# H
 # sizes
# Anchor
 # attributes

# Self closing
# Hr
# Br Meta
 # attributes