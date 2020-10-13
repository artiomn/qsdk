Прототип квантового SDK
=======================

## Требования

### Предложить метод трансляции входных задач в базис QUBO

[Примеры от D-Wave](https://docs.dwavesys.com/docs/latest/c_handbook_1.html).


### Предоставить возможность решения квадратичной оптимизационной задачи

- В базисе [QUBO](https://en.wikipedia.org/wiki/Quadratic_unconstrained_binary_optimization): `argmin_s(s^T * Q * s)`. `s_i = {0, 1}`
- В базисе [Ising](https://en.wikipedia.org/wiki/Ising_model): `argmin_s(s^T * J * s + s^T * h)`. `s_i = {-1; 1}`
- Для базиса QUBO:
  * Трансляция входных задач в базис QUBO.
  * Учёт ограничений для QUBO: `sA <= b`.
- Для базиса Ising:
  * Конвертация между в базис QUBO.


### Реализовать поддержку бэк-эндов

- Адиабатический КК. Доступ через удалённое API. [Dwave-leap SDK](https://www.dwavesys.com/take-leap).
- Квантовый симулятор. Локальный, либо удалённый. [Квантовый симулятор РКЦ](https://qml.rqc.ru/products/simulator).
- Оптимизационный пакет. Локальный.


## Компоновка

quantum-sdk:

- solvers - солверы для различных типов базисов.
  * QSolver - QUBO.
- basis - работа с базисами:
  * convert - процедуры для конвертации между базисами. Переделаны из того, что есть в D-Wave.dimod.
- backends - вычислительные бэк-энды. Каждый - наследник класса `Backend`.
  * dwave. Удалённый доступ по сети.
  * qsim. Локальный или удалённый доступ по сети.
  * optim. Локальный запуск на классическом железе, доступ через импорт.
- examples - каталог с примерами.


### Диаграмма классов

```
@startuml ClassDiagram
left to right direction

package backends {
  class Backend {
  }

  class Solver {
  }


  package dwave {
    class DWaveBackend {
    }
    class dwave.QuboSolver {
    }
  }


  package optim {
    class LocalBackend {
    }
    class optim.QuboSolver {
    }
  }

  package qsim {
    class QuantumSimulationBackend {
    }
    class qsim.QuboSolver {
    }

  }



}

@enduml
```


## Пример использования

```python
from quantum_sdk import QSolver

qsolver = QSolver(backend=”quantum”)
Q = np.random.rand(5, 5)
s = qsolver.solve_qubo(Q)

>> s = [1,0,0,1,1]
```
