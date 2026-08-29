/**
 * @param {object} user
 * @returns {undefined}
 */
function renderProfile(user) {
    document.querySelector("#Username").textContent = user.username;
    document.querySelector("#Name").textContent = user.name;
}

export { renderProfile };
