from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get("https://www.novaliderinformatica.com.br/computadores-gamers")

# Nome do produto
titulos = driver.find_elements(By.XPATH, "//a[@class='nome-produto']")
# Preço do produto
precos = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")

# Criar planilha
workbook = openpyxl.Workbook()
# cria pagina produtos
workbook.create_sheet("produtos")
# seleciona pagina produtos
sheet_produtos = workbook["produtos"]
sheet_produtos["A1"].value = "Produto"
sheet_produtos["B1"].value = "Preço"
workbook.save("produtos.xlsx")


# inserir na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])

workbook.save("produtos.xlsx")
