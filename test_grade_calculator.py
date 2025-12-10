#!/usr/bin/env python3
"""
Unit tests for the Student Grade Calculator
Demonstrates testing fundamental programming concepts
"""

import unittest
from student_grade_calculator import calculate_average, get_letter_grade


class TestGradeCalculator(unittest.TestCase):
    """Test cases for grade calculator functions."""
    
    def test_calculate_average_normal(self):
        """Test average calculation with normal input."""
        grades = [85, 90, 88, 92, 87]
        expected = 88.4
        self.assertAlmostEqual(calculate_average(grades), expected, places=2)
    
    def test_calculate_average_empty(self):
        """Test average calculation with empty list."""
        grades = []
        expected = 0
        self.assertEqual(calculate_average(grades), expected)
    
    def test_calculate_average_single(self):
        """Test average calculation with single grade."""
        grades = [100]
        expected = 100
        self.assertEqual(calculate_average(grades), expected)
    
    def test_letter_grade_a(self):
        """Test letter grade A assignment."""
        self.assertEqual(get_letter_grade(95), 'A')
        self.assertEqual(get_letter_grade(90), 'A')
    
    def test_letter_grade_b(self):
        """Test letter grade B assignment."""
        self.assertEqual(get_letter_grade(85), 'B')
        self.assertEqual(get_letter_grade(80), 'B')
    
    def test_letter_grade_c(self):
        """Test letter grade C assignment."""
        self.assertEqual(get_letter_grade(75), 'C')
        self.assertEqual(get_letter_grade(70), 'C')
    
    def test_letter_grade_d(self):
        """Test letter grade D assignment."""
        self.assertEqual(get_letter_grade(65), 'D')
        self.assertEqual(get_letter_grade(60), 'D')
    
    def test_letter_grade_f(self):
        """Test letter grade F assignment."""
        self.assertEqual(get_letter_grade(55), 'F')
        self.assertEqual(get_letter_grade(0), 'F')
    
    def test_boundary_values(self):
        """Test boundary values between letter grades."""
        self.assertEqual(get_letter_grade(89.9), 'B')
        self.assertEqual(get_letter_grade(79.9), 'C')
        self.assertEqual(get_letter_grade(69.9), 'D')
        self.assertEqual(get_letter_grade(59.9), 'F')


if __name__ == '__main__':
    unittest.main()
