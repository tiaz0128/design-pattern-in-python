# Meta Singleton

```mermaid
classDiagram
    direction BT

    class SingletonMeta{
        _instances : dict[SingletonMeta]
        +__call__(cls) Singleton
    }

    Singleton --|> SingletonMeta
```
