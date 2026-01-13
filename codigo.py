# Passo 1: Abrir a base de dados
# Passo 2: Abrir o navegador
# Passo 3: Entrar no sistema
# Passo 4: Fazer login 
# Passo 5: Cadastrar produto
# Passo 6: Repetir passo 4 até acabar a lista

import pyautogui;
import time;
import pandas;

pyautogui.PAUSE = 0.5;
url= "https://dlp.hashtagtreinamentos.com/python/intensivao/login";

# Passo 1
table= pandas.read_csv("produtos.csv")


# Passo 2
pyautogui.press("win");
pyautogui.write("brave");
pyautogui.press("enter");

# Passo 3
pyautogui.write(url);
pyautogui.press("enter");
time.sleep(2);
    
# Passo 4
pyautogui.click(x=677, y=400);
pyautogui.write("email@email.com");
pyautogui.press("tab");
pyautogui.write("senha");
pyautogui.press("enter");



# Passo 5/6
for line in table.index:
    pyautogui.click(x=667, y=286);
    pyautogui.write(str(table.loc[line, "codigo"]))
    pyautogui.press("tab");

    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab");

    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab");

    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab");

    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab");

    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab");

    obs = str(table.loc[line, "obs"]);
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab");
    pyautogui.press("enter");

    pyautogui.scroll(5000);

