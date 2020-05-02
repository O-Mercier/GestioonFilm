import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from Workbook import Workbook

# colors scheme 2:
# gainsboro (white/light blue) = CFDBD5
# ivory = E8EDDF
# maize (yellow) = F5CB5C
# raisin black = 242423
# jet (grey) = 333533

GAINSBORO = "#E8EDDF"
IVORY = "#E8EDDF"
MAIZE = "#F5CB5C"
RAISIN_BLACK = "#242423"
JET = "#333533"

HELV_30_BUTTON_FONT = "Helvetica, 30"
HELV_20_BUTTON_FONT = "Helvetica, 20"
HELV_15_FONT = "Helvetica, 15"
FUTURA_20_FONT = "Futura, 20"
FUTURA_15_FONT = "Futura, 15"


class MenuGUI:
    def __init__(self, workbook):
        self.workbook = workbook
        self.window = tk.Tk()
        self.window.title("Gestionnaire de films")
        # self.window.overrideredirect(1)
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        h = ws / 2
        w = ws / 2
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.configure(background='#242423')
        main_menu_frame = tk.Frame(self.window, bg='#242423')
        main_menu_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        main_menu_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        self.btn_DEBUG = tk.Button(main_menu_frame, text="DEBUG", command=self.debug_ph,
                                   bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                   bg=RAISIN_BLACK, fg=IVORY, font=HELV_30_BUTTON_FONT)
        self.btn_DEBUG.place(relx=0, rely=0, relwidth=1, relheight=0.175)

        self.btn_category = tk.Button(main_menu_frame, text="catégories", command=self.manage_category_frame,
                                      bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                      bg=RAISIN_BLACK, fg=IVORY, font=HELV_30_BUTTON_FONT)
        self.btn_category.place(relx=0, rely=0.275, relwidth=1, relheight=0.175)

        self.btn_research = tk.Button(main_menu_frame, text="recherche et gestion", command=self.open_workbook,
                                      bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                      bg=RAISIN_BLACK, fg=IVORY, font=HELV_30_BUTTON_FONT)
        self.btn_research.place(relx=0, rely=0.550, relwidth=1, relheight=0.175)

        self.btn_exit = tk.Button(main_menu_frame, text="quitter", command=self.exit_ap,
                                  bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                  bg=RAISIN_BLACK, fg=IVORY, font=HELV_30_BUTTON_FONT)
        self.btn_exit.place(relx=0, rely=0.825, relwidth=1, relheight=0.175)

        self.window.mainloop()

    def exit_ap(self):  # TODO implement saving
        exit()

    def open_workbook(self):
        WorkbookGUI(self.workbook)

    def manage_category_frame(self):
        GestionCategGUI(self.workbook)

    def debug_ph(self):
        AlertPopUP('test', 'test message',
                   btn1=dict(text='test', command=print('test')),
                   btn2=dict(text='test', command=print('test')))


class AlertPopUP:
    def __init__(self, title, text, **kwargs):
        """
        :param kwargs:  btn1=dict(text=String, command=function)
                        btn2=dict(text=String, command=function)
        """

        self.popup = tk.Tk()
        self.popup.title(title)
        self.popup.overrideredirect(1)
        self.popup.configure(bg='#F5CB5C')
        ws = self.popup.winfo_screenwidth()  # width of the screen
        hs = self.popup.winfo_screenheight()  # height of the screen
        h = ws / 4
        w = ws / 4
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.popup.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.popup_frame = tk.Frame(self.popup, bg='#F5CB5C')
        self.popup_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.label = tk.Label(self.popup_frame, text=text, bg='#F5CB5C', fg='#242423', anchor=tk.CENTER,
                              font=FUTURA_20_FONT)
        self.label.place(relx=0, rely=0, relwidth=1, relheight=0.27)
        if 'btn1' in kwargs:
            self.B1 = tk.Button(self.popup_frame, text=kwargs['btn1']['text'], command=kwargs['btn1']['command'],
                                activeforeground="#F5CB5C", activebackground="#333533",
                                bg="#242423", fg="#E8EDDF", font=HELV_20_BUTTON_FONT)
            self.B1.place(relx=0, rely=0.37, relwidth=1, relheight=0.27)
        else:
            self.B1 = tk.Button(self.popup_frame, text='OK', command=self.popup.destroy,
                                activeforeground="#F5CB5C", activebackground="#333533",
                                bg="#242423", fg="#E8EDDF", font=HELV_20_BUTTON_FONT)
            self.B1.place(relx=0, rely=0.74, relwidth=1, relheight=0.27)
        if 'btn2' in kwargs:
            self.B2 = tk.Button(self.popup_frame, text=kwargs['btn2']['text'], command=kwargs['btn2']['command'],
                                activeforeground="#F5CB5C", activebackground="#333533",
                                bg="#242423", fg="#E8EDDF", font=HELV_20_BUTTON_FONT)
            self.B2.place(relx=0, rely=0.74, relwidth=1, relheight=0.27)

        print('\a')
        self.popup.mainloop()
        self.set_active()


