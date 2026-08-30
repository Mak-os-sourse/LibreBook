import BookApi from "./api/bookApi.js";
import renderCards from "./components/card.js";
import setEventDropMenu from "./components/dropMenu.js";

setEventDropMenu("DropMenu", "A");

await (async function getCards(page = 1) {
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
            document.querySelector(`#${type}`).textContent;
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

    const response = await BookApi.search({
        search: search,
        ordering: ordering,
        page: page,
    });

    if (response.status != 200) {
        return;
    }
    renderCards("ListBooks", response.data.results);

    if (response.data.next != undefined) {
        let button = document.querySelector("#GetAllData");
        button.innerHTML = `<button class="btn btn-dark mt-3" id="GetMore">Get more</button>`;
        button.addEventListener("click", () => {
            getCards(page + 1);
        });
    }
})();
