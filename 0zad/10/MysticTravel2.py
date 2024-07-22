from tkinter import *

class Application(Frame):
    """ GUI-приложение, создающее рассказ на основе пользовательского ввода. """
    
    def __init__(self, master):
        """ Инициализирует рамку. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        """ Создает элементы управления, с помощью которых пользователь будет вводить исходные данные и получать готовый рассказ. """
        
        # Заголовок
        Label(self, text="Сумасшедший сказочник", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
        
        # Инструкция
        Label(self, text="Введите данные для создания нового рассказа:", font=("Arial", 12)).grid(row=1, column=0, columnspan=3, pady=5)

        # Метка и поле ввода для имени человека
        Label(self, text="Имя персонажа:", font=("Arial", 10)).grid(row=2, column=0, sticky=W, padx=10)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=2, column=1, padx=10, sticky=W)
        
        # Метка и поле ввода для существительного
        Label(self, text="Множественное существительное:", font=("Arial", 10)).grid(row=3, column=0, sticky=W, padx=10)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=3, column=1, padx=10, sticky=W)
        
        # Метка и поле ввода для глагола
        Label(self, text="Глагол в инфинитиве:", font=("Arial", 10)).grid(row=4, column=0, sticky=W, padx=10)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=4, column=1, padx=10, sticky=W)
        
        # Метка для группы флажков с прилагательными
        Label(self, text="Прилагательные:", font=("Arial", 10)).grid(row=5, column=0, sticky=W, padx=10)
        
        # Флажок со словом "нетерпеливый"
        self.is_itchy = BooleanVar()
        Checkbutton(self, text="Нетерпеливый", variable=self.is_itchy).grid(row=5, column=1, sticky=W, padx=10)
        
        # Флажок со словом "радостный"
        self.is_joyous = BooleanVar()
        Checkbutton(self, text="Радостный", variable=self.is_joyous).grid(row=5, column=2, sticky=W, padx=10)
        
        # Флажок со словом "пронизывающий"
        self.is_electric = BooleanVar()
        Checkbutton(self, text="Пронизывающий", variable=self.is_electric).grid(row=5, column=3, sticky=W, padx=10)
        
        # Метка для переключателя с названиями частей тела
        Label(self, text="Часть тела:", font=("Arial", 10)).grid(row=6, column=0, sticky=W, padx=10)
        
        # Переменная, содержащая название одной из частей тела
        self.body_part = StringVar()
        self.body_part.set(None)
        
        # Переключатели с названиями частей тела
        body_parts = ["Пупок", "Большой палец ноги", "Продолговатый мозг"]
        for idx, part in enumerate(body_parts):
            Radiobutton(self, text=part, variable=self.body_part, value=part).grid(row=6, column=idx + 1, sticky=W, padx=10)
        
        # Кнопка отсылки данных
        Button(self, text="Получить рассказ", command=self.tell_story, font=("Arial", 12)).grid(row=7, column=0, columnspan=4, pady=10)
        
        self.story_txt = Text(self, width=80, height=15, wrap=WORD, font=("Arial", 10))
        self.story_txt.grid(row=8, column=0, columnspan=4, padx=10, pady=10)
    
    def tell_story(self):
        """ Заполняет текстовую область очередной историей на основе пользовательского ввода. """
        # Получение значений из интерфейса
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "нетерпеливое, "
        if self.is_joyous.get():
            adjectives += "радостное, "
        if self.is_electric.get():
            adjectives += "пронизывающее, "
        
        body_part = self.body_part.get()
        
        # Создание рассказа
        story = f"Знаменитый путешественник {person} уже совсем отчаялся довершить дело всей своей жизни - поиск затерянного города, в котором, по легенде, обитали {noun}. Но однажды {noun} и {person} столкнулись лицом к лицу. Мощное, {adjectives}ни с чем не сравнимое чувство охватило душу путешественника. После стольких лет поисков цель была наконец достигнута. {person} ощутил, как на его {body_part} скатилась слезинка. И тут внезапно {noun} перешли в атаку, и {person} был ими мгновенно сожран. Мораль? Если задумали {verb}, надо делать это с осторожностью."
        
        # Вывод рассказа на экран
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

root = Tk()
root.title("Сумасшедший сказочник")
app = Application(root)
root.mainloop()
