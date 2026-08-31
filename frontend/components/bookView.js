import CommentApi from "../api/commentApi.js";

/**
 * @param {object} book
 * @returns {undefined}
 */
function renderBookView(book) {
    document.querySelector("#BookImage").src =
        book.photo ?? "assets/no-image.png";
    document.querySelector("#BookTitle").textContent = book.name;
    document.querySelector("#AuthorName").textContent = book.author;
    document.querySelector("#PublishedBy").textContent = book.user.username;
    document.querySelector("#PublishedBy").href = `/profile?id=${book.user.id}`;
    document.querySelector("#Description").textContent = book.description;
    document.querySelector("#Download").href = book.document;
}

/**
 * @param {Element} element
 * @param {object} item
 * @param {string} position
 * @returns {undefined}
 */
function renderComment(element, item, position) {
    element.insertAdjacentHTML(
        position,
        `<div class="bg-light border rounded-3 p-3 mb-3">
            <div class="d-flex justify-content-between">
                <a class="fw-semibold link-dark" href="/profile?id=${item.user.id}">${item.user.username}</a>
                <span class="text-muted small">${item.create_at}</span>
            </div>
            <p class="mb-0">
                ${item.content}
            </p>
        </div>`
    );
}

/**
 * @param {object[]} comments
 * @returns {undefined}
 */
function renderComments(comments) {
    const element = document.querySelector("#ListComments");
    for (const item of comments) {
        renderComment(element, item, "beforeend");
    }
}

function sendComment() {
    const CommentForm = document.querySelector("#CommentForm");
    CommentForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const urlParameters = new URLSearchParams(location.search);
        const response = await CommentApi.create({
            book: urlParameters.get("id"),
            content: document.querySelector("#comment").value,
        });
        if (response.status == 201) {
            const element = document.querySelector("#ListComments");
            renderComment(element, response.data, "afterbegin");
        }
    });
}

export { renderBookView, renderComments, sendComment };
