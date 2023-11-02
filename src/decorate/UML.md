```mermaid 
classDiagram
    direction BT

    class Beverage {
        <<abstract>>           
        
        str description

        getDescription() str
        cost()* float
    }

    class Espresso {
        cost() float

    }

    class HouseBlend {
        cost() float
    }

    Espresso --|> Beverage
    HouseBlend --|> Beverage


    class CondimentDecorator {
        <<abstract>>

        Beverage beverage
        getDescription()* str
    }

    CondimentDecorator --|> Beverage
    CondimentDecorator --* Beverage

    class Mocha {
        getDescription() str
        cost() float
    }    


    class Soy {
        getDescription() str
        cost() float
    }

    Mocha --|> CondimentDecorator
    Soy --|> CondimentDecorator

```