class WorkbookGUI:
    # TODO change return button size, switch second zone button color

    def __init__(self, workbook):
        self.workbook = workbook
        self.parameter_dict = dict()
        self.result_dict = dict()
        self.workbook_frame = tk.Tk()
        self.workbook_frame.title("Recherche de film")
        ws = self.workbook_frame.winfo_screenwidth()  # width of the screen
        hs = self.workbook_frame.winfo_screenheight()  # height of the screen
        h = hs
        w = ws
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.workbook_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.workbook_frame.configure(background=RAISIN_BLACK)
        self.main_frame = tk.Frame(self.workbook_frame, background=RAISIN_BLACK)
        self.main_frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
        cols = ('year', 'category', 'director', 'actors', 'rating')
        self.search_result_frame = tk.Frame(self.main_frame, background=RAISIN_BLACK)
        self.search_result_frame.place(relx=0.4, rely=0, relwidth=0.6, relheight=0.8)
        style = ttk.Style(self.workbook_frame)
        style.element_create("Custom.Treeheading.border", "from", "default")
        style.layout("Custom.Treeview.Heading", [
            ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
            ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                    ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                    ("Custom.Treeheading.text", {'side': 'left', 'sticky': 'we'})
                ]})
            ]}),
        ])
        style.configure("Custom.Treeview.Heading", background=GAINSBORO,
                        foreground=RAISIN_BLACK, font=HELV_15_FONT, relief="flat", anchor=tk.CENTER)
        style.map("Custom.Treeview.Heading",
                  relief=[('active', 'groove'), ('pressed', 'sunken')])
        style.configure("Custom.Treeview", fieldbackground=GAINSBORO, fieldforeground=RAISIN_BLACK)
        self.result_tree = ttk.Treeview(self.search_result_frame, columns=cols, style="Custom.Treeview")
        self.result_tree.place(relx=0, rely=0, relwidth=1, relheight=1)
        header_w = round(((ws / 2) * 0.8) / 6)
        self.result_tree.column('#0', width=header_w, minwidth=header_w)
        self.result_tree.column('year', width=header_w, minwidth=header_w)
        self.result_tree.column('category', width=header_w, minwidth=header_w)
        self.result_tree.column('director', width=header_w, minwidth=header_w)
        self.result_tree.column('actors', width=header_w, minwidth=header_w)
        self.result_tree.column('rating', width=header_w, minwidth=header_w)
        self.result_tree.heading('#0', text="Nom", anchor=tk.W)
        self.result_tree.heading('year', text="Année", anchor=tk.W)
        self.result_tree.heading('category', text="Catégorie", anchor=tk.W)
        self.result_tree.heading('director', text="Réalisateur", anchor=tk.W)
        self.result_tree.heading('actors', text="Acteurs", anchor=tk.W)
        self.result_tree.heading('rating', text="Note", anchor=tk.W)

        search_frame = tk.Frame(self.main_frame, background=RAISIN_BLACK)
        search_frame.place(relx=0, rely=0, relwidth=0.35, relheight=0.8)
        self.title_film_frame = tk.Frame(search_frame, background=RAISIN_BLACK)
        self.title_film_frame.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        self.tittle_label = tk.Label(self.title_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     text="titre", anchor="w")
        self.tittle_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.tittle_entry = tk.Entry(self.title_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT)
        self.tittle_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour la saisie de la date de création
        self.year_film_frame = tk.Frame(search_frame, background=RAISIN_BLACK)
        self.year_film_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.05)
        self.year_label = tk.Label(self.year_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                   text="année", anchor="w")
        self.year_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.year_entry = tk.Entry(self.year_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT)
        self.year_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour le réalisateur
        self.director_film_frame = tk.Frame(search_frame, background=RAISIN_BLACK)
        self.director_film_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.05)
        self.director_label = tk.Label(self.director_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                       text="réalisateur", anchor="w")
        self.director_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.director_entry = tk.Entry(self.director_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT)
        self.director_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour la saisie de trois noms d'acteurs
        self.actors_film_frame = tk.Frame(search_frame, background=RAISIN_BLACK)
        self.actors_film_frame.place(relx=0, rely=0.3, relwidth=1, relheight=0.15)
        self.actors_label = tk.Label(self.actors_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     text="acteurs", anchor="w")
        self.actors_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.actor1_entry = tk.Entry(self.actors_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT)
        self.actor1_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.33)
        self.actor2_entry = tk.Entry(self.actors_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT)
        self.actor2_entry.place(relx=0.3, rely=0.33, relwidth=0.7, relheight=0.33)
        self.actor3_entry = tk.Entry(self.actors_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT)
        self.actor3_entry.place(relx=0.3, rely=0.66, relwidth=0.7, relheight=0.33)
        # frame pour la catégorie
        self.category_film_frame = tk.Frame(search_frame, background=RAISIN_BLACK)
        self.category_film_frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.05)
        style.map('TCombobox', fieldbackground=[('readonly', RAISIN_BLACK)])
        style.map('TCombobox', fieldforeground=[('readonly', GAINSBORO)])
        style.map('TCombobox', background=[('readonly', GAINSBORO)])
        style.map('TCombobox', foreground=[('readonly', GAINSBORO)])
        style.map('TCombobox', selectbackground=[('readonly', RAISIN_BLACK)])
        style.map('TCombobox', selectforeground=[('readonly', GAINSBORO)])
        self.category_label = tk.Label(self.category_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                       text="catégorie", anchor="w")
        self.category_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.category_combobox = ttk.Combobox(self.category_film_frame, values=list(self.workbook.category_dict.keys()),
                                              font=FUTURA_15_FONT)
        self.category_combobox['state'] = 'readonly'
        self.category_combobox.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.category_rating_frame = tk.Frame(search_frame, background='#7A918D')
        self.category_rating_frame.place(relx=0, rely=0.6, relwidth=1, relheight=0.05)
        self.rating_label = tk.Label(self.category_rating_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     text="note", anchor="w")
        self.rating_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.rating_combobox = ttk.Combobox(self.category_rating_frame, values=list(range(0, 11)), font=FUTURA_15_FONT)
        self.rating_combobox['state'] = 'readonly'
        self.rating_combobox.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.search_button = tk.Button(search_frame, text="chercher", command=self.update_tree,
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                       bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT)
        self.search_button.place(relx=0, rely=0.75, relwidth=1, relheight=0.1)
        self.clear_button = tk.Button(search_frame, text="vider champs", command=self.clear_inputs,
                                      bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                      bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT)
        self.clear_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        self.options_button_frame = tk.Frame(self.main_frame, background=RAISIN_BLACK)
        self.options_button_frame.place(relx=0, rely=0.85, relwidth=1, relheight=0.1)
        self.add_button = tk.Button(self.options_button_frame, text="ajouter film", command=self.add_film,
                                    bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                    bg=GAINSBORO, fg=RAISIN_BLACK, font=HELV_30_BUTTON_FONT)
        self.add_button.place(relx=0, rely=0, relwidth=0.35, relheight=1)
        self.edit_button = tk.Button(self.options_button_frame, text="modifier film",
                                     bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                     bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT,
                                     command=self.edit_film)
        self.edit_button.place(relx=0.4, rely=0, relwidth=0.15, relheight=1)
        self.delete_button = tk.Button(self.options_button_frame, text="supprimer film",
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                       bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT,
                                       command=self.delete_film)
        self.delete_button.place(relx=0.60, rely=0, relwidth=0.15, relheight=1)
        self.save_button = tk.Button(self.options_button_frame, text="exporter liste",
                                     bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                     bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT,
                                     command=self.save_search)
        self.save_button.place(relx=0.80, rely=0, relwidth=0.2, relheight=1)

        self.cancel_button = tk.Button(self.workbook_frame, text="retour",
                                     bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                     bg=RAISIN_BLACK, fg=MAIZE, font=HELV_20_BUTTON_FONT,
                                     command=self.exit_window)
        self.cancel_button.place(relx=0.74, rely=0.90, relwidth=0.16, relheight=0.05)

        self.set_active()

    def update_tree(self):
        for element in self.result_tree.get_children():
            self.result_tree.delete(element)
        self.update_parameter()
        if self.parameter_dict:
            self.result_dict = self.workbook.find_films(**self.parameter_dict)  # TODO Pop-up if no result
        else:
            self.result_dict = self.workbook.find_films(all=True)
        for k, v in self.result_dict.items():
            self.result_tree.insert('', "end", text=k, values=[v.get('year'), v.get('category'),
                                                               v.get('director'),
                                                               list(filter(lambda actor: actor, v.get('actors'))),
                                                               v.get('rating'), v.get('comment')])

    def set_active(self):  # TODO bind update to enter?
        self.workbook_frame.lift()
        self.workbook_frame.focus_force()
        self.workbook_frame.grab_set()
        self.workbook_frame.grab_release()

    def exit_window(self):
        self.workbook_frame.destroy()

    def edit_film(self):  # TODO implement confirmation pop-up
        InputFilmGUI(self.workbook, self)

    def delete_film(self):  # TODO implement confirmation pop-up
        try:
            selected = self.result_tree.focus()
            name = self.result_tree.item(selected).get('text')
            category = self.result_tree.item(selected).get('values')[1]
            self.workbook.remove_film(name, category)
            self.result_tree.delete(selected)
        except IndexError:  # TODO implement please select pop up
            pass

    def save_search(self):  # TODO implement confirmation pop-up
        path = filedialog.asksaveasfile(initialdir="/", filetypes=[("Fichier CSV", "*.csv")])
        if path:
            Workbook.save_search(path.name + '.csv', self.results_dict)
            self.exit_window()

    def add_film(self):
        InputFilmGUI(self.workbook, self, add=True)

    def clear_inputs(self):  # TODO implement method
        pass

    def update_parameter(self):
        if self.tittle_entry.get():
            self.parameter_dict.update(name=self.tittle_entry.get())
        if self.year_entry.get():
            self.parameter_dict.update(year=self.year_entry.get())
        if self.director_entry.get():
            self.parameter_dict.update(name=self.director_entry.get())
        if self.actor1_entry.get() or self.actor2_entry.get() or self.actor3_entry.get():
            self.parameter_dict.update(actors=[entry.get() for entry in
                                               [self.actor1_entry,
                                                self.actor2_entry,
                                                self.actor3_entry] if entry.get()])
        if self.category_combobox.get():
            self.parameter_dict.update(category=self.category_combobox.get())
        if self.rating_combobox.get():
            self.parameter_dict.update(rating=self.rating_combobox.get())


