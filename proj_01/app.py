import json

dicionario=[
    {
        "dia": 1,
        "faturamento": 500.00
    },
    {
        "dia": 2,
        "faturamento": 600.00
    },
    {
        "dia": 3,
        "faturamento": 00.00
    },
    {
        "dia": 4,
        "faturamento": 00.00
    },
    {
        "dia": 5,
        "faturamento": 750.00
    },
    {
        "dia": 6,
        "faturamento": 800.00
    },
    {
        "dia": 7,
        "faturamento": 320.00
    },
    {
        "dia": 8,
        "faturamento": 100.00
    },
    {
        "dia": 9,
        "faturamento": 260.00
    },
    {
        "dia": 10,
        "faturamento": 00.00
    },
    {
        "dia": 11,
        "faturamento": 00.00
    },
    {
        "dia": 12,
        "faturamento": 980.00
    },
    {
        "dia": 13,
        "faturamento": 1000.00
    },
    {
        "dia": 14,
        "faturamento": 560.00
    },
    {
        "dia": 15,
        "faturamento": 516.00
    },
    {
        "dia": 16,
        "faturamento": 955.00
    },
    {
        "dia": 17,
        "faturamento": 00.00
    },
    {
        "dia": 18,
        "faturamento": 00.00
    },
    {
        "dia": 19,
        "faturamento": 925.00
    },
    {
        "dia": 20,
        "faturamento": 122.00
    },
    {
        "dia": 21,
        "faturamento": 986.00
    },
    {
        "dia": 22,
        "faturamento": 952.00
    },
    {
        "dia": 23,
        "faturamento": 123.00
    },
    {
        "dia": 24,
        "faturamento": 00.00
    },
    {
        "dia": 25,
        "faturamento": 00.00
    },
    {
        "dia": 26,
        "faturamento": 515.00
    },
    {
        "dia": 27,
        "faturamento": 561.00
    },
    {
        "dia": 28,
        "faturamento": 900.00
    },
    {
        "dia": 29,
        "faturamento": 456.00
    },
    {
        "dia": 30,
        "faturamento": 263.00
    },
    {
        "dia": 31,
        "faturamento": 00.00
    },
]

object_json = json.dumps(dicionario, indent=4)

with open("faturamento.json", "w") as file:
    file.write(object_json)