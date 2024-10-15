def solution(data, ext, val_ext, sort_by):
    inform_doc = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    return sorted([i for i in data if i[inform_doc[ext]] < val_ext], key=lambda x: x[inform_doc[sort_by]])