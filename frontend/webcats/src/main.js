import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import {ColorPicker, ColorPanel} from 'one-colorpicker'
// import "./assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(ColorPicker)
app.use(ColorPanel)
app.use(ColorPicker)
app.mount("#app");
