/**
 * @param {string} dropMenuName
 * @param {string} tagName
 * @returns {undefined}
 */
export default function setEventDropMenu(dropMenuName, tagName) {
    const dropMenu = document.getElementById(dropMenuName);
    dropMenu.addEventListener("click", (event) => {
        if (event.target.tagName != tagName) {
        	return;
        }

        const url = new URL(location.href);
        url.searchParams.set("type", event.target.id);
        location.assign(url.toString());
    });
}
