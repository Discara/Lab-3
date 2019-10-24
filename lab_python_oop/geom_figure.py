from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Необходимо переопределить метод")
