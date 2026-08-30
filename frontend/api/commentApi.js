import BaseApi from "./baseApi.js";

class CommentApi extends BaseApi {
    constructor() {
        super("/comment/");
        this.update = undefined;
    }
}

export default new CommentApi();
