from mcp.server.fastmcp import FastMCP
import math

# Initialize the MCP server
mcp = FastMCP("calculator")

#  BASIC OPERATIONS

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together. Example: add(3, 5) → 8"""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a. Example: subtract(10, 4) → 6"""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers. Example: multiply(3, 7) → 21"""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Example: divide(10, 2) → 5"""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool()
def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b. Example: modulo(10, 3) → 1"""
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent. Example: power(2, 10) → 1024"""
    return base ** exponent

#  ADVANCED OPERATIONS

@mcp.tool()
def square_root(a: float) -> float:
    """Return the square root of a number. Example: square_root(144) → 12"""
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


@mcp.tool()
def absolute_value(a: float) -> float:
    """Return the absolute value of a number. Example: absolute_value(-9) → 9"""
    return abs(a)


@mcp.tool()
def logarithm(a: float, base: float = math.e) -> float:
    """Return the logarithm of a. Defaults to natural log (base e).
    Example: logarithm(100, 10) → 2.0"""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(a, base)


@mcp.tool()
def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer. Example: factorial(5) → 120"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n > 20:
        raise ValueError("Input too large. Maximum allowed is 20.")
    return math.factorial(n)


@mcp.tool()
def percentage(value: float, total: float) -> float:
    """Calculate what percentage value is of total. Example: percentage(25, 200) → 12.5"""
    if total == 0:
        raise ValueError("Total cannot be zero.")
    return (value / total) * 100

#  TRIGONOMETRY (angles in degrees)

@mcp.tool()
def sine(degrees: float) -> float:
    """Return the sine of an angle in degrees. Example: sine(90) → 1.0"""
    return round(math.sin(math.radians(degrees)), 10)


@mcp.tool()
def cosine(degrees: float) -> float:
    """Return the cosine of an angle in degrees. Example: cosine(0) → 1.0"""
    return round(math.cos(math.radians(degrees)), 10)


@mcp.tool()
def tangent(degrees: float) -> float:
    """Return the tangent of an angle in degrees. Example: tangent(45) → 1.0"""
    if degrees % 180 == 90:
        raise ValueError("Tangent is undefined at 90° and 270°.")
    return round(math.tan(math.radians(degrees)), 10)



if __name__ == "__main__":
    mcp.run()
