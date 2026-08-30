import BookApi from "../api/bookApi";

const BookForm = document.querySelector("#BookForm");
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
    const responseDocument = await BookApi.updateDocument(
        book.data.id,
        data.get("document")
    );
    const responseImage = await BookApi.updateImage(
        book.data.id,
        data.get("photo")
    );
    if (responseDocument.status != 200 || responseImage.status != 200) {
        await BookApi.delete(book.data.id);
        document.querySelector("#AddBookInfo").innerHTML =
            `<div class="alert alert-danger pt-2" role="alert">
        The photograph must be in png or jpeg format, and the document in pdf format.</div>`;
        return;
    }
    location.assign("/");
}
