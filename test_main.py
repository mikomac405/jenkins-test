import main

class Tests:
  def test_add(self):
    assert 4 == main.add(2, 2)
    
  def test_sub(self):
    assert 2 == main.add(4, 2)
    
  def test_wrong_add(self):
    assert 10 == main.wrong_add(5, 5)
