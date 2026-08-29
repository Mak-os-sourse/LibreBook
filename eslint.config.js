import js from "@eslint/js";
import globals from "globals";
import { defineConfig } from "eslint/config";
import simpleImportSort from "eslint-plugin-simple-import-sort";
import sonarjs from 'eslint-plugin-sonarjs';
import unicorn from 'eslint-plugin-unicorn';

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs}"],
    languageOptions: {
			globals: globals.browser,
		},
    plugins: {
      "simple-import-sort": simpleImportSort,
      sonarjs,
      unicorn,
      js,
    },
    extends: [
			'unicorn/recommended',
		],
    rules: {
      "semi": "error",
			"no-unused-vars": "warn",
			"no-undef": "warn",
      "simple-import-sort/imports": "error",
      "simple-import-sort/exports": "error",
      "sonarjs/no-implicit-dependencies": "error",
      "unicorn/prefer-module": "error",
		},
  }
]);
