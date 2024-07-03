```mermaid 
classDiagram
    direction BT

    class Singleton{
        -_instance: Singleton

        +get_instance() Singleton
    }

    Singleton --> Singleton : create
```