class InputFilmGUI:
    def __init__(self, workbook, workbookGUI, **kwargs):
        """
        :param kwargs:
            add=True
            edit=True TODO implement for readability
        """
        self.workbook = workbook
        self.workbookGUI = workbookGUI
        self.film_frame = tk.Tk()
        if kwargs.get('add'):
            self.film_frame.title("Ajout d'un film")
        else:
            self.film_frame.title("Modification d'un film")
        self.film_frame.overrideredirect(1)
        w = 500
        h = 700
        ws = self.film_frame.winfo_screenwidth()  # width of the screen
        hs = self.film_frame.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.film_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.film_frame.configure(background='#AAC0AA')
        main_film_frame = tk.Frame(self.film_frame, background='#AAC0AA')
        main_film_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        # frame pour la saisie du titre
        self.title_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.title_film_frame.place(relx=0, rely=0, relheight=0.08, relwidth=1)
        self.tittle_label = tk.Label(self.title_film_frame, bg="#7A918D", fg="#AAC0AA", text="Titre : ")
        self.tittle_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.tittle_entry = tk.Entry(self.title_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.tittle_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour la saisie de la date de création
        self.year_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.year_film_frame.place(relx=0, rely=0.08, relheight=0.08, relwidth=1)
        self.year_label = tk.Label(self.year_film_frame, bg="#7A918D", fg="#AAC0AA", text="Année : ")
        self.year_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.year_entry = tk.Entry(self.year_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.year_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour le réalisateur
        self.director_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.director_film_frame.place(relx=0, rely=0.18, relheight=0.08, relwidth=1)
        self.director_label = tk.Label(self.director_film_frame, bg="#7A918D", fg="#AAC0AA", text="Réalisateur : ")
        self.director_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.director_entry = tk.Entry(self.director_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.director_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour la saisie de trois noms d'acteurs
        self.actors_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.actors_film_frame.place(relx=0, rely=0.28, relheight=0.22, relwidth=1)
        self.actors_label = tk.Label(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA", text="Acteurs")
        self.actors_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.actor1_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor1_entry.place(relx=0.3, rely=0, relheight=0.333, relwidth=0.7)
        self.actor2_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor2_entry.place(relx=0.3, rely=0.333, relheight=0.333, relwidth=0.7)
        self.actor3_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor3_entry.place(relx=0.3, rely=0.666, relheight=0.333, relwidth=0.7)
        # frame pour la catégorie
        self.category_film_frame = tk.Frame(main_film_frame, background='#AAC0AA')
        self.category_film_frame.place(relx=0, rely=0.52, relheight=0.16, relwidth=1)
        self.category_label = tk.Label(self.category_film_frame, bg="#7A918D", fg="#AAC0AA", text="Categorie : ")
        self.category_label.place(relx=0, rely=0, relheight=0.4, relwidth=0.3)
        self.category_combobox = ttk.Combobox(self.category_film_frame, values=list(self.workbook.category_dict.keys()),
                                              state='readonly')
        self.category_combobox.current(0)
        self.category_combobox.place(relx=0.3, rely=0, relheight=0.4, relwidth=0.7)
        self.category_combobox.place(relx=0.3, rely=0, relheight=0.4, relwidth=0.7)
        self.note_label = tk.Label(self.category_film_frame, bg="#7A918D", fg="#AAC0AA", text="Note : ")
        self.note_label.place(relx=0, rely=0.5, relheight=0.4, relwidth=0.3)
        self.rating_combobox = ttk.Combobox(self.category_film_frame, values=list(range(0, 11)), state='readonly')
        self.rating_combobox.place(relx=0.3, rely=0.5, relheight=0.4, relwidth=0.7)
        # frame pour les commentaires
        self.commentary_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.commentary_film_frame.place(relx=0, rely=0.68, relheight=0.2, relwidth=1)
        self.commentary_label = tk.Label(self.commentary_film_frame, bg="#7A918D", fg="#AAC0AA", text="commentaires : ")
        self.commentary_label.place(relx=0, rely=0, relheight=0.2, relwidth=1)
        self.commentary_text = tk.Text(self.commentary_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.commentary_text.place(relx=0, rely=0.2, relheight=0.8, relwidth=1)
        # frame pour fermeture de la saisie
        self.buttons_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.buttons_film_frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)
        if kwargs.get('add'):
            self.add_button = tk.Button(self.buttons_film_frame, bg="#7A918D",
                                        fg="#AAC0AA", text="ajouter",
                                        command=self.add_film_ctr)
            self.add_button.place(relx=0, rely=0, relheight=1, relwidth=0.5)
        else:
            self.edit_button = tk.Button(self.buttons_film_frame, bg="#7A918D",
                                         fg="#AAC0AA", text="modifier",
                                         command=self.edit_film_ctr)
            self.edit_button.place(relx=0, rely=0, relheight=1, relwidth=0.5)
        self.cancel_button = tk.Button(self.buttons_film_frame, bg="#7A918D",
                                       fg="#AAC0AA", text="annuler",
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)
        self.set_active()

    def add_film_ctr(self):
        self.workbook.add_film(self.category_combobox.get(),  # TODO implement pop up if missing name or year
                               self.tittle_entry.get(),
                               self.year_entry.get(),
                               director=self.director_entry.get(),
                               actors=[self.actor1_entry.get(), self.actor2_entry.get(), self.actor3_entry.get()],
                               rating=self.rating_combobox.get(),
                               comment=self.commentary_text.get('1.0', tk.END))
        self.workbookGUI.update_tree()
        self.exit_window()

    def edit_film_ctr(self):
        self.workbook.edit_film(self.category_combobox.get(),  # TODO implement pop up if missing name or year
                                self.tittle_entry.get(),
                                year=self.year_entry.get(),
                                director=self.director_entry.get(),
                                actors=[self.actor1_entry.get(), self.actor2_entry.get(), self.actor3_entry.get()],
                                rating=self.rating_combobox.get(),
                                comment=self.commentary_text.get('1.0', tk.END))
        self.workbookGUI.update_tree()
        self.exit_window()

    def exit_window(self):
        self.film_frame.destroy()

    def set_active(self):
        self.film_frame.lift()
        self.film_frame.focus_force()
        self.film_frame.grab_set()
        self.film_frame.grab_release()


class GestionCategGUI:
    def __init__(self, workbook):
        self.workbook = workbook
        self.manage_window = tk.Tk()
        self.manage_window.title("gérer les catégories")
        # self.manage_window.overrideredirect(1)
        ws = self.manage_window.winfo_screenwidth()  # width of the screen
        hs = self.manage_window.winfo_screenheight()  # height of the screen
        w = ws / 2  # width for the Tk root
        h = ws / 2  # height for the Tk root
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.manage_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.manage_window.configure(background='#242423')
        manage_main_frame = tk.Frame(self.manage_window, bg="#242423")
        manage_main_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        btn_add_category = tk.Button(manage_main_frame, text="ajouter une catégorie",
                                     bd=0, activeforeground="#242423", activebackground="#F5CB5C", bg="#242423",
                                     fg="#E8EDDF", font=HELV_30_BUTTON_FONT)
        btn_add_category.place(relx=0, rely=0, relwidth=1, relheight=0.27)

        btn_remove_category = tk.Button(manage_main_frame, text="supprimer une catégorie",
                                        bd=0, activeforeground="#242423", activebackground="#F5CB5C", bg="#242423",
                                        fg="#E8EDDF", font=HELV_30_BUTTON_FONT)
        btn_remove_category.place(relx=0, rely=0.37, relwidth=1, relheight=0.27)

        btn_exit = tk.Button(manage_main_frame, text="retour", command=self.exit_window,
                             bd=0, activeforeground="#242423", activebackground="#F5CB5C", bg="#242423",
                             fg="#E8EDDF", font=HELV_30_BUTTON_FONT)
        btn_exit.place(relx=0, rely=0.73, relwidth=1, relheight=0.27)

        self.set_active()

    def exit_window(self):
        self.manage_window.destroy()

    def set_active(self):
        self.manage_window.lift()
        self.manage_window.focus_force()
        self.manage_window.grab_set()
        self.manage_window.grab_release()


# colors scheme 2:
# gainsboro (white/light blue) = CFDBD5
# ivory = E8EDDF
# maize (yellow) = F5CB5C
# raisin black = 242423
# jet (grey) = 333533


if __name__ == "__main__":
    debug_workbook_gui = MenuGUI(Workbook())