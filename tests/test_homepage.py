"""Run: python3 -m unittest discover -s tests. No dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.elements=[]; self.stack=[]
    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
        if tag not in {'meta','link','img','hr','br','input','source'}: self.stack.append(tag)
    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, (tag, self.stack)
        self.stack.pop()
class HomepageTests(unittest.TestCase):
    def setUp(self):
        self.html=(ROOT/'index.html').read_text()
        self.page=Page(); self.page.feed(self.html)
    def test_structure(self):
        self.assertEqual(self.page.stack, [])
        for tag in ('h1','main','header','footer'):
            self.assertEqual(sum(t==tag for t,a in self.page.elements),1)
    def test_links_and_assets(self):
        ids=[a['id'] for t,a in self.page.elements if 'id' in a]
        self.assertEqual(len(ids),len(set(ids)))
        for tag,a in self.page.elements:
            for ref in a.get('aria-labelledby','').split(): self.assertIn(ref,ids)
            for key in ('href','src'):
                ref=a.get(key,'')
                if ref.startswith('#'): self.assertIn(ref[1:],ids)
                elif ref and not ref.startswith(('https:','data:')): self.assertTrue((ROOT/ref).is_file(),ref)
            if tag=='img': self.assertIn('alt',a)
    def test_retained_content(self):
        for tag,count in [('details',9),('img',6),('section',8)]:
            self.assertEqual(sum(t==tag for t,a in self.page.elements),count)
        self.assertIn('not verified reviews',self.html)
    def test_no_dead_buttons_or_hidden_content(self):
        self.assertFalse(any(t=='button' for t,a in self.page.elements))
        self.assertNotIn('opacity: 0', (ROOT/'assets/styles.css').read_text())
        self.assertNotIn('IntersectionObserver',(ROOT/'assets/script.js').read_text())
    def test_colour_and_accessibility_retained(self):
        css=(ROOT/'assets/styles.css').read_text()
        for token in ('#FFC224','#4255FF','#FFF8ED','prefers-reduced-motion',':focus-visible'):
            self.assertIn(token,css)
if __name__=='__main__': unittest.main()
