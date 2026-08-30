import FavoritesApi from "../api/favoritesApi.js";

/**
 * @param {HTMLElement} parent
 * @param {object} data
 */
function appendCard(parent, data) {
    parent.insertAdjacentHTML(
        "beforeend",
        `
        <div class="col mb-3">
            <div class="card h-100" style="max-width: 320px">
            <img src="${data.photo != null ? data.photo : "/assets/no-image.png"}" class="card-img-top" alt="Book Image" height="320px">
            <div class="card-body">
                <h5><a class="card-title text-decoration-none" href="/book?id=${data.id}">${data.name}</a></h5>
                <h6 class="card-text">${data.author}</h6>
                <a class="card-text link-dark text-decoration-none" href="/profile?id=${data.user.id}">${data.user.username}</a>
            </div>
            <div class="card-footer d-flex justify-content-between bg-light">
                <a href="${data.document}" class="btn btn-dark btn-sm">Download</a>
                <button class="btn btn-outline-secondary btn-sm" id="Like-${data.id}">
                    <i class="${data.favorite_id ? "bi bi-heart-fill" : "bi bi-heart"}" 
                    id="Heart-${data.id}" data-id="${data.favorite_id}">
                    </i> ${data.count_favorites}
                </button>
            </div>
        </div>
        `
    );
}

/**
 * @param {Number} bookId
 * @returns {undefined}
 */
function addLikesInCard(bookId) {
    const like = document.querySelector(`#Like-${bookId}`);
    like.addEventListener("click", async () => {
        const number_ = Number.parseInt(like.textContent);
        const id = document.querySelector(`#Heart-${bookId}`).dataset.id;

        if (id !== "null") {
            const response = await FavoritesApi.delete(id);
            if (response.status == 204) {
                like.innerHTML = `<i class="bi bi-heart" id="Heart-${bookId}" data-id="null"></i> ${number_ - 1}`;
            }
            return;
        }

        const response = await FavoritesApi.create({ book: bookId });
        if (response.status == 201) {
            like.innerHTML = `<i class="bi bi-heart-fill" id="Heart-${bookId}" data-id="${response.data.id}"></i> ${number_ + 1}`;
        }
    });
}

/**
 * @param {string} parentId
 * @param {object[]} books
 * @returns {undefined}
 */
export default async function renderCards(parentId, books) {
    let list = document.querySelector(`#${parentId}`);

    for (let item of books) {
        appendCard(list, item);
        addLikesInCard(item.id);
    }
}
