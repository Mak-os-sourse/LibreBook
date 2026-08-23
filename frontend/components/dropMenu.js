const dropMenu = document.getElementById("DropMenu");
dropMenu.addEventListener("click", (event) => {
    if (event.target.tagName == "A") {
        const url = new URL(window.location.href);
        switch (event.target.textContent) {
            case "Popular":
                url.searchParams.set("ordering", "-count_favorites");
                break;
            case "News":
                url.searchParams.set("ordering", "-create_at");
                break;
        }
        window.location.href = url.toString();
    }
});
