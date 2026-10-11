import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from new_skill import create
class DraftDiscoveryTests(unittest.TestCase):
 def test_path_recommendations_do_not_publish_a_draft(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=create('research-draft','新人物','材料互证',tmp,'research')
   c=json.loads((root/'series-catalog.json').read_text(encoding='utf-8'))
   self.assertEqual(c['skills'][-1]['status'],'planned')
   text=(root/'README.md').read_text(encoding='utf-8')
   self.assertIn('同类问题还可以用',text)
   self.assertIn('材料互证',text)
   self.assertNotIn('https://github.com/constantin2088/research-draft',text)
 def test_invalid_path_leaves_no_partial_draft(self):
  with tempfile.TemporaryDirectory() as tmp:
   with self.assertRaises(ValueError):create('new-draft','新人物','研究',tmp,'unknown')
   self.assertFalse((Path(tmp)/'new-draft').exists())
if __name__=='__main__':unittest.main()
