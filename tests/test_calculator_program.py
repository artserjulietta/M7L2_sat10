import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_calculate_subtraction():
    assert calculate(9, 5, '-') == 4

def test_calculate_multiply():
    assert calculate(-2, 5, '*') == -10

def test_calculate_division_zero():
    assert calculate(8, 0, '/') == 'Ошибка: Деление на ноль.'

'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо добавить тесты для следующих операций:
1. Вычитание
2. Умножение
'''
