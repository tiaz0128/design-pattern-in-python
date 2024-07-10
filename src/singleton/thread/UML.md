# Thread Safe Singleton

```mermaid
classDiagram
    direction BT

    class SingletonMeta{
        -_instances: dict

        -__call__() Singleton
    }
    
    Singleton --|> SingletonMeta
```
