import BaseApi from "./baseApi.js";

class CommentApi extends BaseApi {
    constructor() {
        super("/comment/");
    }

    update = undefined;
}

export default new CommentApi();
