import BookApi from "./api/bookApi.js";
import renderCards from "./components/card.js";
import setEventDropMenu from "./components/dropMenu.js";

let page = 1;

setEventDropMenu("DropMenu", "A");

(async function getCards() {
    const urlParams = new URLSearchParams(window.location.search);
    const search = urlParams.get("search");
    const type = urlParams.get("type");
    let ordering;

    if (search != null && search != "") {
        document.getElementById("SearchQueryTitle").textContent =
            `Found for the query "${search}"`;
    }

    document.getElementById("DropdownMenuButton").textContent = type;
    switch (type) {
        case "Popular":
            ordering = "-count_favorites";
            break;
        case "News":
            ordering = "-create_at";
            break;
    }

    const res = await BookApi.search({
        search: search,
        ordering: ordering,
        page: page,
    });

    if (res.status != 200) {
        return;
    }
    renderCards(res.data.results);

    if (res.data.next != null) {
        let button = document.getElementById("GetAllData");
        button.innerHTML = `<button class="btn btn-dark mt-3" id="GetMore">Get more</button>`;
        button.onclick = () => {
            page++;
            getCards();
        };
    }
})();