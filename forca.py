import tkinter as tk
from tkinter import messagebox as msg
import random as r

root = tk.Tk()
root.title("Jogo da Forca")
root.wm_resizable(height=False, width=False)

wordlist = [
    "Abacateiro", "Abandonado", "Acelerado", "Acidentado", "Acontecente",
    "Adversário", "Albergagem", "Alimentar", "Analisador", "Animadora",
    "Armazenada", "Atencioso", "Atraente", "Balneário", "Benefício",
    "Benfeitoria", "Bonificado", "Caldeirada", "Cabelereiro", "Candelabro",
    "Carregador", "Cervejeiro", "Conselheiro", "Contundente", "Criatividade",
    "Dedicado", "Deliberado", "Determinado", "Desempenho", "Desenvolver",
    "Desperdício", "Diferente", "Dirigente", "Elevado", "Emocionado",
    "Empreendedor", "Envolvente", "Estabelecer", "Estudantes", "Excepcional",
    "Exercício", "Extremista", "Felicidade", "Ferramenta", "Formidable",
    "Fundamento", "Graduado", "Graduação", "Imortalizar", "Imperador",
    "Indagador", "Inferior", "Inteligente", "Irregular", "Jovialidade",
    "Ladrilheiro", "Luminária", "Masculino", "Maturidade", "Observador",
    "Ouvinte", "Padecer", "Padeiro", "Palestra", "Paraíso",
    "Perfeição", "Pescador", "Preservar", "Processar", "Protetor",
    "Quadrado", "Refrigeração", "Relacionar", "Renovável", "Restaurador",
    "Responsável", "Revelador", "Salvação", "Salteador", "Sociedade",
    "Solitário", "Superação", "Suspender", "Telefone", "Temperatura",
    "Traficante", "Trilogia", "Universidade", "Valente", "Violento",
    "Vontade", "Viajante", "Valorização", "Vanguarda", "Apreciador",
    "Alimentador", "Aromatizador", "Bailarina", "Barricada", "Bem-estar",
    "Benfeitoria", "Benquisto", "Calculadora", "Caleidoscópio", "Carcinoma",
    "Caçadora", "Claridade", "Comandante", "Companheiro", "Complexo",
    "Conservador", "Coragem", "Cortesia", "Corredor", "Cuidadoso",
    "Curador", "Cauteloso", "Decifrar", "Definido", "Delegado",
    "Determinada", "Exibicionista", "Elétrico", "Estudioso", "Exibido",
    "Esclarecer", "Escalante", "Estagnado", "Envolvimento", "Empoderado",
    "Equilibrado", "Encorajante", "Exemplar", "Exagerado", "Fracasso",
    "Fisioterapeuta", "Freguesia", "Formalidade", "Flutuante", "Frontal",
    "Fundadora", "Galeria", "Gritante", "Gravidade", "Harmonioso",
    "Hereditário", "Hospitalar", "Iniciado", "Indicado", "Influência",
    "Inflação", "Inovador", "Inimigos", "Inteligente", "Insolente",
    "Jornada", "Joguinho", "Ligação", "Magnífico", "Mandato",
    "Mecânico", "Mendicante", "Moderno", "Motivador", "Ouvinte",
    "Obreiro", "Operário", "Paradoxal", "Paralisia", "Pedreiro",
    "Piligrinagem", "Pontualidade", "Provisório", "Prestigiar", "Reacionário",
    "Realizar", "Rejeitado", "Relatar", "Resistente", "Rivalidade",
    "Salvamento", "Senilidade", "Sensacional", "Sobrenatural", "Temático",
    "Tesoureiro", "Totalidade", "Tratamento", "Transtorno", "Tradição",
    "Ventilador", "Violonista", "Zangado", "Zumbi", "Vingança",
    "Vencido", "Vingador", "Versátil", "Voluntário", "Vanguarda"
]

word = "abc"


def newword():
    global word, wordlist
    word = (r.choice(wordlist)).lower()


def start_game():
    global word, guesses, max_atps, rem_atps, worddis

    newword()
    guesses = set()
    max_atps = 6
    rem_atps = max_atps
    worddis = ["_" for i in word]
    canvas.delete("all")
    upd_dis()


def upd_dis():
    wordlbl.config(text=" ".join(worddis))
    atplbl.config(text=f"Tentativas restantes: {rem_atps}")


def guess_letter():
    global rem_atps

    letter = enter.get().lower()
    enter.delete(0, tk.END)
    if len(letter) != 1 or not letter.isalpha():
        msg.showerror("Erro de carater", "Entrada Invalida. Tente novamente.")
        return
    if letter in guesses:
        msg.showwarning("Aviso", "Letra já foi sugerida.")
        return
    guesses.add(letter)
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                worddis[i] = letter
    else:
        rem_atps -= 1
        hangman()
    upd_dis()
    check_stat()


def check_stat():
    global rem_atps
    if "_" not in worddis:
        msg.showinfo("Parabéns!", "Você Ganhou!")
        start_game()
    elif rem_atps <= 0:
        msg.showinfo("Perdeste!", f'A palavra é "{word}".')
        start_game()


def hangman():
    if rem_atps == 5:
        canvas.create_line(100, 280, 100, 50, width=2)
        canvas.create_line(100, 50, 150, 50, width=2)
        canvas.create_line(20, 280, 180, 280, width=2)
    elif rem_atps == 4:
        canvas.create_line(150, 50, 150, 100, width=2)
    elif rem_atps == 3:
        canvas.create_oval(130, 100, 170, 140, width=2)
    elif rem_atps == 2:
        canvas.create_line(150, 140, 150, 200, width=2)
    elif rem_atps == 1:
        canvas.create_line(150, 140, 130, 160, width=2)
        canvas.create_line(150, 140, 170, 160, width=2)
    elif rem_atps == 0:
        canvas.create_line(150, 200, 130, 240, width=2)
        canvas.create_line(150, 200, 170, 240)


canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

wordlbl = tk.Label(root, text="", font="Fixedsys 12")
wordlbl.pack(pady=5)

enter = tk.Entry(root)
enter.pack(padx=10)

atplbl = tk.Label(root, text="", font="Fixedsys 12")
atplbl.pack(padx=10)

guessbtn = tk.Button(root, text="Feito!", font="Fixedsys 14", command=guess_letter)
guessbtn.pack(padx=10)

resetbtn = tk.Button(root, text="Reiniciar", font="Fixedsys 14", command=start_game)
resetbtn.pack(padx=10)
start_game()
root.mainloop()
