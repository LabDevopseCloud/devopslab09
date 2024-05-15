# -*- coding: utf-8 -*-
from app import app
import unittest
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

# envia uma requisicao GET para a URL
self.result = self.app.get('/')

def test_requisicao(self):
    # compara o status da requisicao (precisa ser igual a 200)
    self.assertEqual(self.result.status_code, 200)

def test_conteudo(self):
    # verifica o retorno do conteudo da pagina
    self.assertEqual(self.result.data.decode('utf-8'), "Hello Mariana")

