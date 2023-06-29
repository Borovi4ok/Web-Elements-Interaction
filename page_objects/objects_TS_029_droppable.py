from selenium.webdriver.common.by import By


class Droppable:
    def __init__(self, driver):
        self.driver = driver

    simple_droppable = (By.ID, "droppable")
    simple_draggable = (By.ID, "draggable")
    accept_tab = (By.CSS_SELECTOR, "a#droppableExample-tab-accept")
    accept_droppable = (By.XPATH, "//div[@id='acceptDropContainer']//div[@id='droppable']")
    accept_draggable = (By.CSS_SELECTOR, "#acceptDropContainer div.drag-box")
    prevent_propagation_tab = (By.ID, "droppableExample-tab-preventPropogation")
    prevent_propagation_draggable = (By.ID, "dragBox")
    not_greedy_outer_droppable = (By.ID, "notGreedyDropBox")
    not_greedy_inner_droppable = (By.ID, "notGreedyInnerDropBox")
    greedy_outer_droppable = (By.ID, "greedyDropBox")
    greedy_inner_droppable = (By.ID, "greedyDropBoxInner")
    greedy_outer_droppable_text = (By.XPATH, "./p")
    revert_droppable_tab = (By.ID, "droppableExample-tab-revertable")
    revert_droppable_box = (By.XPATH, "(//div[@id='droppable'])[last()]")
    revertable_box = (By.ID, "revertable")
    not_revertable_box = (By.ID, "notRevertable")

    def get_simple_droppable(self):
        return self.driver.find_element(*Droppable.simple_droppable)

    def get_simple_draggable(self):
        return self.driver.find_element(*Droppable.simple_draggable)

    def get_accept_tab(self):
        return self.driver.find_element(*Droppable.accept_tab)

    def get_accept_droppable(self):
        return self.driver.find_element(*Droppable.accept_droppable)

    def get_accept_draggable(self):
        return self.driver.find_elements(*Droppable.accept_draggable)

    def get_prevent_propagation_tab(self):
        return self.driver.find_element(*Droppable.prevent_propagation_tab)

    def get_prevent_propagation_draggable(self):
        return self.driver.find_element(*Droppable.prevent_propagation_draggable)

    def get_not_greedy_outer_droppable(self):
        return self.driver.find_element(*Droppable.not_greedy_outer_droppable)

    def get_not_greedy_inner_droppable(self):
        return self.driver.find_element(*Droppable.not_greedy_inner_droppable)

    def get_greedy_outer_droppable(self):
        return self.driver.find_element(*Droppable.greedy_outer_droppable)

    def get_greedy_inner_droppable(self):
        return self.driver.find_element(*Droppable.greedy_inner_droppable)

    @staticmethod
    def get_greedy_outer_droppable_text(parent_element):
        return parent_element.find_element(*Droppable.greedy_outer_droppable_text)

    def get_revert_droppable_tab(self):
        return self.driver.find_element(*Droppable.revert_droppable_tab)

    def get_revert_droppable_box(self):
        return self.driver.find_element(*Droppable.revert_droppable_box)

    def get_revertable_box(self):
        return self.driver.find_element(*Droppable.revertable_box)

    def get_not_revertable_box(self):
        return self.driver.find_element(*Droppable.not_revertable_box)
