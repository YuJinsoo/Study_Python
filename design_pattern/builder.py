## guru 예제
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    콘크리트빌더 클래스는 Builder interface 를 따르고,
    생성 단계에 필요한 구체적인 구현을 정의한다
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        콘크리트 빌더는 결과를 반환하기 위한 자체 메서드를 제공해야 합니다.
        다양한 유형의 빌더가 동일한 인터페이스를 따르지 않는 완전히 다른 제품을 생성할 수 있기 때문입니다.
        따라서 이러한 메서드는 기본 빌더 인터페이스에서 선언될 수 없습니다.
        (적어도 정적 타입 프로그래밍 언어에서는 그렇습니다.)

        일반적으로 최종 결과를 반환한 후 빌더 인스턴스는 다른 제품을 생성할 준비가 된 것으로 예상됩니다.
        따라서 `product` 메서드 본문 끝에서 reset 메서드를 호출하는 것이 일반적입니다.
        하지만 이 동작은 필수는 아니며, 클라이언트가 따로 호출하는 방법도 있다.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    클라이언트 코드는 빌더 객체를 생성하여 디렉터에게 전달한 다음
    생성 프로세스를 시작합니다. 최종 결과는 빌더 객체에서 가져옵니다.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Director 클래스 없이 사용할 수 있음.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()



## 빌더패턴
# 햄버거 만드는 예제
class Burger:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def show(self):
        print("Burger with:")
        for ing in self.ingredients:
            print(f" - {ing}")

# Builder Interface
class BurgerBuilder:
    def add_bun(self):
        pass

    def add_patty(self):
        pass

    def add_sauce(self):
        pass

    def get_burger(self):
        pass

# Concrete Builder
class CheeseBurgerBuilder(BurgerBuilder):
    def __init__(self):
        self.burger = Burger()

    def add_bun(self):
        self.burger.add_ingredient("Sesame Bun")

    def add_patty(self):
        self.burger.add_ingredient("Beef Patty")

    def add_sauce(self):
        self.burger.add_ingredient("Cheddar Cheese")
        self.burger.add_ingredient("Ketchup")

    def get_burger(self):
        ## 결과물 반환...
        # 여기서 self.burger를 초기화 해줘도 됨.(다음 버거를 만들기 위해)
        return self.burger

# Director
class BurgerDirector:
    def __init__(self, builder: BurgerBuilder):
        self.builder = builder

    def construct_burger(self):
        self.builder.add_bun()
        self.builder.add_patty()
        self.builder.add_sauce()
        return self.builder.get_burger()

# 클라이언트 코드
if __name__ == "__main__":
    builder = CheeseBurgerBuilder()
    director = BurgerDirector(builder)
    burger = director.construct_burger()
    burger.show()

## 실행 결과
# Burger with:
#  - Sesame Bun
#  - Beef Patty
#  - Cheddar Cheese
#  - Ketchup


## Fluent Interface 방식
# Product
class BurgerFluent:
    def __init__(self):
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def show(self):
        print("Burger with:")
        for ing in self.ingredients:
            print(f" - {ing}")

# Fluent Builder
class BBurgerFluentBuilder:
    def __init__(self):
        self.burger = BurgerFluent()

    def add_bun(self, bun_type="Regular Bun"):
        self.burger.add(bun_type)
        return self

    def add_patty(self, patty_type="Beef Patty"):
        self.burger.add(patty_type)
        return self

    def add_cheese(self, cheese_type="Cheddar Cheese"):
        self.burger.add(cheese_type)
        return self

    def add_sauce(self, sauce="Ketchup"):
        self.burger.add(sauce)
        return self

    def add_veggies(self, veggies="Lettuce & Tomato"):
        self.burger.add(veggies)
        return self

    def build(self):
        return self.burger

# 클라이언트 코드
if __name__ == "__main__":
    burger = (
        BBurgerFluentBuilder()
        .add_bun("Sesame Bun")
        .add_patty("Chicken Patty")
        .add_cheese("Swiss Cheese")
        .add_veggies("Lettuce & Pickles")
        .add_sauce("Mayo")
        .build()
    )

    burger.show()