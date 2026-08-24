/**
 * @param {string} dropMenuName
 * @param {string} tagName
 * @returns {undefined}
 */
function setEventDropMenu(dropMenuName, tagName) {
    const dropMenu = document.getElementById(dropMenuName);
    dropMenu.addEventListener("click", (event) => {
        if (event.target.tagName == tagName) {
            const url = new URL(window.location.href);
            url.searchParams.set("type", event.target.textContent);
            window.location.href = url.toString();
        }
    });
}

export default setEventDropMenu;
