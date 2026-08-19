import pytest from app import soma

def test_soma():
  assert soma(10, 10) == 20
