import BookApi from "./api/bookApi.js";
import FavoritesApi from "./api/favoritesApi.js";

let page = 1;

(async function get_cards() {
    const urlParams = new URLSearchParams(window.location.search);
    let res = await BookApi.search(
        urlParams.get("search"),
        urlParams.get("ordering"),
        page
    );

    for (let item of res.data.results) {
        let element = document.getElementById("ListBooks");
        element.insertAdjacentHTML("beforeend",
            `
            <div class="col mb-3">
                <div class="card h-100" style="max-width: 320px">
                <img src="${item.photo != null ? item.photo : "/assets/no-image.png"}" class="card-img-top" alt="Book Image" height="320px">
                <div class="card-body">
                    <h5 class="card-title">${item.name}</h5>
                    <h6 class="card-text">${item.author}</h6>
                    <p class="card-text">${item.user.username}</p>
                </div>
                <div class="card-footer d-flex justify-content-between bg-light">
                    <a href="${item.document}" class="btn btn-dark btn-sm">Download</a>
                    <button class="btn btn-outline-secondary btn-sm" id="Like-${item.id}">
                        <i class="${item.favorite_id ? "bi bi-heart-fill" : "bi bi-heart"}" 
                        id="Heart-${item.id}" data-id="${item.favorite_id}">
                        </i> ${item.count_favorites}
                    </button>
                </div>
            </div>
            `
        );
        const like = document.getElementById(`Like-${item.id}`);
        like.onclick = async () => {
            const num = Number.parseInt(like.textContent)
            const id = document.getElementById(`Heart-${item.id}`).dataset.id
            if (id !== "null") {
                const res = await FavoritesApi.delete(id);
                if (res.status == 204) {
                    like.innerHTML = `<i class="bi bi-heart" id="Heart-${item.id}" data-id="${null}"></i> ${num - 1}`;
                }
            } else {
                const res = await FavoritesApi.create({book: item.id});
                if (res.status == 201) {
                    like.innerHTML = `<i class="bi bi-heart-fill" id="Heart-${item.id}" data-id="${res.data.id}"></i> ${num + 1}`;
                }
            }
            
        }
    }
    
    if (res.data.next != null) {
        let button = document.getElementById("GetAllData");
        button.innerHTML = `<button class="btn btn-dark mt-3" id="GetMore">Get more</button>`;
        button.onclick = () => {
            page++;
            get_cards();
        }
    }
})()

(function get_user() {
    const token = localStorage.getItem("token");
    let element = document.getElementById("NavBarButtons");

    if (token === null) {
        element.innerHTML = '<li><a class="btn btn-outline-ligh" href="/login">Log in</a></li>';
    }
    else {
        element.innerHTML = `<li><button class="btn rounded-circle">+</button></li>
        <li><image src="assets/user-image.jpg" class="d-inline-block align-text-top mx-auto" height="35"</li>`;
    }

})()