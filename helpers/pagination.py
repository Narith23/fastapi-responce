import math
from sqlalchemy import func


class Page:
    pass


class Page(object):
    """ Pagination Util for List data"""

    def __init__(self, items, page, page_size, total):
        self.data = items
        self.page_size = len(items)
        self.previous_page = None
        self.next_page = None
        self.has_previous = page > 1
        if self.has_previous:
            self.previous_page = page - 1
        previous_items = (page - 1) * page_size
        self.has_next = previous_items + len(items) < total
        if self.has_next:
            self.next_page = page + 1
        self.total_items = total
        self.pages = int(math.ceil(total / float(page_size)))


def paginate(query, db, model, page, page_size, condition) -> Page:
    if page <= 0:
        raise AttributeError('page needs to be >= 1')
    if page_size <= 0:
        raise AttributeError('page_size needs to be >= 1')
    statement = query.limit(page_size).offset((page - 1) * page_size)
    results = db.exec(statement)
    items = results.all()
    if condition=="swdepartments":
        condition = model.departmentid
        total = db.execute(func.count(condition)).scalar()
    elif condition=="swtickets":
        condition = model.ticketid
        total = db.execute(func.count(condition)).scalar()
    else:
        total = db.execute(func.count(model.id)).scalar()
    return Page(items, page, page_size, total)
