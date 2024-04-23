import flet as ft
import UI.view as v


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._pd = None

    def get_corsi_periodo(self,e):
        # pd=self._view.dd_periodo.value
        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico")
            return
        corsi = self._model.get_corsi_periodo(self._pd)
        self._view.lv_result.clean()
        for corso in corsi:
            self._view.lv_result.controls.append(ft.Text(corso))
        self._view.update_page()



    def get_studenti_periodo(self,e):
        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico")
            return
        num_studenti=self._model.get_numero_studenti_periodo(self._pd)
        self._view.lv_result.clean()
        self._view.lv_result.controls.append(ft.Text(f"Gli studenti iscritti a corsi del periodo didattco {self._pd} sono: {num_studenti}"))
        self._view.update_page()

    def get_studenti_corso(self,e):
        pass

    def get_dettaglio_corso(self,e):
        pass

    def leggi_tendina(self, e):
        self._pd = e.control.value  # e' un alternativa al prendere il valore del dropdown con self._view.dd_periodo.value
