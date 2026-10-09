import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from new_skill import create,validate_slug
from check_skill import check

class ScaffoldTests(unittest.TestCase):
    def test_reject_bad_slug(self):
        with self.assertRaises(ValueError):
            validate_slug('../x')
    def test_generate(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=create('chen-yinke-research-skill','陈寅恪','深度研究',tmp)
            self.assertTrue((p/'SKILL.md').exists())
            self.assertEqual(check(p),[])
    def test_release_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=create('test-thinker','测试人物','研究',tmp)
            self.assertTrue(check(p,release=True))
    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            create('test-thinker','测试人物','研究',tmp)
            with self.assertRaises(FileExistsError):
                create('test-thinker','测试人物','研究',tmp)

if __name__=='__main__':
    unittest.main()
