from unittest import TestCase
from x7.lib.annotations import tests
from x7.lib.inspect_more import item_name, item_lookup
from typing import Type, cast


@tests('x7.lib.inspect_more')
class TestModInspectMore(TestCase):
    """Tests for stand-alone functions in maketests.inspect_more module"""

    TEST_INSPECT_MORE_NAME = 'tests.x7.lib.test_inspect_more.TestModInspectMore'

    class SubclassForTesting(object):
        pass

    @tests(item_name)
    def test_callable_name(self):
        self.assertEqual('x7.lib.inspect_more.item_name', item_name(item_name))
        self.assertEqual(self.TEST_INSPECT_MORE_NAME + '.test_callable_name',
                         item_name(self.test_callable_name))
        for bad_thing in [Type, list()]:
            bad_thing = cast(callable, bad_thing)       # Just to make type checking happy
            with self.assertRaises(ValueError):
                item_name(bad_thing)

    @tests('x7.lib.inspect_more.item_name')
    def test_item_name(self):
        self.assertEqual(self.TEST_INSPECT_MORE_NAME, item_name(TestModInspectMore))
        subclass = self.TEST_INSPECT_MORE_NAME+'.SubclassForTesting'
        self.assertEqual(subclass, item_name(self.SubclassForTesting))
        self.assertEqual(subclass, item_name(TestModInspectMore.SubclassForTesting))

    @tests(item_lookup)
    def test_item_lookup(self):
        self.assertEqual(TestModInspectMore, item_lookup(self.TEST_INSPECT_MORE_NAME))
        self.assertEqual(TestModInspectMore.test_callable_name,
                         item_lookup(self.TEST_INSPECT_MORE_NAME+'.test_callable_name'))
        subclass = self.TEST_INSPECT_MORE_NAME+'.SubclassForTesting'
        self.assertEqual(self.SubclassForTesting, item_lookup(subclass))
        with self.assertRaises(FileNotFoundError):
            item_lookup('non_existent.anything')
        with self.assertRaises(FileNotFoundError):
            item_lookup('os.non_existent.anything')
