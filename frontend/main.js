import BookApi from "./api/bookApi.js";
import renderCards from "./components/card.js";
import setEventDropMenu from "./components/dropMenu.js";

let page = 1;

setEventDropMenu("DropMenu", "A");

(async function getCards() {
    const urlParameters = new URLSearchParams(location.search);
    const search = urlParameters.get("search");
    const type = urlParameters.get("type");
    let ordering;

    if (search != undefined && search != "") {
        document.querySelector("#SearchQueryTitle").textContent =
            `Found for the query "${search}"`;
    }

    if (type != undefined) {
        document.querySelector("#DropdownMenuButton").textContent =
            document.getElementById(type).textContent;
    }
    switch (type) {
        case "popular": {
            ordering = "-count_favorites";
            break;
        }
        case "news": {
            ordering = "-create_at";
            break;
        }
    }

    const res = await BookApi.search({
        search: search,
        ordering: ordering,
        page: page,
    });

    if (res.status != 200) {
        return;
    }
    renderCards("ListBooks", res.data.results);

    if (res.data.next != undefined) {
        let button = document.querySelector("#GetAllData");
        button.innerHTML = `<button class="btn btn-dark mt-3" id="GetMore">Get more</button>`;
        button.addEventListener('click', () => {
            page++;
            getCards();
        });
    }
})();
