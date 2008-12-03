# -*- coding: utf-8 -*-

"""
    unitest utils
    ~~~~~~~~~~~~~
    
"""

import sys
import unittest

from shared_tests import SharedTests

sys.path.insert(0, "../creole")

from creole import html2creole


class TestHtml2Creole(SharedTests):

    def assertCreole(self, source_string, should_string, debug=False):
        self.assert_html2Creole(source_string, should_string, debug)

    #--------------------------------------------------------------------------

#    def test_creole_basic(self):
#        out_string = creole2html("a text line.")
#        self.assertEqual(out_string, "<p>a text line.</p>\n")
#
#    def test_lineendings(self):
#        """ Test all existing lineending version """
#        out_string = creole2html(u"first\nsecond")
#        self.assertEqual(out_string, u"<p>first<br />\nsecond</p>\n")
#        
#        out_string = creole2html(u"first\rsecond")
#        self.assertEqual(out_string, u"<p>first<br />\nsecond</p>\n")
#        
#        out_string = creole2html(u"first\r\nsecond")
#        self.assertEqual(out_string, u"<p>first<br />\nsecond</p>\n")
        
    #--------------------------------------------------------------------------

#    def test_bold_italics(self):
#        self.assertCreole(r"""
#            **//bold italics//**
#            //**bold italics**//
#            //This is **also** good.//
#        """, """
#            <p><strong><i>bold italics</i></strong><br />
#            <i><strong>bold italics</strong></i><br />
#            <i>This is <strong>also</strong> good.</i></p>
#        """,
##            debug=True
#        )
#
#    def test_links(self):
#        self.assertCreole(r"""
#            test link: '[[internal links|link A]]' 1 and
#            test link: '[[http://domain.tld|link B]]' 2.
#        """, """
#            <p>test link: '<a href="internal links">link A</a>' 1 and<br />
#            test link: '<a href="http://domain.tld">link B</a>' 2.</p>
#        """)
#
#    def test_images(self):
#        self.assertCreole(r"""
#            a {{/image.jpg|JPG pictures}} and
#            a {{/image.jpeg|JPEG pictures}} and
#            a {{/image.gif|GIF pictures}} and
#            a {{/image.png|PNG pictures}} !
#            
#            picture [[www.domain.tld|{{foo.JPG|Foo}}]] as a link
#        """, """
#            <p>a <img src="/image.jpg" alt="JPG pictures"> and<br />
#            a <img src="/image.jpeg" alt="JPEG pictures"> and<br />
#            a <img src="/image.gif" alt="GIF pictures" /> and<br />
#            a <img src="/image.png" alt="PNG pictures" /> !</p>
#            
#            <p>picture <a href="www.domain.tld"><img src="foo.JPG" alt="Foo"></a> as a link</p>
#        """)
#
#    def test_nowiki1(self):
#        self.assertCreole(r"""
#            this:
#            {{{
#            //This// does **not** get [[formatted]]
#            }}}
#            and this: {{{** <i>this</i> ** }}} not, too.
#            
#            === Closing braces in nowiki:
#            {{{
#            if (x != NULL) {
#              for (i = 0; i < size; i++) {
#                if (x[i] > 0) {
#                  x[i]--;
#              }}}
#            }}}
#        """, """
#            <p>this:</p>
#            <pre>
#            //This// does **not** get [[formatted]]
#            </pre>
#            <p>and this: <tt>** &lt;i&gt;this&lt;/i&gt; ** </tt> not, too.</p>
#            
#            <h3>Closing braces in nowiki:</h3>
#            <pre>
#            if (x != NULL) {
#              for (i = 0; i &lt; size; i++) {
#                if (x[i] &gt; 0) {
#                  x[i]--;
#              }}}
#            </pre>
#        """)
#    

#        
#    def test_horizontal_rule(self):
#        self.assertCreole(r"""
#            one
#            ----
#            two
#        """, """
#            <p>one</p>
#            <hr />
#            <p>two</p>
#        """)
#
#    def test_list1(self):
#        """
#        FIXME: Two newlines between a list and the next paragraph :( 
#        """
#        self.assertCreole(r"""
#            ==== List a:
#            * a1 item
#            ** a1.1 Force\\linebreak
#            ** a1.2 item
#            *** a1.2.1 item
#            *** a1.2.2 item
#            * a2 item
#            
#            
#            list 'a' end
#            
#            ==== List b:
#            # b1 item
#            ## b1.2 item
#            ### b1.2.1 item
#            ### b1.2.2 Force\\linebreak1\\linebreak2
#            ## b1.3 item
#            # b2 item
#            
#            
#            list 'b' end
#        """, """
#            <h4>List a:</h4>
#            <ul>
#            <li>a1 item</li>
#            <ul>
#                <li>a1.1 Force
#                linebreak</li>
#                <li>a1.2 item</li>
#                <ul>
#                    <li>a1.2.1 item</li>
#                    <li>a1.2.2 item</li>
#                </ul>
#            </ul>
#            <li>a2 item</li>
#            </ul>
#            <p>list 'a' end</p>
#            
#            <h4>List b:</h4>
#            <ol>
#            <li>b1 item</li>
#            <ol>
#                <li>b1.2 item</li>
#                <ol>
#                    <li>b1.2.1 item</li>
#                    <li>b1.2.2 Force
#                    linebreak1
#                    linebreak2</li>
#                </ol>
#                <li>b1.3 item</li>
#            </ol>
#            <li>b2 item</li>
#            </ol>
#            <p>list 'b' end</p>
#        """,
##            debug=True
#        )
#
#    def test_list2(self):
#        """ Bold, Italics, Links, Pre in Lists """
#        self.assertCreole(r"""
#            * **bold** item
#            * //italic// item
#            
#            # item about a [[domain.tld|page link]]
#            # {{{ //this// is **not** [[processed]] }}}
#        """, """
#            <ul>
#                <li><strong>bold</strong> item</li>
#                <li><i>italic</i> item</li>
#            </ul>
#            <ol>
#                <li>item about a <a href="domain.tld">page link</a></li>
#                <li><tt>//this// is **not** [[processed]]</tt></li>
#            </ol>
#        """,
##            debug=True
#        )
#
#    #__________________________________________________________________________
#    # TODO:
#
#
#    def test_django(self):
#        self.assertCreole(r"""
#            The current page name: >{{ PAGE.name }}< great?
#            A {% lucidTag page_update_list count=10 %} PyLucid plugin
#            {% block %}
#            FooBar
#            {% endblock %}
#            A [[www.domain.tld|link]].
#            no image: {{ foo|bar }}!
#        """, """
#            <p>The current page name: &gt;{{ PAGE.name }}&lt; great?<br />
#            A {% lucidTag page_update_list count=10 %} PyLucid plugin</p>
#            {% block %}
#            FooBar
#            {% endblock %}
#            <p>A <a href="www.domain.tld">link</a>.<br />
#            no image: {{ foo|bar }}!</p>
#        """)
#
#    def test_escape_char(self):
#        self.assertCreole(r"""
#            ~#1
#            http://domain.tld/~bar/
#            ~http://domain.tld/
#            [[Link]]
#            ~[[Link]]
#        """, """
#            <p>#1<br />
#            <a href="http://domain.tld/~bar/">http://domain.tld/~bar/</a><br />
#            http://domain.tld/<br />
#            <a href="Link">Link</a><br />
#            [[Link]]</p>
#        """)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHtml2Creole)
    unittest.TextTestRunner().run(suite)