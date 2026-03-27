from fastapi import FastAPI
from fastapi_mcp import FASTAPiMCP

app = FastAPI(title="Calculator API")

@app.post("/multiply")
def multiply(a:float,b:float):
    """
    Multiply two numbers and returns the result
    
    """

    result = a * b

    return {"result": result}


@app.post("/add")
def add(a:float,b:float):
    """
    Add two numbers and returns the result
    
    """

    result = a + b

    return {"result ": result}


@app.post("/subtraction")
def subtraction(a:float,b:float):
    """
    Subtract two numbers and returns the result
    
    """

    result = a - b

    return {"result ": result}

@app.post("/division")
def division(a:float,b:float):
    """
    Divide two numbers and returns the result
    
    """
    if b==0:
        return {"Error":"Divsion by zero is not allowed"}

    result = a / b

    return {"result ": result}



# Converting into mcp
mcp=FASTAPiMCP(app,name="Calculator mcp")
mcp.mount()

if __name__ == "__main__":
    import uvicorn
    print("Starting the Calculator API server...")
    uvicorn.run(app, host="localhost", port=8002)

