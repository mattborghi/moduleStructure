# -*- coding: utf-8 -*-
'''
General documentation architecture:
Home
Index
- Getting started
    Getting started with the model
    FAQ
- Models
Utils
'''

from TestProject import Architecture
from TestProject import Decoder

EXCLUDE = {
    'tests'
}

# For each class to document, it is possible to:
# 1) Document only the class: [classA, classB, ...]
# 2) Document all its methods: [classA, (classB, "*")]
# 3) Choose which methods to document (methods listed as strings):
# [classA, (classB, ["method1", "method2", ...]), ...]
# 4) Choose which methods to document (methods listed as qualified names):
# [classA, (classB, [module.classB.method1, module.classB.method2, ...]), ...]

PAGES = [
    {
        'page': 'Decoder/Main.md',
        'classes': [
            Decoder.MyClass,
            Decoder.Suma
        ]
    },
    {
        'page': 'Decoder/selectName.md',
        'functions': [
            Decoder.selectName.call_architecture
        ]
    },
    {
        'page': 'Architecture/engine.md',
        'classes': [
            Architecture.Engine
        ]
    },
    {
        'page': 'Architecture/event_handler.md',
        'functions': [
            Architecture.event_handler.calling_hello
        ]
    }
]


ROOT = ''

template_np_implementation = """# Numpy implementation
    ```python
{{code}}
    ```
"""

template_hidden_np_implementation = """# Numpy implementation
    <details>
    <summary>Show the Numpy implementation</summary>
    ```python
{{code}}
    ```
    </details>
"""
