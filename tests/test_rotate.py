import os
import subprocess
import sys
import unittest
import time
import tempfile
import pdfarranger.core as core
import pikepdf

class PTest(unittest.TestCase):

    @staticmethod
    def _lpage1() -> core.LayerPage:
        return core.LayerPage(2, 4, 'lcopy', 90, 2, core.Sides(0.11, 0.21, 0.31, 0.41),
                              core.Sides(0.12, 0.22, 0.32, 0.42), 'OVERLAY', core.Dims(10.33, 20.33))

    @staticmethod
    def _lpage1_180() -> core.LayerPage:
        return core.LayerPage(2, 4, 'lcopy', 270, 2, core.Sides(0.21, 0.11, 0.41, 0.31),
                              core.Sides(0.22, 0.12, 0.42, 0.32), 'OVERLAY', core.Dims(10.33, 20.33))

    def _page1(self) -> core.Page:
        """Sample page 1"""
        return core.Page(1, 2, 0.55, 'copy', 0, 2, core.Sides(0.1, 0.2, 0.3, 0.4),
                         core.Sides(0.11, 0.21, 0.31, 0.41), core.Dims(100.33, 200.66), 'base', [self._lpage1()])

    def _page1_180(self) -> core.Page:
        """Sample page 1 rotated 180 degrees"""
        return core.Page(1, 2, 0.55, 'copy', 180, 2, core.Sides(0.2, 0.1, 0.4, 0.3),
                         core.Sides(0.21, 0.11, 0.41, 0.31), core.Dims(100.33, 200.66), 'base', [self._lpage1_180()])

   
class RotationTest(PTest):

    def _rotate_p1(self, angle: int) -> core.LayerPage:
        p = self._lpage1()
        p.rotate(angle)
        return p
    
    def _rotate_p2(self, angle: int) -> core.Page:
        lp = self._page1()
        lp.rotate(angle)
        return lp

    # Teste de rotação de 180 graus para LayerPage
    def test_lrotate_180_p1(self):
        self.assertEqual(repr(self._rotate_p1(2)), repr(self._lpage1_180()))

    # Teste de rotação de -180 graus para LayerPage
    def test_lrotate_180_p2(self):
        self.assertEqual(repr(self._rotate_p1(-2)), repr(self._lpage1_180()))

    # Teste de rotação de 0 graus para LayerPage
    def test_lrotate_180_p3(self):
        self.assertEqual(repr(self._rotate_p1(0)), repr(self._lpage1()))

    # Teste de rotação de 180 graus para Page
    def test_rotate_180_p1(self):
        self.assertEqual(repr(self._rotate_p2(180)), repr(self._page1_180()))

    # Teste de rotação de -180 graus para Page
    def test_rotate_180_p2(self):
        self.assertEqual(repr(self._rotate_p2(-180)), repr(self._page1_180()))

    # Teste de rotação de 0 graus para Page
    def test_rotate_180_p3(self):
        self.assertEqual(repr(self._rotate_p2(0)), repr(self._page1()))



