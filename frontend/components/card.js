import FavoritesApi from "../api/favoritesApi.js";

function append_card(parent, data) {
    parent.insertAdjacentHTML(
        "beforeend",
        `
        <div class="col mb-3">
            <div class="card h-100" style="max-width: 320px">
            <img src="${data.photo != null ? data.photo : "/assets/no-image.png"}" class="card-img-top" alt="Book Image" height="320px">
            <div class="card-body">
                <h5 class="card-title">${data.name}</h5>
                <h6 class="card-text">${data.author}</h6>
                <p class="card-text">${data.user.username}</p>
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

function add_likes_in_card(bookId) {
    const like = document.getElementById(`Like-${bookId}`);
    like.onclick = async () => {
        const num = Number.parseInt(like.textContent);
        const id = document.getElementById(`Heart-${bookId}`).dataset.id;

        if (id !== "null") {
            const res = await FavoritesApi.delete(id);
            if (res.status == 204) {
                like.innerHTML = `<i class="bi bi-heart" id="Heart-${bookId}" data-id="${null}"></i> ${num - 1}`;
            }
            return;
        }

        const res = await FavoritesApi.create({ book: bookId });
        if (res.status == 201) {
            like.innerHTML = `<i class="bi bi-heart-fill" id="Heart-${bookId}" data-id="${res.data.id}"></i> ${num + 1}`;
        }
    };
}

/**
 * @param {object[]} books
 * @returns {undefined}
 */
async function render_cards(books) {
    let list = document.getElementById("ListBooks");

    for (let item of books) {
        append_card(list, item);
        add_likes_in_card(item.id);
    }
}

export default render_cards;
