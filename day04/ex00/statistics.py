from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate various statistical measures based on input args and kwargs"""
    if not args:
        for key in kwargs.values():
            print("ERROR")
        return

    numbers = sorted(float(x) for x in args)
    n = len(numbers)

    for key, value in kwargs.items():
        if value == "mean":
            mean = sum(numbers) / n
            print(f"mean : {mean}")
        
        elif value == "median":
            if n % 2 == 0:
                median = (numbers[n//2 - 1] + numbers[n//2]) / 2
            else:
                median = numbers[n//2]
            print(f"median : {median}")
        
        elif value == "quartile":
            q1_pos = (n - 1) * 0.25
            q3_pos = (n - 1) * 0.75
            
            q1_int, q1_frac = int(q1_pos), q1_pos - int(q1_pos)
            q3_int, q3_frac = int(q3_pos), q3_pos - int(q3_pos)
            
            q1 = numbers[q1_int] + q1_frac * (numbers[q1_int + 1] - numbers[q1_int])
            q3 = numbers[q3_int] + q3_frac * (numbers[q3_int + 1] - numbers[q3_int])
            
            print(f"quartile : [{q1}, {q3}]")
        
        elif value == "std":
            mean = sum(numbers) / n
            variance = sum((x - mean) ** 2 for x in numbers) / n
            std = variance ** 0.5
            print(f"std : {std}")
        
        elif value == "var":
            mean = sum(numbers) / n
            variance = sum((x - mean) ** 2 for x in numbers) / n
            print(f"var : {variance}")
