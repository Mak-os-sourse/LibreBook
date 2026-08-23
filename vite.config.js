import { defineConfig } from "vite";
import { resolve } from "path";

const ROOT_DIR = "frontend/";

export default defineConfig({
  root: ROOT_DIR,
  build: {
    outDir: "../dist",
    emptyOutDir: true,
    rolldownOptions: {
      checks: {
        pluginTimings: false,
      },
    },
  },
  input: {
    main: resolve(ROOT_DIR, "index.html"),
    regist: resolve(ROOT_DIR, "regist.html"),
    login: resolve(ROOT_DIR, "login.html"),
  },

  css: {
    preprocessorOptions: {
      scss: {
        silenceDeprecations: [
          "import",
          "color-functions",
          "global-builtin",
          "if-function",
        ],
      },
    },
  },
});
