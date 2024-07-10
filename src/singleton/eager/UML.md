# Eager Singleton

```mermaid
classDiagram
    direction BT

    class SingletonMeta{
        -_instances: dict

        -__init__()
        -__call__()
    }

    Singleton --|> SingletonMeta
```
