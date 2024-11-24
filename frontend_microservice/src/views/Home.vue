<template>
  <div>
    <HeaderComponent />
    <ProductList />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from '@/components/Header.vue';
import ProductList from '@/components/ProductList.vue';
import FooterComponent from '@/components/Footer.vue';

export default {
  name: 'HomeView',
  components: {
    HeaderComponent,
    ProductList,
    FooterComponent,
  },
};
</script>

<style scoped>
/* Estilos específicos para la vista Home */
</style>