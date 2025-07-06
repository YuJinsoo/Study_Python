## 예제코드
# https://refactoring.guru/
from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    '''
    추상 팩토리 인터페이스는 서로 다른 추상 제품을 반환하는 메서드 집합을 선언합니다.
    이러한 제품을 패밀리라고 하며, 상위 수준 테마 또는 개념으로 연관됩니다.
    한 패밀리의 제품은 일반적으로 서로 협업할 수 있습니다.
    제품군에는 여러 변형이 있을 수 있지만, 한 변형의 제품은 다른 변형의 제품과 호환되지 않습니다.
    '''
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreateFactory1(AbstractFactory):
    '''
    콘크리트 팩토리는 단일 변형에 속하는 제품 군을 생성합니다.
    팩토리는 결과 제품의 호환성을 보장합니다.
    콘크리트 팩토리 메서드의 시그니처는 추상 제품을 반환하는 반면,
    메서드 내부에서는 콘크리트 제품이 인스턴스화됩니다.
    '''
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

class ConcreateFactory2(AbstractFactory):
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class AbstractProductA(ABC):
    '''
    제품군의 각 개별 제품은 기본 인터페이스를 가져야 합니다.
    모든 제품 변형은 이 인터페이스를 구현해야 합니다.
    '''
    @abstractmethod
    def useful_function_a(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self):
        pass

    @abstractmethod
    def another_useful_function_b(self):
        pass

class ConcreteProductB1(AbstractProductB):
    """
    변형인 제품 B1은 변형인 제품 A1에서만 제대로 작동할 수 있습니다.
    그럼에도 불구하고 AbstractProductA의 모든 인스턴스를 인수로 허용합니다.
    """
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        변형인 제품 B2는 변형인 제품 A2에서만 제대로 작동할 수 있습니다.
        그럼에도 불구하고, 모든 추상제품A 인스턴스를 인수로 허용합니다.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    클라이언트 코드는 추상 유형인 AbstractFactory와 AbstractProduct를 통해서만 팩토리와 제품을 사용합니다.
    이를 통해 팩토리 또는 제품 하위 클래스를 클라이언트 코드에 전달해도 코드 손상 없이 사용할 수 있습니다.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")




## gpt 예제코드 -------------------------------------------------------
# 다양한 운영 체제에서 UI 요소를 생성하는 시스템을 만든다고 가정해봅시다.
# 각 운영 체제마다 버튼과 체크박스 디자인이 다릅니다. Windows와 Mac에 맞는 UI 요소를 생성하는 시스템을 예
from abc import ABC, abstractmethod

## 1. 추상 제품(Abstract Product)
# 추상 버튼 클래스
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# 추상 체크박스 클래스
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

## 2. 구체적인 제품(Concrete Product)
# Windows 스타일 버튼
class WindowsButton(Button):
    def render(self):
        print("Rendering Windows Button")

# Mac 스타일 버튼
class MacButton(Button):
    def render(self):
        print("Rendering Mac Button")

# Windows 스타일 체크박스
class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering Windows Checkbox")

# Mac 스타일 체크박스
class MacCheckbox(Checkbox):
    def render(self):
        print("Rendering Mac Checkbox")


## 3.추상 팩토리 (Abstract Factory)
# UI 요소를 생성하는 인터페이스를 정의
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


## 4. 구체적인 팩토리 (Concrete Factory)
# 각 운영 체제에 맞는 구체적인 팩토리를 정의
# Windows 팩토리
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Mac 팩토리
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

## 5.클라이언트 (Client)
# 클라이언트는 추상 팩토리를 사용하여 객체를 생성합니다.
# 클라이언트는 구체적인 팩토리나 제품을 알지 못합니다.
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()

## 실행예시
def gpt_main():
    # 사용자가 Windows 환경이라면
    windows_factory = WindowsFactory()
    client_code(windows_factory)

    print("-----")

    # 사용자가 Mac 환경이라면
    mac_factory = MacFactory()
    client_code(mac_factory)
