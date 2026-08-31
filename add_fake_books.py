import httpx, sys, time

GUTENDEX_URL = "https://gutendex.com/books/"

def main(
    base_url: str, field: str,
    password: str, count: int
):
    res = httpx.post(
        f"{base_url}api/user/login",
        json={
            "field": field,
            "password": password,
        }
    )
    
    if res.status_code != 200:
        print(f"Status code: {res.status_code}❌")
        sys.exit()
    else:
        print(f"Status code: {res.status_code}✅") 
    
    access_token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
 
    imported = 0
    page = 1
 
    while imported < count:
        res = httpx.get(GUTENDEX_URL, params={"page": page}, timeout=30, trust_env=False)
        if res.status_code != 200:
            print(f"Gutendex request failed: {res.status_code}")
            break
 
        results = res.json().get("results", [])
        if not results:
            break
 
        for item in results:
            if imported >= count:
                break
 
            formats = item.get("formats", {})
            pdf_url = formats.get("application/pdf")
            cover_url = formats.get("image/jpeg")
            title = (item.get("title") or "").strip()[:50]
            if not pdf_url or not cover_url or len(title) < 4:
                continue 
 
            authors = item.get("authors") or []
            author = (authors[0]["name"] if authors else "Unknown")[:100]
 
            summaries = item.get("summaries") or []
            description = summaries[0][:500] if summaries else ""
 
            payload = {"name": title, "author": author}
            if description:
                payload["description"] = description
 
            res = httpx.post(f"{base_url}api/book/", data=payload, headers=headers)
            if res.status_code != 201:
                print(f"create failed: {res.status_code} {res.text[:200]}")
                continue
            book_id = res.json()["id"]
 
            cover_bytes = httpx.get(cover_url, follow_redirects=True, timeout=15).content
            res = httpx.post(
                f"{base_url}api/book/update-image",
                data={"book_id": book_id},
                files={"file": ("cover.jpg", cover_bytes)},
                headers=headers,
            )
            if res.status_code != 200:
                print(f"photo upload failed: {res.status_code}")
 
            pdf_bytes = httpx.get(pdf_url, follow_redirects=True, timeout=15).content
            res = httpx.post(
                f"{base_url}api/book/update-document",
                data={"book_id": book_id},
                files={"file": ("book.pdf", pdf_bytes)},
                headers=headers,
            )
            if res.status_code != 200:
                print(f"document upload failed: {res.status_code}")
 
            imported += 1
            print(f"[{imported}/{count}] {title} {author}")
            time.sleep(1)
 
        page += 1
 
    print(f"\nDone: {imported}/{count} books imported.")

    
if __name__ == "__main__":
    base_url = input("BaseUrl (http://localhost/): ") or "http://localhost/"
    field = input("Username or email: ")
    password = input("Password: ")
    count = int(input("Count (100): ") or 100)
    
    if base_url[-1] != "/":
        base_url += 1
    
    main(base_url, field, password, count)