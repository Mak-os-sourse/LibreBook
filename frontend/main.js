import BookApi from "./api/bookApi.js";
import UserApi from "./api/userApi.js";
import render_cards from "./components/card.js";
import "./components/dropMenu.js";

let page = 1;

(async function get_cards() {
    const urlParams = new URLSearchParams(window.location.search);
    const res = await BookApi.search({
        search: urlParams.get("search"),
        ordering: urlParams.get("ordering"),
        page: page,
    });

    if (res.status == 200) {
        render_cards(res.data.results);

        if (res.data.next != null) {
            let button = document.getElementById("GetAllData");
            button.innerHTML = `<button class="btn btn-dark mt-3" id="GetMore">Get more</button>`;
            button.onclick = () => {
                page++;
                get_cards();
            };
        }
    }
})();

(async function get_user() {
    const res = await UserApi.getMe();
    let element = document.getElementById("NavBarButtons");

    if (res.status != 200) {
        element.innerHTML =
            '<li><a class="btn btn-outline-ligh" href="/login">Log in</a></li>';
    } else {
        element.innerHTML = `<li><button class="btn rounded-circle">+</button></li>
        <li><image src="assets/user-image.jpg" class="d-inline-block align-text-top mx-auto" height="35"</li>`;
    }
})();
