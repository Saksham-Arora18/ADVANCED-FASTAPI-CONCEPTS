from fastapi import FastAPI, Query

app = FastAPI()


fake_items_db = [{"item_name": f"Item {i}"} for i in range(1, 101)]  # 100 items


@app.get("/items")
def get_items(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100)):
    start = (page - 1) * limit
    end = start + limit

    total_items = len(fake_items_db)
    total_pages = (total_items + limit - 1) // limit  # ceiling division

    paginated_items = fake_items_db[start:end]

    return {
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "total_pages": total_pages,
        "items": paginated_items
    }