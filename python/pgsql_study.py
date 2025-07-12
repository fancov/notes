import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        rf"""
    ## 安装&启动
    我使用了brew安装postgresql

    ```shell
    brew install postgresql@17
    ```

    然后使用 brew 启动了
    ```
    brew services start postgresql@17
    ```


    ```
    brew services list
    Name          Status  User File
    mysql         none    fc   
    postgresql@17 started fc   ~/Library/LaunchAgents/homebrew.mxcl.postgresql@17.plist
    ssdb          none   
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 连接
    ### 安装位置
    ```
    /usr/local/opt/postgresql@17
    ```
    然后需要把`/usr/local/opt/postgresql@17/bin`添加到系统path

    有以下命令：

    ```
    /usr/local/opt/postgresql@17/bin  
    ls
    clusterdb		pg_amcheck		pg_ctl			pg_rewind		postgres
    createdb		pg_archivecleanup	pg_dump			pg_test_fsync		psql
    createuser		pg_basebackup		pg_dumpall		pg_test_timing		reindexdb
    dropdb			pg_checksums		pg_isready		pg_upgrade		vacuumdb
    dropuser		pg_combinebackup	pg_receivewal		pg_verifybackup		vacuumlo
    ecpg			pg_config		pg_recvlogical		pg_waldump
    initdb			pg_controldata		pg_resetwal		pg_walsummary
    oid2name		pg_createsubscriber	pg_restore		pgbench
    ```

    psql是客户端
    ```
    psql -d postgres
    ```
    -d代表database
    使用brew安装好的postgresql默认会有一个数据库postgres，一开始没有用户，密码，所以可以直接像上面那样连接

    ```
    psql -d postgres
    psql (17.5 (Homebrew))
    Type "help" for help.

    postgres=#
    ```
    ![](public/psql_login.png)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 执行sql
    教程：  
    https://neon.com/postgresql/tutorial
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## 试试使用python执行""")
    return


@app.cell
def _():
    import psycopg2

    ## Data Source Name
    POSTGRESQL_DSN = "postgresql://fc:123456@127.0.0.1:5432/dvdrental"

    ## conn负责管理连接，事务
    conn = psycopg2.connect(dsn=POSTGRESQL_DSN)   
    cursor = conn.cursor()

    return conn, cursor


@app.cell
def _(conn):
    dir(conn)
    return


@app.cell
def _(cursor):
    dir(cursor)
    return


@app.cell
def _():
    from inspect import getmembers
    return (getmembers,)


@app.cell
def _(conn, getmembers):
    getmembers (conn)  
    return


@app.cell
def _(cursor):
    query_sql = """
    SELECT
      title,
      rental_rate
    FROM
      film
    WHERE
      rental_rate = 0.99 OR
      rental_rate = 2.99;
    """
    cursor.execute(query_sql)
    return (query_sql,)


@app.cell
def _(cursor):
    type(cursor.fetchall())   
    return


@app.cell
def _(cursor):
    type(cursor.fetchone())
    return


app._unparsable_cell(
    r"""
    cursor.execute(query_sql)
    type(cursor.fetchone()
    """,
    name="_"
)


@app.cell
def _(cursor, query_sql):
    cursor.execute(query_sql)
    cursor.fetchmany(10)
    return


@app.cell
def _(cursor):
    cursor.close()
    return


@app.cell
def _(conn):
    conn.close()
    return


@app.cell
def _():
    import os
    import sqlalchemy

    _password = os.environ.get("POSTGRES_PASSWORD", "123456")
    DATABASE_URL = f"postgresql://fc:{_password}@127.0.0.1:5432/dvdrental"
    engine = sqlalchemy.create_engine(DATABASE_URL)       
    return (engine,)


@app.cell
def _(engine, getmembers):
    from sqlalchemy import text

    sqlalchemy_conn = engine.connect()
    getmembers(sqlalchemy_conn)
    return sqlalchemy_conn, text


@app.cell
def _(text):
    text_sql_obj = text("select 'hello world'")
    dir(text_sql_obj)
    return (text_sql_obj,)


@app.cell
def _(sqlalchemy_conn, text_sql_obj):
    result = sqlalchemy_conn.execute(text_sql_obj)   
    result
    return (result,)


@app.cell
def _(result):
    result.all()
    return


@app.cell
def _(result):
    dir(result)
    return


@app.cell
def _(engine, query_sql, text):
    from sqlalchemy.orm import Session

    with Session(engine) as session: # 这个session根上面的conn区别不大
        result2 = session.execute(text(query_sql))
        for row in result2:
            print(row) 
            break
    print(dir(row))
    print(row.title)
    print(row._fields)
    print(row.rental_rate)

    return


if __name__ == "__main__":
    app.run()
