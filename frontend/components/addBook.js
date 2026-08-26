import BookApi from "../api/bookApi";

const BookForm = document.getElementById("BookForm");
BookForm.addEventListener("submit", addBook);

/**
 * @param {Event} event
 */
async function addBook(event) {
    event.preventDefault();
    const data = new FormData(BookForm);

    const book = await BookApi.create({
        name: data.get("name"),
        description: data.get("description"),
        author: data.get("author"),
    });
    const resDocument = await BookApi.updateDocument(
        book.data.id,
        data.get("document")
    );
    const resImage = await BookApi.updateImage(book.data.id, data.get("photo"));
    if (resDocument.status != 200 || resImage.status != 200) {
        await BookApi.delete(book.data.id);
        document.getElementById("AddBookInfo").innerHTML =
            `<div class="alert alert-danger pt-2" role="alert">
        The photograph must be in png or jpeg format, and the document in pdf format.</div>`;
        return;
    }
    window.location.href = "/";
}
