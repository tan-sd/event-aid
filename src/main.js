import "./assets/main.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faPlus } from "@fortawesome/free-solid-svg-icons";

/* add icons to the library */
library.add(faPlus)

const app = createApp(App);

app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router);

app.mount("#app");
