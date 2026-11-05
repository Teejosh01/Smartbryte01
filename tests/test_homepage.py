"""Dependency-free static-site checks: python3 -m unittest discover -s tests."""
from html.parser import HTMLParser
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.stack = []
    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
        if tag not in {'meta', 'link', 'img', 'br', 'hr', 'input', 'source'}:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            raise AssertionError(f'Unbalanced tag: {tag}; stack: {self.stack}')
        self.stack.pop()

class HomepageTests(unittest.TestCase):
    def setUp(self):
        self.html = (ROOT / 'index.html').read_text()
        self.doc = Document()
        self.doc.feed(self.html)
    def test_balanced_html(self):
        self.assertEqual(self.doc.stack, [])
    def test_landmarks(self):
        for tag in ('h1', 'main', 'header', 'footer'):
            self.assertEqual(sum(t == tag for t, _ in self.doc.elements), 1)
    def test_destinations_and_assets(self):
        ids = [a['id'] for _, a in self.doc.elements if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)))
        for tag, attrs in self.doc.elements:
            for ref in attrs.get('aria-labelledby', '').split():
                self.assertIn(ref, ids)
            url = attrs.get('src') or attrs.get('href', '')
            if url.startswith('#'):
                self.assertIn(url[1:], ids)
            elif url and not url.startswith(('https:', 'data:')):
                self.assertTrue((ROOT / url).is_file(), url)
            if tag == 'img':
                self.assertIn('alt', attrs)
    def test_no_runtime_or_dead_buttons(self):
        self.assertFalse(any(t in ('script', 'button') for t, _ in self.doc.elements))
        self.assertNotIn('opacity: 0', (ROOT / 'assets/styles.css').read_text())
        self.assertNotIn('fonts.googleapis.com', self.html)
    def test_faq_and_programmes(self):
        self.assertEqual(sum(t == 'details' for t, _ in self.doc.elements), 9)
        self.assertEqual(sum(t == 'article' and 'prog-card' in a.get('class', '') for t, a in self.doc.elements), 3)
    def test_vercel_config(self):
        config = json.loads((ROOT / 'vercel.json').read_text())
        self.assertEqual(config['outputDirectory'], '.')
    def test_sample_disclosure(self):
        self.assertIn('not verified reviews', self.html)

if __name__ == '__main__':
    unittest.main()
