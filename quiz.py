import tkinter as tk
from tkinter import messagebox

# Perguntas e respostas do quiz
questions = [
    {"question": "Quem é considerado o pai da sociologia?", "options": ["Auguste Comte", "Karl Marx", "Max Weber", "Emile Durkheim"], "answer": "Auguste Comte"},
    {"question": "Qual é o conceito central em Marx sobre a divisão da sociedade?", "options": ["Classe social", "Capitalismo", "Socialismo", "Proletariado"], "answer": "Classe social"},
    {"question": "Qual autor é conhecido por seu trabalho sobre a ética protestante e o espírito do capitalismo?", "options": ["Max Weber", "Emile Durkheim", "Karl Marx", "Auguste Comte"], "answer": "Max Weber"}
]

# Função para verificar a resposta e avançar para a próxima pergunta
def check_answer():
    global current_question
    selected_option = option_var.get()
    if selected_option == questions[current_question]["answer"]:
        messagebox.showinfo("Resultado", "Resposta Correta!")
    else:
        messagebox.showinfo("Resultado", "Resposta Errada!")

    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        messagebox.showinfo("Fim do Quiz", "Você completou o quiz!")
        root.destroy()

# Função para carregar uma pergunta
def load_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        options[i].config(text=option, value=option)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Quiz de Sociologia")

current_question = 0

question_label = tk.Label(root, text="", padx=20, pady=20)
question_label.pack()

option_var = tk.StringVar()

options = []
for i in range(4):
    option = tk.Radiobutton(root, text="", variable=option_var, value="", padx=20, pady=10)
    option.pack(anchor="w")
    options.append(option)

submit_button = tk.Button(root, text="Enviar", command=check_answer)
submit_button.pack(pady=20)

load_question()

root.mainloop()
