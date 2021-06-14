from .main import calculator

class Tests:
  def test_add(self):
    assert 4 == calculator.add(2, 2)
    
  def test_sub(self):
    assert 2 == calculator.add(4, 2)
    
  def test_wrong_add(self):
    assert 10 == calculator.wrong_add(5, 5)
