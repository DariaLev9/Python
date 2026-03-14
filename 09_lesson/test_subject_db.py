from sqlalchemy import create_engine
from sqlalchemy import text


db_connection_string = (
    "postgresql://postgres:sky7654647@localhost:5432/postgres"
)
db = create_engine(db_connection_string)


# Проверим что есть коннект с БД
def test_db_connection():
    result = db.execute("SELECT 1").fetchone()
    assert result[0] == 1


# Добавление
def test_add_subject():
    # 1.Берём максимальный id
    max_id_rows = db.execute(
        text("SELECT MAX(subject_id) FROM subject")
    ).fetchall()

    max_id = max_id_rows[0][0]
    new_id = max_id + 1

    subject_title = "test_subject_add"

    # 2.Добавляем запись
    db.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        id=new_id,
        title=subject_title
    )

    # 3.Проверяем, что запись добавилась
    rows = db.execute(
        text(
            "SELECT subject_id, "
            "subject_title FROM subject WHERE subject_id = :id"
        ),
        id=new_id
    ).fetchall()

    assert len(rows) == 1
    assert rows[0]["subject_id"] == new_id
    assert rows[0]["subject_title"] == subject_title

    # 4.Удаляем запись
    db.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        id=new_id
    )


# Изменение
def test_update_subject():
    # 1.Новый id
    max_id_rows = db.execute(
        text("SELECT MAX(subject_id) FROM subject")).fetchall()
    new_id = max_id_rows[0][0] + 1

    title_before = "test_subject_before"
    title_after = "test_subject_after"

    # 2.Создаём запись для изменения
    db.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        id=new_id,
        title=title_before
    )

    # 3.Обновляем
    db.execute(
        text(
            "UPDATE subject SET subject_title = :title "
            "WHERE subject_id = :id"
        ),
        id=new_id,
        title=title_after
    )

    # 4.Проверяем
    rows = db.execute(
        text(
            "SELECT subject_id, subject_title FROM subject "
            "WHERE subject_id = :id"
        ),
        id=new_id
    ).fetchall()

    assert len(rows) == 1
    assert rows[0]["subject_title"] == title_after

    # 5.Удаляем запись
    db.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        id=new_id
    )


# Удаление
def test_delete_subject():
    # 1.Новый id
    max_id_rows = db.execute(
        text("SELECT MAX(subject_id) FROM subject")
    ).fetchall()
    new_id = max_id_rows[0][0] + 1

    subject_title = "test_subject_to_delete"

    # 2.Создаём запись
    db.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        id=new_id,
        title=subject_title
    )

    # 3.Удаляем запись
    db.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        id=new_id
    )

    # 4.Проверяем, что записи нет
    rows = db.execute(
        text("SELECT subject_id FROM subject WHERE subject_id = :id"),
        id=new_id
    ).fetchall()

    assert len(rows) == 0
