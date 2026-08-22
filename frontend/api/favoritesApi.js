import BaseApi from "./baseApi.js";

class FavoritesApi extends BaseApi {
    constructor() {
        super("/favorites/")
    }

    update = undefined;
}

export default new FavoritesApi();