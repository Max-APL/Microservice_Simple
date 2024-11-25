import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import SalesList from "@/views/SalesList.vue";
import CreateSale from "@/views/CreateSale.vue";
import ProductList from "@/components/ProductList.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/ventas",
    name: "sales",
    component: SalesList,
  },
  {
    path: "/crear_venta",
    name: "createSales",
    component: CreateSale,
  },
  {
    path: "/productos",
    name: "products",
    component: ProductList,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
