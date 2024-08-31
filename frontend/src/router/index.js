import { createRouter, createWebHistory } from "vue-router";
import Landing from "../views/Landing.vue";
import Login from "../views/Login.vue";
import ElderlyHome from "../views/ElderlyHome.vue";
import PlannerHome from "../views/PlannerHome.vue";

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
            path: "/elderlyHome",
            name: "elderlyHome",
            component: ElderlyHome,
        },
        {
            path: "/plannerHome",
            name: "plannerHome",
            component: PlannerHome,
        },
    ],
});

export default router;
