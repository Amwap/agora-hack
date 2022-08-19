import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/Home.vue"),
    },
    {
      path: "/editor",
      name: "about",
      component: () => import("../views/Editor.vue"),
    },
    {
      path: "/preview",
      name: "about",
      component: () => import("../views/Preview.vue"),
    },
  ],
});

export default router;
