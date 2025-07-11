import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""### 这个是我第一个marimo的笔记想做marimo的测试""")
    return


@app.cell
def _():
    print("hello") # cmd + enter可以运行   
    return


@app.cell
def _():
    json_path = 'sample-file.json'
    return (json_path,)


@app.cell
def _(json_path, mo):
    query = mo.sql(
        f"""
        SELECT * FROM read_json_auto('{json_path}')
        LIMIT 10
        """
    )
    return


if __name__ == "__main__":
    app.run()
