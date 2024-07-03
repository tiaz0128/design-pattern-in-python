# Class level Singleton

```mermaid
classDiagram
    direction BT

    class Singleton{
        -_instance: Singleton = None

        +__new__() Singleton
    }

    Singleton --> Singleton : create
```