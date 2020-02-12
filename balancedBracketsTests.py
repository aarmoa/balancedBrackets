from balancedBrackets import areBracketsBalanced
import unittest

class BalancedBracketsTest(unittest.TestCase):

    def test_simpleBalancedSingleString(self):
        self.assertTrue(areBracketsBalanced('1', ['()']) == ['YES'])
        self.assertTrue(areBracketsBalanced('1', ['[]']) == ['YES'])
        self.assertTrue(areBracketsBalanced('1', ['{}']) == ['YES'])

    def test_stringWithOnlyOpeningBracketIsNotBalanced(self):
        self.assertTrue(areBracketsBalanced('3', ['(', '[', '{']) == ['NO', 'NO', 'NO'])

    def test_mixedCases(self):
        self.assertTrue(areBracketsBalanced('3', ['{[()]}', '{[(])}', '{{[[(())]]}}']) == ['YES', 'NO', 'YES'])

if __name__ == '__main__':
    unittest.main()