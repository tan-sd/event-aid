import { createRouter, createWebHistory } from "vue-router";
import Landing from "../views/Landing.vue";
import Login from "../views/Login.vue";
import Home from "../views/Home.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "landing",
            component: Landing,
        },
        {
            path: "/login",
            name: "login",
            component: Login,
        },
        {
            path: "/home",
            name: "home",
            component: Home,
        },
    ],
});

export default router;
