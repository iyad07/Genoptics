from flet import *

from pages.Home import Home
from pages.calculator import Calculator
from pages.Learn import Learn
from pages.questions import Questions
def views_handler(page):
  return {
    '/home':View(
      route='/home',
      controls=[
        Home(page)
      ]
    ),
    '/calculator':View(
      route='/calculator',
      controls=[
        Calculator(page)
      ]
    ),
    '/quest':View(
      route='/quest',
      controls=[
        Questions(page)
      ]
    ),
    '/learn':View(
      route='/learn',
      controls=[
        Learn(page)
      ]
    ),
  }