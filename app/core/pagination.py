from sqlalchemy.orm import Query

def paginate(query: Query, page: int, size: int):
    if page < 1:
        page = 1
    if size < 1:
        size = 10

    return query.offset((page - 1) * size).limit(size)