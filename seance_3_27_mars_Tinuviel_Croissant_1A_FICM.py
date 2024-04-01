## Class Tree

class Tree :
    def __init__(self,label,*children):
        self._label = label
        self._children = children

    def label(self):
        return str(self._label)

    def children(self):
        return tuple(self._children)

    def nb_children(self):
        return len(self._children)

    def child(self, i: int):
        """ the first subtree (i = 1) has for label the first children on the left"""
        if 1<= i <= self.nb_children():
            return self._children[i-1]

    def is_leaf(self):
        """ return True if the tree is a leaf"""
        return (self.nb_children() == 0)


    def depth(self):
        if self.is_leaf() :
            return 0
        else :
            maxDepth = 0
            for child in self._children:
                maxDepth = max(maxDepth, child.depth())
            return maxDepth + 1
            """we look for the maximum of children on each level, then when the entire level is visited, we move on to the next (so depth += 1)"""


    def __str__(self):
        if self.is_leaf():
            return self.label()
        else :
            """for each child of the tree we write child.label(child.children[0], child.children[1],...)"""
            chain = self.label() + "("
            count = 0
            for child in self._children:
                count += 1
                chain += child.__str__()
                if count != self.nb_children():
                    chain += ','
            chain += ")"
        return chain

    def __eq__(self,__value: object):
        return (self.__str__()) == (__value.__str__())


    def deriv(self,var: str):

        if self.is_leaf():

            # self is a leaf, so a variable 'X' or a constant
            if self.label() == var:
                self._label = Tree('1')
            else :
                self._label = Tree('0')
            return self

        else:
            if self.label() == '+':

                # for a polynomial tree, the children of '+' can be '*', 'X' or a constant
                for i in range(self.nb_children()):
                    self._children[i]._label = Tree(self._children[i].deriv(var)._label)
                return self

            if self.label() == '*':
                # for the derivative of X^k, we replace one of the subtree 'X' with the power k
                power = 0
                j = 0
                for i in range(self.nb_children()):
                    if (self._children[i]).label() == var:
                        power +=1
                        j = i
                if power > 1 :
                    self._children[j]._label = Tree(str(power))
                elif power == 1 :
                    self._children[j]._label = Tree('1')
                else:
                    # there is no variable, all the children are constants, so the derivative will be 0
                    self._children = (self.nb_children())*[Tree('0')]
                return self


T = Tree(3,Tree('a',Tree('d'),Tree('e')), Tree('b'),Tree('c'))
T1 = Tree(3,Tree('a',Tree('d'),Tree('e')), Tree('b'),Tree('c'))


p3 = (Tree('+', Tree('*', Tree(3), Tree('X'), Tree('X')), Tree('*', Tree(5), Tree('X')), Tree(7)))

""" T and T1 are equals but don't have the same identity"""

#print(T.children())
#print(T.child(1))
#print(T.__eq__(T1))
#print("P3 str:" + p3.__str__())
#print("P3 deriv:" + p3.deriv('X').__str__())

## exercice 2

## exerice 3
# depth use recurssion on subtrees

## exercice 4

# __str__ use same recurssion as depth
# __eq__ directly use the __str__ method as a signature of each tree

## exercice 5

## test

# -*- coding: utf-8 -*-

import unittest


"""class TestTree(unittest.TestCase):

    def test_create_tree1(self):
        a = Tree('a')
        a1 = Tree('a1', a)
        a2 = Tree('a1', a, a)
        self.assertIsNotNone(a)
        self.assertIsNot(a, a1)
        self.assertIsNot(a1, a2)

    def test_create_tree2(self):
        a = Tree('a')
        b = Tree('b')
        fab = Tree('f', a, b)
        ga = Tree('g', a)
        gb = Tree('g', b)

        self.assertEqual(a.label(), 'a')
        self.assertEqual(len(a.children()), 0)
        self.assertEqual(b.label(), 'b')
        self.assertEqual(len(b.children()), 0)

        self.assertEqual(fab.label(), 'f')
        self.assertEqual(fab.child(1), a)
        self.assertEqual(fab.child(2), b)

    def test_leaf(self):
        a = Tree('a')
        ga = Tree('g', a)

        self.assertTrue(a.is_leaf())
        self.assertFalse(ga.is_leaf())

    def test_depth(self):
        a = Tree('a')
        b = Tree('b')
        fab = Tree('f', a, b)
        ga = Tree('g', a)
        gb = Tree('g', b)
        fagb = Tree('f', a, gb)

        self.assertEqual(a.depth(), 0)
        self.assertEqual(fab.depth(), 1)
        self.assertEqual(ga.depth(), 1)
        self.assertEqual(gb.depth(), 1)
        self.assertEqual(fagb.depth(), 2)

    def test_eq_tree(self):
        a1 = Tree('a')
        a2 = Tree('a')
        fab1 = Tree('f', Tree('a'), Tree('b'))
        fab2 = Tree('f', Tree('a'), Tree('b'))

        self.assertEqual(a1, a2)
        self.assertEqual(fab1, fab2)

    def test_deriv_constant(self):
        X = Tree('X')
        a = Tree('a')
        zero = Tree('0')
        self.assertEqual(a.deriv(X), zero)
        self.assertEqual(zero.deriv(X), zero)

    def test_deriv_X(self):
        X = Tree('X')
        Y = Tree('Y')
        zero = Tree('0')
        un = Tree('1')

        self.assertEqual(X.deriv(X), un)
        self.assertEqual(Y.deriv(X), zero)

    def test_deriv_addition(self):
        X = Tree('X')
        zero = Tree('0')
        un = Tree('1')

        self.assertEqual(Tree('+', X, X).deriv(X), Tree('+', un, un))
        self.assertEqual(Tree('+', X, un).deriv(X), Tree('+', un, zero))

if __name__ == '__main__':
    unittest.main()"""

