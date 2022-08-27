class Specification:
    """
    Спецификация (правила) базовая.
    «Спецификация» в программировании — это шаблон проектирования,
    посредством которого представление правил бизнес-логики может быть
    преобразовано в виде цепочки объектов, связанных операциями булевой логики.
    """

    def is_satisfied(self):
        raise NotImplementedError()
