import { createRouter, createWebHistory } from 'vue-router'

import Home from './views/Home.vue'
import About from './views/About.vue'
import NotFound from './views/NotFound.vue'

const routes = [
    {
        name: 'Home',
        path: '/',
        component: Home
    },
    {
        name: 'About',
        path: '/about',
        component: About
    },
    {
        // wildcard for missing route
        name: 'not-found',
        path: '/:pathMatch(.*)*',
        component: NotFound
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// wildcard handler
router.resolve({
    name: 'not-found',
    params: { pathMatch: ['not', 'found'] },
})

export default router