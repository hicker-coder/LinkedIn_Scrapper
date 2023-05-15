from dataclasses import dataclass
from time import sleep
from . import constants as c
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@dataclass
class Contact:
    pass


@dataclass
class Institution:
    pass


@dataclass
class Experience(Institution):
    pass

@dataclass
class Education(Institution):
    pass


@dataclass
class Interest(Institution):
    pass


@dataclass
class Accomplishment(Institution):
    pass


@dataclass
class Scraper:
    pass